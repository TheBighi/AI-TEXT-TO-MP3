from gtts import gTTS
import subprocess
import os
from groq import Groq

apikey = "APIKEY HERE"

# converastion list for continuous chat
conversation_history = []
counter = 1

while True:
    question = input("What would you like to ask GROQ: ")
    if question.lower() in ["exit", "quit", "stop"]:
        print("Goodbye!")
        break
    
    client = Groq(api_key=apikey)
    
    # append history
    conversation_history.append({"role": "user", "content": question})
    
    chat_completion = client.chat.completions.create(
        messages=conversation_history,
        model="llama3-8b-8192",  # might wanna update model if its old
    )
    
    response = chat_completion.choices[0].message.content
    
    #append to converstion history
    conversation_history.append({"role": "assistant", "content": response})
    
    # filepath HERE
    file_path = f"{counter}audio.mp3" 
    counter += 1
    
    tts = gTTS(response)
    tts.save(file_path)
    
    print(f"Audio saved as {file_path}")
    os.startfile(file_path)
    
    print(f"\033[96m{response}\033[0m")  # cyan cause cool
