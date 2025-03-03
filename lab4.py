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

        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        
        # Player answer
        try:
            user_choice = int(input("Your answer (enter number): "))
            # Check player answer
            if options[user_choice - 1] == question_data["correct_answer"]:
                print(" Correct!")
                score += 1
            else:
                print(f" Wrong! The correct answer was: {question_data['correct_answer']}")
        except (ValueError, IndexError):
            print(" Invalid input. Skipping this question.")  

    
    print(f"\nGame Over! Your final score: {score}/{len(questions)}")

if __name__ == "__main__":
    trivia_game()
