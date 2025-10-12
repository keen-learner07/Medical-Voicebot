# Voicebot UI with gradio
import os
import gradio as gr
from brain_of_the_doctor import encode_image, analyse_image_with_query
from voice_of_the_patient import transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts

system_prompt = """You have to act as a professional doctor, I know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Don't add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Don't say 'In the image I see' but say 'With what I see, I think you have ....'
            Don't respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""


def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = transcribe_with_groq(
        stt_model="whisper-large-v3",
        audio_filepath=audio_filepath,
        GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
    )

    # Handle the image input
    if image_filepath:
        doctor_response = analyse_image_with_query(
            query=system_prompt + speech_to_text_output,
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            encoded_image=encode_image(image_filepath),
        )
    else:
        doctor_response = "No image provided to analyse"

    voice_of_the_doctor = text_to_speech_with_gtts(doctor_response, "final.mp3")

    return speech_to_text_output, doctor_response, voice_of_the_doctor


# Create the interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath", label="Record your question"),
        gr.Image(type="filepath"),
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="AI Doctor's Response", lines=10, interactive=False),
        gr.Audio("filepath"),
    ],
    title="AI Doctor with Vision and Voice",
)

iface.launch(debug=True, share=False, inbrowser=True)
