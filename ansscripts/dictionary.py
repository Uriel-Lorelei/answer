import requests
import json
import subprocess

word = input("Word --> ")

if word == "":
    print("TRY AGAIN")
else:
    base_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(base_url)

    data = response.json()

    # try:
    #     print("-----------------------------------------")
    #     print(f"Word: {data[0]['word']}\nPart of Speech: {data[0]['meanings'][0]['partOfSpeech']}\nDefinition: {data[0]['meanings'][0]['definitions'][0]['definition']}")
    #     print("-----------------------------------------")
    # except KeyError:
    #     print("Word not found.")
    #     print("-----------------------------------------")

    try:
        meaning = f"Definition: {data[0]['meanings'][0]['definitions'][0]['definition']}"
        subprocess.run(["notify-send", meaning])
    except KeyError:
        subprocess.run(["notify-send", "Word not found"])