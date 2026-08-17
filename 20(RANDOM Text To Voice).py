from gtts import gTTS           # install gtts in python but need to first install python itself

text = "Hello"
tts = gTTS(text=text, lang = "en")

tts.save("voice.mp3")
print("Audio Saved Successfully")