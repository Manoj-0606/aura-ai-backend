import json
import os

FILE_PATH = "data/conversations/chat_history.json"


def load_history():

    if not os.path.exists(FILE_PATH):

        with open(FILE_PATH, "w") as file:
            json.dump([], file)

        return []

    with open(FILE_PATH, "r") as file:
        return json.load(file)


def save_history(history):

    with open(FILE_PATH, "w") as file:
        json.dump(history, file, indent=4)


def add_message(role, message):

    history = load_history()

    history.append({
        "role": role,
        "message": message
    })

    save_history(history)


def get_history():

    return load_history()