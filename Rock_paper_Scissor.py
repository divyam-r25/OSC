import random
print("Rock Paper Scissor")
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
computer = random.randint(1,3)
rock=3
paper=1
scissor=2
n = input("enter ur choice (r for rock, p for paper, s for scissors): ").lower()
youDict = {"s": 1, "p": -1, "r": 0}
reverseDict = {1: "s", -1: "p", 0: "r"}
if n not in youDict:
    print("Invalid input! Please enter 'r', 'p', or 's'.")
    exit()
you = youDict[n]

print(f"you choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")
if (computer == -1 and you == 1):
    print("you win")
    print("congrats!")
elif (computer == -1 and you == 0):
    print("you lost")
elif (computer == 0 and you == -1):
    print("you win")
    print("congrats!")
elif (computer == 0 and you == 1):
    print("you lost")
elif (computer == 1 and you == 0):
    print("you win")
    print("congrats!")
elif (computer == 1 and you == -1):
    print("you lost")

else:
    print("draw!")