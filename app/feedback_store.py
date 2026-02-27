# Задание 2.1 и 2.2
feedbacks: list[dict] = []

def add_feedback(name: str, message: str) -> dict:
    feedback = {"name": name, "message": message}
    feedbacks.append(feedback)
    return feedback
