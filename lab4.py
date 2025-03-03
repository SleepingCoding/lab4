import requests
import random

# Function to get trivia questions 
def fetch_trivia_questions(amount=10):
    url = f"https://opentdb.com/api.php?amount={amount}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data["results"]
    else:
        print("Error fetching trivia questions!")
        return []

def trivia_game():
    questions = fetch_trivia_questions()
    
    if not questions:
        return
    
    score = 0
    
    for i, question_data in enumerate(questions):
        print(f"\nQuestion {i+1}: {question_data['question']}")
        
        options = question_data["incorrect_answers"] + [question_data["correct_answer"]]
        random.shuffle(options)