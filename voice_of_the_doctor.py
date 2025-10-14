# Step 1: Setup text to speech TTS model with gTTS
from gtts import gTTS
from pydub import AudioSegment


def text_to_speech_with_gtts_old(input_text, output_filepath):
    language = "en"

    audio_obj = gTTS(text=input_text, lang=language, slow=False)
    audio_obj.save(output_filepath)


input_text = "How's the weather today?"
# text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")


# Step 2: Create a function to autoplay the voice of the doctor
import subprocess
import platform
import os


def text_to_speech_with_gtts(input_text, output_filepath="doctor_voice.wav"):
    language = "en"
    tts = gTTS(text=input_text, lang=language, slow=False)

    # Save as MP3 first
    temp_mp3 = "temp_tts.mp3"
    tts.save(temp_mp3)

    # Convert MP3 → WAV
    sound = AudioSegment.from_mp3(temp_mp3)
    sound.export(output_filepath, format="wav")
    os.remove(temp_mp3)

    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(["afplay", output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(
                [
                    "powershell",
                    "-c",
                    f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();',
                ]
            )
        elif os_name == "Linux":  # Linux
            subprocess.run(["aplay", output_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


# input_text = "You must increase your water intake"
# text_to_speech_with_gtts(input_text=input_text)
