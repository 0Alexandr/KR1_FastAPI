from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from pydantic import BaseModel

from app.models import User, UserWithAge, Feedback, FeedbackValidated
from app.feedback_store import add_feedback

# Создаем приложение FastAPI
app = FastAPI()

# Задание 1.1
@app.get("/")
async def root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}

# Задание 1.2
@app.get("/html", response_class=HTMLResponse)
async def read_html():
    return FileResponse("static/index.html")

# Задание 1.3
class CalculateRequest(BaseModel):
    num1: float
    num2: float

@app.post("/calculate")
async def calculate(request: CalculateRequest):
    return {"result": request.num1 + request.num2}

# Задание 1.4
current_user = User(name="Александр Краснопольский", id=1)

@app.get("/users")
async def get_users():
    return current_user

# Задание 1.5
@app.post("/user")
async def check_adult(user: UserWithAge):
    is_adult = user.age >= 18

    return {"name": user.name, "age": user.age, "is_adult": is_adult}

# Задание 2.1
@app.post("/feedback")
async def submit_feedback(feedback: Feedback):
    add_feedback(feedback.name, feedback.message)

    return {"message": f"Feedback received. Thank you, {feedback.name}."}

# Задание 2.2
@app.post("/feedback/validated")
async def submit_validated_feedback(feedback: FeedbackValidated):
    add_feedback(feedback.name, feedback.message)

    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}
