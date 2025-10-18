🩺 Medical VoiceBot — AI Doctor with Vision & Voice

Medical VoiceBot is an AI-powered multimodal assistant that listens to patients, analyzes images, and responds with a human-like doctor’s voice. It combines speech recognition, image understanding, and text-to-speech to create an interactive, conversational medical experience.

🚀 Features

   Voice Input: Patients can ask questions by speaking.

   AI Diagnosis: Uses Groq’s multimodal Llama model to analyze speech and optional medical images.

   Image Analysis: Evaluates uploaded photos for visible conditions.

   Doctor’s Voice: Responds naturally using gTTS (Google Text-to-Speech).

🧩 Tech Stack

   Groq API — Multimodal LLM & Whisper speech-to-text
  
   Gradio — Intuitive web interface
    
   gTTS + pydub — Text-to-speech synthesis
    
   Python — Core logic and orchestration

🧠 How It Works

   User speaks their question and optionally uploads an image.
  
   The voice is transcribed using Groq Whisper (STT).
  
   The transcribed text + image are analyzed by Groq’s multimodal Llama model.
  
   The AI doctor’s response is generated and spoken aloud.

🌐 Live Demo

   Try it here: https://medical-voicebot.onrender.com/

📜 Note

   This project is for educational and research purposes only and not a substitute for professional medical advice.
