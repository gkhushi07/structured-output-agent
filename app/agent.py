import json

from pydantic import ValidationError

from app.llm import generate_article
from app.models import Article


def process_article(article_text):
    max_retries = 3
    error = None
    for attempt in range(1, max_retries + 1):
        print(f"Attempt {attempt}")
        
        raw_response = generate_article(article_text, error)
        raw_response = raw_response.replace("```json", "").replace("```", "")
        

        try:
            article_data = json.loads(raw_response)
            article = Article.model_validate(article_data)

            print("Valid response received!")
            
            return article

        except (json.JSONDecodeError, ValidationError) as validation_error:
            print("LLM returned invalid data")
            print(validation_error)

            error = validation_error

    print("All attempts failed.")
    return None