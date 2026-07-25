# Voicebot UI with gradio
import os
import gradio as gr
from brain_of_the_doctor import encode_image, analyse_image_with_query
from voice_of_the_patient import transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts

system_prompt = """Act as an experienced medical doctor.

Analyze the uploaded image together with the patient's question.

Refer to "the image" instead of "the images".

State the most likely condition using phrases like "This appears to be..." or "This looks most consistent with...".

Briefly mention possible causes and one or two home care recommendations.

If there are signs that require urgent medical evaluation, mention them.

Do not explain your reasoning.
Do not use markdown.
Do not use bullet points.
Do not mention that you are an AI.
Respond in plain English using no more than three sentences."""


def process_inputs(audio_filepath, image_filepath):
    # print("process_inputs called")
    speech_to_text_output = transcribe_with_groq(
        stt_model="whisper-large-v3",
        audio_filepath=audio_filepath,
        GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
    )

    # Handle the image input
    if image_filepath:
        doctor_response = analyse_image_with_query(
            prompt=system_prompt,
            query=speech_to_text_output,
            model="qwen/qwen3.6-27b",
            encoded_image=encode_image(image_filepath),
        )
    else:
        doctor_response = "No image provided to analyse"

    # print("\n----- RAW MODEL RESPONSE -----")
    # print(doctor_response)
    # print("------------------------------\n")

    mp3_path = "final.mp3"
    text_to_speech_with_gtts(doctor_response, mp3_path)

    return speech_to_text_output, doctor_response, mp3_path


port = int(os.environ.get("PORT", 7860))

# Create the interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(
            sources=["microphone"],
            type="filepath",
            label="Record your question",
            autoplay=False,
        ),
        gr.Image(type="filepath"),
    ],
    outputs=[
        gr.Textbox(label="Your question", lines=2),
        gr.Textbox(label="AI Doctor's Response", lines=10, interactive=False),
        gr.Audio(type="filepath", label="AI Doctor's Voice", autoplay=False),
    ],
    title="AI Doctor with Vision and Voice",
)

iface.launch(server_name="0.0.0.0", server_port=port)
# iface.launch(share=False, inbrowser=True)
