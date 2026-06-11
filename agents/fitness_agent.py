from services.gemini_service import generate_response
from memory.user_memory import get_profile


def handle_fitness_query(query: str):

    profile = get_profile()

    prompt = f"""
    You are AURA AI's Fitness Coach.

    User Profile:

    Name: {profile.get('name')}
    Age: {profile.get('age')}
    Weight: {profile.get('weight')}
    Height: {profile.get('height')}
    Goal: {profile.get('goal')}
    Diet Type: {profile.get('diet_type')}
    Activity Level: {profile.get('activity_level')}

    Create a highly personalized workout and fitness plan.

    Focus on:
    - Strength training
    - Fat loss
    - Muscle gain
    - Mobility
    - Recovery
    - Weekly workout planning

    Use the user's profile whenever possible.

    IMPORTANT:

    Keep responses concise and easy to read.

    Return the response EXACTLY in this format:

    🏋️ Goal
    <goal>

    📅 Weekly Plan

    Monday
    • Workout

    Tuesday
    • Workout

    Wednesday
    • Workout

    Thursday
    • Workout

    Friday
    • Workout

    Saturday
    • Workout

    Sunday
    • Workout

    ⏱ Workout Duration
    • xx minutes/day

    💡 Tips
    • Tip 1
    • Tip 2
    • Tip 3

    Rules:
    - Use bullet points
    - Use headings
    - No long paragraphs
    - No motivational speeches
    - No explanations unless asked
    - Maximum 120 words
    - Make the workout practical

    User Query:
    {query}
    """

    return generate_response(prompt)