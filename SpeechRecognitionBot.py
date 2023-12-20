
#1
'''
import vosk
import pyaudiowpatch as pyaudio
import queue
import deepl
import soundfile as sf
import io
import numpy as np
from scipy.io.wavfile import write
secret = "<your_deepl_api_key>"

translator = deepl.Translator(secret)

DURATION = 5.0
CHUNK_SIZE = 8000

vosk_model = vosk.Model(model_name="vosk-model-ja-0.22")

q = queue.Queue()

def convert_bytearray_to_wav_ndarray(input_bytearray: bytes, sampling_rate=16000):
    """
    Convert a bytearray to wav format to output in a file for quality check debuging
    """
    bytes_wav = bytes()
    byte_io = io.BytesIO(bytes_wav)
    write(byte_io, sampling_rate, np.frombuffer(input_bytearray, dtype=np.int16))
    output_wav = byte_io.read()
    output, _ = sf.read(io.BytesIO(output_wav))
    return output

if __name__ == "__main__":
    with pyaudio.PyAudio() as p:
        try:
            # Get default WASAPI info
            wasapi_info = p.get_host_api_info_by_type(pyaudio.paWASAPI)
        except OSError:
            print("Looks like WASAPI is not available on the system. Exiting...")
            exit()
        
        # Get default WASAPI speakers
        default_speakers = p.get_device_info_by_index(wasapi_info["defaultOutputDevice"])
        
        if not default_speakers["isLoopbackDevice"]:
            for loopback in p.get_loopback_device_info_generator():
                if default_speakers["name"] in loopback["name"]:
                    default_speakers = loopback
                    break
            else:
                print("Default loopback output device not found.\n\nRun `python -m pyaudiowpatch` to check available devices.\nExiting...\n")
                exit()
                
        print(f"Recording from: ({default_speakers['index']}){default_speakers['name']}")
        
        def callback(in_data, frame_count, time_info, status):
            """Write frames and return PA flag"""
            # wave_file.writeframes(in_data)
            if status:
                print(status, file="log.txt")
            q.put(bytes(in_data))
            return (in_data, pyaudio.paContinue)
        
        with p.open(format=pyaudio.paInt16,
                channels=1,
                rate=int(default_speakers["defaultSampleRate"]),
                frames_per_buffer=8000,
                input=True,
                input_device_index=default_speakers["index"],
                stream_callback=callback
        ) as stream:
            rec = vosk.KaldiRecognizer(vosk_model, int(default_speakers["defaultSampleRate"]))
            full_recording = bytearray()
            while True:
                data = q.get()

                full_recording.extend(data)
                # print(data)
                if len(data) > int(int(default_speakers["defaultSampleRate"])/4):
                    if rec.AcceptWaveform(data):
                        transcript = rec.Result()[14:-3]
                        if len(transcript) > 0:
                            print(translator.translate_text(transcript, source_lang="JA", target_lang="EN-US"))

'''
