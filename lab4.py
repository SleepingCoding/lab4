import requests
import random

# Function to get trivia questions from OpenTDB
def fetch_trivia_questions(amount=10):
    url = f"https://opentdb.com/api.php?amount={amount}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data["results"]
    else:
        print("Error fetching trivia questions!")
        return []