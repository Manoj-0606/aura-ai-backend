import json

FILE_PATH = "data/users/progress.json"


def load_progress():

    with open(FILE_PATH, "r") as file:
        return json.load(file)


def save_progress(data):

    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


def add_workout():

    data = load_progress()

    data["workouts_completed"] += 1

    save_progress(data)

    return data["workouts_completed"]


def get_workouts():

    data = load_progress()

    return data["workouts_completed"]