# Step 1: Setup audio recorder using sounddevice
import logging
import sounddevice as sd
from pydub import AudioSegment

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def record_audio(file_path, duration=5, fs=44100):
    try:
        logging.info("Start speaking now...")
        audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype="int16")
        sd.wait()
        logging.info("Recording complete...")

        audio_segment = AudioSegment(
            audio.tobytes(),
            frame_rate=fs,
            sample_width=audio.dtype.itemsize,
            channels=1,
        )
        audio_segment.export(file_path, format="mp3", bitrate="128k")
        logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


# audio_filepath = "patient_voice_test.mp3"
# record_audio(file_path=audio_filepath)

# Step 2: Setup speech to text STT model for transcription
import os
from groq import Groq

from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

stt_model = "whisper-large-v3"


def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)

    audio_file = open(audio_filepath, "rb")
    transcription = client.audio.transcriptions.create(
        model=stt_model, file=audio_file, language="en"
    )

    return transcription.text
