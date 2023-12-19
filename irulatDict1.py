import json
import tkinter as tk
import speech_recognition as sr

def load_dictionary(file_path):
    with open(file_path, 'r') as json_file:
        english_dictionary = json.load(json_file)
    return english_dictionary

def lookup_meanings(word):
    if word in english_dictionary:
        return english_dictionary[word]
    else:
        return ["Meaning not found"]

def process_text():
    input_text = entry.get()
    meanings = lookup_meanings(input_text)
    output_label.config(text=", ".join(meanings))

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        input_text = recognizer.recognize_google(audio)
        entry.delete(0, tk.END)
        entry.insert(0, input_text)
        process_text()
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Error with the speech recognition service: {e}")

# Load the dictionary from the JSON file
english_dictionary = load_dictionary('english_dictionary.json')

# Create the GUI
root = tk.Tk()
root.title("Word Meaning Lookup")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry_label = tk.Label(frame, text="Enter a word:")
entry_label.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(frame, width=20)
entry.grid(row=0, column=1, padx=5, pady=5)

search_button = tk.Button(frame, text="Search", command=process_text)
search_button.grid(row=0, column=2, padx=5, pady=5)

output_label = tk.Label(frame, text="")
output_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

#speech_button = tk.Button(frame, text="Speech Recognition", command=recognize_speech)
#speech_button.grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
