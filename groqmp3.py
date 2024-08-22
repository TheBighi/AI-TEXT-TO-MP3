from gtts import gTTS
import subprocess
import os
from groq import Groq

apikey = "API_KEY_HERE"

question = input("What would you like to ask GROQ: ")

client = Groq(
    api_key=apikey,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": question,
        }
    ],
    model="llama3-8b-8192", #model version might need to be changed depending on when u are seeing this
)

response = chat_completion.choices[0].message.content

tts = gTTS(response)

file_path = (f'YOUR DESIRED FILE PATH')
tts.save(file_path)

print(f"Audio saved as file.mp3")

os.startfile(file_path)

print(f"\033[96m{response}\033[0m") #i made it cyan cause cool
