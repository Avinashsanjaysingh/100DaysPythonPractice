
# Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game.


def KBC():

    pass


print("Welcome to the game kaun banega crorepati\n")

import random

# Define the questions and their corresponding answers using a list of tuples
questions = [
    ("What is the capital of France?", "Paris"),
    ("Who wrote 'Romeo and Juliet'?", "William Shakespeare"),
    ("What is the chemical symbol for water?", "H2O"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("What is the powerhouse of the cell?", "Mitochondria")
]

# Function to display a question and get user's answer
def ask_question(question, correct_answer):
    print(question)
    user_answer = input("Your answer: ")
    return user_answer.lower() == correct_answer.lower()

# Function to play the quiz game
def play_game():
    total_questions = len(questions)
    correct_answers = 0

    # Shuffle the questions to make the game more random
    random.shuffle(questions)

    # Loop through each question
    for i, (question, correct_answer) in enumerate(questions, 1):
        print(f"\nQuestion {i}/{total_questions}:")
        if ask_question(question, correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Sorry, the correct answer was {correct_answer}")

    # Calculate the amount won based on the number of correct answers
    prize_money = 1000 * correct_answers

    print(f"\nCongratulations! You answered {correct_answers} questions correctly.")
    print(f"You are taking home ${prize_money}.")

# Main function to start the program
def main():
    print("Welcome to the KBC quiz game!")
    play_game()

if __name__ == "__main__":
    main()

