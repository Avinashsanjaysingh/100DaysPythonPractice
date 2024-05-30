
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


levelText = "There are 17 levels of the game \n\nlevel 1: 1,000 \nlevel 2: 2,000 \nlevel 3: 3,000 \nlevel 4: 5,000 \nlevel 5: 10,000 \nlevel 6: 20,000 \nlevel 7: 40,000 \nlevel 8: 80,000 \nlevel 9: 1,60,000 \nlevel 10: 3,20,000 \nlevel 11: 6,40,000 \nlevel 12: 12,50,000 \nlevel 13: 25,00,000 \nlevel 14: 50,00,000 \nlevel 15: 75,00,000 \nlevel 16: 1 Crore \nlevel 17: 7.5 Crore"

welcome = input("\nWelcome to Kon Banega Crorepati !\n(press Enter to start the game)")
level = (input(f"{levelText} \n\nPlease select your intelligence level between 10-17: "))

while (level) not in ['10','11','12','13','14','15','16','17']:
    level = (input("Please select the level between 10-17: "))

level = int(level)

for i in range(len(questions)):

    question = questions[i]

    print(f"\nQustion no. {i+1} for the amount of {amount[i]}\n")
    print(f"{question[0]}\na. {question[1]}\tb. {question[2]}\nc. {question[3]}\td. {question[4]}\n")

    answer = input("Enter your answer (a, b, c, d) or 'q' to quit.\n")
    # while not (answer == 'a' or answer == 'b' or answer == 'c' or answer == 'd' or answer == 'q'):
    #     answer = input("Please enter only from the given options \nEnter your answer (a, b, c, d) or 'q' to quit.\n")
    while answer not in ['a','b','c','d','q']:
        answer = input("Please enter only from the given options \nEnter your answer (a, b, c, d) or 'q' to quit.\n")

    if answer == question[-1]:
        print(f"\nCorrect answer. \nYou win {amount[i]}")
    elif answer == 'q':
        if (i <= level):
            print(f"\nYou win nothing.")
        elif i >= 10:
            print(f"You win {amount[i-1]}")
        break
    else:
        if (i <= level):
            print("Wrong answer! \nYou win nothing")
        if i >= level:
            print(f"You win {amount[level]}")
            break
        break



