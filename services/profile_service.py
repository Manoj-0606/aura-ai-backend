# services/profile_service.py

import json

PROFILE_PATH = "data/users/user_profile.json"


def get_profile():

    with open(PROFILE_PATH, "r") as f:
        return json.load(f)