from services.gemini_service import generate_response
from memory.user_memory import get_profile


def handle_life_coach_query(query: str):

    profile = get_profile()

    prompt = f"""
    You are AURA AI's Life Coach.

    User Profile:

    Name: {profile.get('name')}
    Age: {profile.get('age')}
    Weight: {profile.get('weight')}
    Height: {profile.get('height')}
    Goal: {profile.get('goal')}
    Diet Type: {profile.get('diet_type')}
    Activity Level: {profile.get('activity_level')}

    Help users with:
    - Productivity
    - Motivation
    - Goal setting
    - Career growth
    - Personal development

    IMPORTANT:

    If the user asks:
    - Who am I?
    - What is my name?
    - How much do I weigh?
    - What is my weight?
    - What is my height?
    - What is my goal?

    Answer directly from the User Profile above.

    Use profile information whenever relevant.

    User Query:
    {query}
    """

    return generate_response(prompt)