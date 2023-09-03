import openai
import pyttsx3


# Initialize the text-to-speech engine
engine = pyttsx3.init()


def get_completion(messages, model="gpt-3.5-turbo"):
    #messages = [{"role": "user", "content": prompt}]
    print(messages)
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=50,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


# Function for speaking a text
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Function for getting a response from ChatGPT for a given text
# https://openai.com/blog/function-calling-and-other-api-updates
# Add Function caling for skills

def check_for_wake_word(text):
    if "jarvis" in text.lower():
        return True
    return False

