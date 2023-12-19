import speech_recognition as sr
from gtts import gTTS
import os

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Patient, please speak in Tamil:")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ta-IN")
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
        return None
    except sr.RequestError as e:
        print(f"Error connecting to Google API: {e}")
        return None

def text_to_speech(text, lang="ta"):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("doctor_response.mp3")
    os.system("start doctor_response.mp3")  # Opens the file with the default audio player

def chat_with_doctor():
    print("Chatting with the doctor:")
    while True:
        patient_message = speech_to_text()

        if not patient_message:
            continue

        # Send the patient's message to the doctor (you can replace this with your alert mechanism)
        doctor_response = "Doctor responds to the patient's message in English."

        print("Doctor:", doctor_response)
        text_to_speech(doctor_response)

        # Here, you can send the doctor's response to the patient, or handle it as needed.

        # For simplicity, let's assume the conversation ends after one round.
        break

if __name__ == "__main__":
    chat_with_doctor()
