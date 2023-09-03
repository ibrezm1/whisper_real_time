import speech_recognition as sr

# Initialize the recognizer
# Follow
# https://github.com/AssemblyAI/youtube-tutorials/tree/main/raspberry-pi-speech-recognition
# https://www.youtube.com/watch?v=vEMzN5RgXbw
recognizer = sr.Recognizer()

# Use a try-except block for error handling
try:
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

    # Use Google Web Speech API to transcribe the audio
    transcribed_text = recognizer.recognize_google(audio)
    print("You said:", transcribed_text)

except sr.UnknownValueError:
    print("Sorry, I couldn't understand what you said.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")
