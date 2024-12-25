# Quiz-App
A simple Django-based web application for a multiple-choice quiz. Features include starting a new quiz session, fetching random questions from the database, submitting answers, and tracking results with details on correct and incorrect responses.

#Overview

This is a simple Django web application for a Quiz App. It allows a user to:
1. Start a new quiz session.
2. Get a random multiple-choice question from a set of questions in the database.
3. Submit an answer to the question.
4.View the total number of questions answered, along with details about correct and incorrect submissions.

#Features

1.Backend built using Django framework.
2. Random question selection.
3. Tracking of correct and incorrect answers.
4. Session management to maintain user progress.


#Installation

1. Clone the repository:
git clone <repository-url>
cd quiz-app-django

2. Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the required packages:
pip install -r requirements.txt

4. Run migrations to set up the database:
python manage.py makemigrations
python manage.py migrate

5. Create sample questions (optional):
python manage.py shell

from app.models import Question
Question.objects.create(
    text="What is the capital of France?",
    option_a="Paris",
    option_b="London",
    option_c="Berlin",
    option_d="Madrid",
    correct_option="A"
)
Question.objects.create(
    text="What is 2 + 2?",
    option_a="3",
    option_b="4",
    option_c="5",
    option_d="6",
    correct_option="B"
)
exit()

6. Run the development server:
python manage.py runserver
Access the app at http://127.0.0.1:8000/.

