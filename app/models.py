from pydantic import BaseModel, Field, field_validator
import re

# Задание 1.4
class User(BaseModel):
    name: str
    id: int

# Задание 1.5
class UserWithAge(BaseModel):
    name: str
    age: int

# Задание 2.1
class Feedback(BaseModel):
    name: str
    message: str

# Задание 2.2
class FeedbackValidated(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)

    @field_validator('message')
    @classmethod
    def validate_message(cls, v: str) -> str:
        bad_words = ["кринж", "рофл", "вайб"]
        message_lower = v.lower()

        for word in bad_words:
            pattern = r'\b' + re.escape(word) + r'(а|у|ом|е|ов)?\b'
            if re.search(pattern, message_lower, re.IGNORECASE):
                raise ValueError('Использование недопустимых слов')
        return v
