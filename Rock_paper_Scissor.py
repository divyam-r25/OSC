import random

print("Rock Paper Scissors")


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


n = input("Enter your choice (r for rock, p for paper, s for scissors): ").lower()


choice = {"r": 0, "p": 1, "s": 2}  
choice_names = ["rock", "paper", "scissors"]
choice_sign= [rock, paper, scissors]

if n not in choice:
    print("Invalid input! Please enter 'r', 'p', or 's'.")
    exit()


user_choice = choice[n]
computer_choice = random.randint(0, 2)  


print(f"\nYou chose {choice_names[user_choice]}:")
print(choice_sign[user_choice])

print(f"Computer chose {choice_names[computer_choice]}:")
print(choice_sign[computer_choice])


if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice - computer_choice) % 3 == 1:
    print("You win!")
    print("Congrats! 🎉")
else:
    print("You lost!")
    print("Better luck next time! 😅")
