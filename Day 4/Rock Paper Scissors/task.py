import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_paper_scissors = [rock,paper,scissors]
computer_choice = random.randint(0,2)
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

try:
    value = int(player_choice) / 2
    player_choice = int(player_choice)

    if player_choice == computer_choice:
        print(rock_paper_scissors[player_choice])
        print("Computer chose:")
        print(rock_paper_scissors[computer_choice])
        print("It's a draw.")
    elif player_choice == 0:
        print(rock_paper_scissors[player_choice])
        print("Computer chose:")
        print(rock_paper_scissors[computer_choice])
        if computer_choice == 1:
            print("You lose.")
        elif computer_choice == 2:
            print("You win!")
    elif player_choice == 1:
        print(rock_paper_scissors[player_choice])
        print("Computer chose:")
        print(rock_paper_scissors[computer_choice])
        if computer_choice == 2:
            print("You lose.")
        elif computer_choice == 0:
            print("You win!")
    elif player_choice == 2:
        print(rock_paper_scissors[player_choice])
        print("Computer chose:")
        print(rock_paper_scissors[computer_choice])
        if computer_choice == 0:
            print("You lose.")
        elif computer_choice == 1:
            print("You win!")
    else:
        print("You typed an invalid number, you lose!")

except:
    print("undefined")
    print("Computer chose:")
    print(rock_paper_scissors[computer_choice])







