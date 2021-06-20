from playsound import playsound

from gtts import gTTS
def playaudio(audio):
    playsound(audio)
def convert_to_audio(text):
    audio = gTTS(text)
    audio.save("textaudio.mp3")
    playaudio("textaudio.mp3")
convert_to_audio("hello! your're viewing Shreya's project! hope you like this small project of text to speech")
