from services.gemini_service import generate_response
from memory.user_memory import get_profile


def handle_diet_query(query: str):

    profile = get_profile()

    prompt = f"""
    You are AURA AI's Diet & Nutrition Expert.

    User Profile:

    Name: {profile.get('name')}
    Age: {profile.get('age')}
    Weight: {profile.get('weight')}
    Height: {profile.get('height')}
    Goal: {profile.get('goal')}
    Diet Type: {profile.get('diet_type')}
    Activity Level: {profile.get('activity_level')}

    Create a highly personalized diet plan and nutrition recommendations.

    Focus on:
    - Healthy eating
    - Weight management
    - Nutritional balance
    - Sustainable habits
    - Protein requirements
    - Calorie awareness

    Use the user's profile whenever possible.

    User Query:
    {query}
    """

    return generate_response(prompt)