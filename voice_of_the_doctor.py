# Step 1: Setup text to speech TTS model with gTTS
from gtts import gTTS


def text_to_speech_with_gtts_old(input_text, output_filepath):
    language = "en"

    audio_obj = gTTS(text=input_text, lang=language, slow=False)
    audio_obj.save(output_filepath)


input_text = "How's the weather today?"
# text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")


# Step 2: Create a function to autoplay the voice of the doctor
from gtts import gTTS
import pygame
import time


def text_to_speech_with_gtts(input_text, output_filepath):
    # Generate MP3
    tts = gTTS(text=input_text, lang="en", slow=False)
    tts.save(output_filepath)

    # Initialize pygame mixer
    pygame.mixer.init()
    time.sleep(0.07)
    pygame.mixer.music.load(output_filepath)
    pygame.mixer.music.play()

    # Wait for the audio to finish
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)


# input_text = "You must increase your water intake"
# text_to_speech_with_gtts(
#     input_text=input_text, output_filepath="gtts_testing_autoplay.mp3"
# )
