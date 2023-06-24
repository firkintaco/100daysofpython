from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface
def get_questions() -> list:
    url = "https://opentdb.com/api.php?amount=20&category=18&type=boolean"
    response = requests.get(url)
    data = response.json()["results"]
    return data

question_bank = [Question(question["question"], question["correct_answer"]) for question in get_questions()]


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

