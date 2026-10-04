import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_article(article_text, error=None):
    prompt = f"""
        Analyze this article:

        Return JSON with exactly these fields:

        - title
        - summary
        - sentiment

        Sentiment must be one of:
        positive
        negative
        neutral

        Article:
        {article_text}
    """
    
    if error:
        prompt += f"""

            Your previous response was invalid.

            The validation error was:

            {error}

            Please correct your response and return valid JSON.
        """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text
