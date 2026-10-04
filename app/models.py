from enum import Enum
from pydantic import BaseModel


class Sentiment(str, Enum):
    POSITIVE = "positive"
    # NEGATIVE = "negative"
    NEUTRAL = "neutral"


class Article(BaseModel):
    title: str
    summary: str
    sentiment: Sentiment
