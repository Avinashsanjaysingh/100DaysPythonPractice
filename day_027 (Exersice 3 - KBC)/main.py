# Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game.

questions = [
  ["Which language was used to create fb ?", "Python", "French", "JavaScript", "Php", "d"],
  ["Which language was used to create fb ?", "Python", "French", "JavaScript", "Php", "d"],
  ["Which language was used to create fb ?", "Python", "French", "JavaScript", "Php", "d"],
  ["Which language was used to create fb ?", "Python", "French", "JavaScript", "Php", "d"],
  ["Which language was used to create fb ?", "Python", "French", "JavaScript", "Php", "d"],
  ["Which language was used to create fb ?", "Python", "French", "JavaScript", "Php", "d"],
  ["Which language was used to create fb ?", "Python", "French", "JavaScript", "Php", "d"],
  ["Which language was used to create fb ?", "Python", "French", "JavaScript", "Php", "d"],
  ["Which language was used to create fb ?", "Python", "French", "JavaScript", "Php", "d"],
  ["Which language was used to create fb ?", "Python", "French", "JavaScript", "Php", "d"],
  ["Which language was used to create fb ?", "Python", "French", "JavaScript", "Php", "d"],
  ["Which language was used to create fb ?", "Python", "French", "JavaScript", "Php", "d"],
  ["Which language was used to create fb ?", "Python", "French", "JavaScript", "Php", "d"],
  ["Which language was used to create fb ?", "Python", "French", "JavaScript", "Php", "d"],
  ["Which language was used to create fb ?", "Python", "French", "JavaScript", "Php", "d"],
  ["Which language was used to create fb ?", "Python", "French", "JavaScript", "Php", "d"],
  ["Which language was used to create fb ?", "Python", "French", "JavaScript", "Php", "d"],
]

amount = ['1,000', '2,000', '3,000', '5,000', '10,000', '20,000', '40,000', '80,000', '1,60,000', '3,20,000', '6,40,000', '12,50,000', '25,00,000', '50,00,000', '75,00,000', '1 Crore', '7.5 Crore']

welcome = input("\nWelcome to Kon Banega Crorepati !\n(press Enter to start the game)")

for i in range(len(questions)):

    question = questions[i]

    print(f"\nQustion no. {i+1} for the amount of {amount[i]}\n")
    print(f"{question[0]}\na. {question[1]}\tb. {question[2]}\nc. {question[3]}\td. {question[4]}\n")

    answer = input("Enter your answer (a, b, c, d) or 'q' to quit.\n")
    while not (answer == 'a' or answer == 'b' or answer == 'c' or answer == 'd' or answer == 'q'):
        answer = input("Please enter only from the given options \nEnter your answer (a, b, c, d) or 'q' to quit.\n")

    if answer == question[-1]:
        print(f"\nCorrect answer. \nYou win {amount[i]}")
    elif answer == 'q':
        print(f"\nYou win {amount[i-1]}")
        break
    else:
        print("Wrong answer! \nYou win nothing")
        break
