from services.gemini_service import generate_response


def handle_health_query(query: str):

    prompt = f"""
    You are AURA AI's Health Assistant.

    Provide educational health information.

    Never diagnose diseases.
    Never claim certainty.
    Recommend professional medical help when needed.

    User Query:
    {query}
    """

    return generate_response(prompt)