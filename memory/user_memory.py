import json
import os

FILE_PATH = "data/users/user_profile.json"


def load_profile():

    if not os.path.exists(FILE_PATH):

        default_profile = {
            "name": None,
            "age": None,
            "weight": None,
            "height": None,
            "goal": None,
            "diet_type": None,
            "activity_level": None
        }

        os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

        with open(FILE_PATH, "w") as file:
            json.dump(default_profile, file, indent=4)

        return default_profile

    with open(FILE_PATH, "r") as file:
        return json.load(file)


def save_profile(profile):

    with open(FILE_PATH, "w") as file:
        json.dump(profile, file, indent=4)


# -------------------
# NAME
# -------------------

def save_name(name):
    profile = load_profile()
    profile["name"] = name
    save_profile(profile)


def get_name():
    return load_profile()["name"]


# -------------------
# AGE
# -------------------

def save_age(age):
    profile = load_profile()
    profile["age"] = age
    save_profile(profile)


def get_age():
    return load_profile()["age"]


# -------------------
# WEIGHT
# -------------------

def save_weight(weight):
    profile = load_profile()
    profile["weight"] = weight
    save_profile(profile)


def get_weight():
    return load_profile()["weight"]


# -------------------
# HEIGHT
# -------------------

def save_height(height):
    profile = load_profile()
    profile["height"] = height
    save_profile(profile)


def get_height():
    return load_profile()["height"]


# -------------------
# GOAL
# -------------------

def save_goal(goal):
    profile = load_profile()
    profile["goal"] = goal
    save_profile(profile)


def get_goal():
    return load_profile()["goal"]


# -------------------
# DIET TYPE
# -------------------

def save_diet_type(diet):
    profile = load_profile()
    profile["diet_type"] = diet
    save_profile(profile)


def get_diet_type():
    return load_profile()["diet_type"]


# -------------------
# ACTIVITY LEVEL
# -------------------

def save_activity_level(activity):
    profile = load_profile()
    profile["activity_level"] = activity
    save_profile(profile)


def get_activity_level():
    return load_profile()["activity_level"]


# -------------------
# FULL PROFILE
# -------------------

def get_profile():
    return load_profile()