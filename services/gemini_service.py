import google.generativeai as genai

from utils.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_response(prompt: str):

    system_prompt = f"""
    You are AURA AI, a Health & Life Companion.

    Return responses in clean readable text.

    Do NOT use markdown.
    Do NOT use asterisks.
    Do NOT use headings.
    Do NOT use bullet symbols like *, #, or -.

    Keep responses structured and easy to read.

    User Request:
    {prompt}
    """

    response = model.generate_content(system_prompt)

    return response.text