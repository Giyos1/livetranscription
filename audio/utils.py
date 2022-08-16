import speech_recognition as sr

recognizer = sr.Recognizer()


def get_audio(audio):
    with sr.AudioFile(audio) as audios:
        listening = recognizer.listen(audios)
        text = recognizer.recognize_google(listening, language="uz-UZ")
    return text
