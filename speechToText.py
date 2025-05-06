# DOCS: https://pypi.org/project/SpeechRecognition/
# pip install SpeechRecognition SpeechRecognition[whisper-local]

import speech_recognition as sr
audio_file_path = r"C:\Users\ihadjimpalasis\Desktop\Learning\VoiceDubbing\audio.wav"

r = sr.Recognizer()
with sr.AudioFile(audio_file_path) as src:
    audio = r.record(src)

text = r.recognize_whisper(audio)
print(text)


