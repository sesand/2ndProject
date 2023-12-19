#1
"""
import os
from google.cloud import speech_v1p1beta1 as speech
from google.cloud import texttospeech_v1 as texttospeech
from google.cloud.translate_v2 import Client
from google.cloud import translate_v2 as translate
from twilio.rest import Client

# Set your Google Cloud API credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/credentials.json"

# Set your Twilio credentials
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_phone_number"
EMERGENCY_PHONE_NUMBER = "emergency_phone_number"

# Initialize Google Cloud clients
speech_client = speech.SpeechClient()
translate_client = translate.Client()
text_to_speech_client = texttospeech.TextToSpeechClient()

# Twilio client
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def speech_to_text(audio_file_path):
    with open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="ta-IN",
    )

    response = speech_client.recognize(config=config, audio=audio)
    return response.results[0].alternatives[0].transcript

def text_translation(text, target_language):
    translation = translate_client.translate(text, target_language=target_language)
    return translation["translatedText"]

def text_to_speech(text, target_language):
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice_params = texttospeech.VoiceSelectionParams(
        language_code=target_language, name="ta-IN-Wavenet-D"
    )
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.LINEAR16)

    response = text_to_speech_client.synthesize_speech(
        input=synthesis_input, voice=voice_params, audio_config=audio_config
    )

    return response.audio_content

def send_emergency_alert():
    message = client.messages.create(
        body="Emergency! Patient needs immediate attention.",
        from_=TWILIO_PHONE_NUMBER,
        to=EMERGENCY_PHONE_NUMBER,
    )
    print("Emergency alert sent!")

# Example usage:
audio_file_path = "path/to/patient_audio.wav"
patient_speech = speech_to_text(audio_file_path)

# Translate patient's suggestion to English for analysis
english_text = text_translation(patient_speech, "en")

# Send emergency alert if needed
if "emergency" in english_text.lower():
    send_emergency_alert()

# Doctor's analysis (replace this with your analysis logic)
doctor_analysis = "The doctor's analysis goes here."

# Translate doctor's analysis back to Tamil
tamil_analysis = text_translation(doctor_analysis, "ta-IN")

# Convert the Tamil analysis to speech
tamil_audio_content = text_to_speech(tamil_analysis, "ta-IN")

# Save the Tamil audio to a file or play it
# (You may need additional libraries for audio handling)

# Example: Save the audio to a file
with open("path/to/tamil_analysis.wav", "wb") as audio_file:
    audio_file.write(tamil_audio_content)
"""

import speech_recognition as sr
from googletrans import Translator
import requests
import winsound

# Replace with your own API key
google_speech_recognition_api_key = 'YOUR_GOOGLE_SPEECH_RECOGNITION_API_KEY'
google_translation_api_key = 'YOUR_GOOGLE_TRANSLATION_API_KEY'
emergency_alert_url = 'YOUR_EMERGENCY_ALERT_API_URL'

def get_microphone():
    mic = sr.Microphone()
    try:
        with mic as source:
            print("Microphone initialized.")
        return mic
    except sr.RequestError as e:
        print(f"Error accessing microphone: {e}")
        return None
    except sr.UnknownValueError:
        print("Microphone is not available.")
        return None

def speech_to_text(mic):
    recognizer = sr.Recognizer()

    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=10)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, key=google_speech_recognition_api_key)
        print("Text: ", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Error connecting to Google Speech Recognition service: {e}")
        return None

def translate_text(text, target_language='en'):
    translator = Translator(service_urls=['translate.googleapis.com'])
    translated_text = translator.translate(text, dest=target_language).text
    print(f"Translated Text: {translated_text}")
    return translated_text

def send_emergency_alert(message):
    payload = {'message': message}
    response = requests.post(emergency_alert_url, data=payload)
    print(f"Emergency Alert Sent. Response: {response.text}")

def text_to_speech(text, target_language='ta-IN'):
    translator = Translator(service_urls=['translate.googleapis.com'])
    translated_text = translator.translate(text, dest=target_language).text
    print(f"Tamil Text: {translated_text}")
    winsound.SND_FILENAME
    winsound.PlaySound(translated_text, winsound.SND_FILENAME)

# Main function
def main():
    # Step 1: Get Microphone
    mic = get_microphone()

    if mic:
        # Step 2: Speech to Text
        patient_text = speech_to_text(mic)

        if patient_text:
            # Step 3: Translate Patient's Text
            translated_text = translate_text(patient_text)

            # Step 4: Send Emergency Alert
            send_emergency_alert(translated_text)

            # Step 5: Doctor's Analysis and Response (Hardcoded for example)
            doctor_response = "Doctor's response in English"

            # Step 6: Translate Doctor's Response back to Patient's Language
            translated_response = translate_text(doctor_response, target_language='ta-IN')

            # Step 7: Text to Speech for Patient
            text_to_speech(translated_response, target_language='ta-IN')

if __name__ == "__main__":
    main()
