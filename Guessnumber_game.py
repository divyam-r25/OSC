import random


def choose_difficulty():
  
    while True:
        difficulty = input("Enter your difficulty\n1 for Easy\n2 for Medium\n3 for Hard\n>>>")
        if not difficulty.isdigit():
            print("Invalid input,Plz select 1,2,3 only")
            continue
        difficulty = int(difficulty)

        if difficulty not in [1,2,3]:
            print("Invalid input,Plz select 1,2,3 only")
            continue

        if difficulty == 1:
            a = -1
            r = random.randint(1,100)
            while(a != r):
                a = input("Guess a number bteween 1 to 100:")
                if not a.isdigit():
                    print("Invalid input")
                    continue

                if int(a) > r:
                    print("wrong ans! Try a lower number")
                elif int(a) < r:
                    print("wrong ans! Try a higher number")
                else:
                    print("Right answer!")
                    break
        elif difficulty == 2:
            r = random.randint(1,200)
            a = -1
            while(a != r):
                a = input("Guess a number between 1 to 200:")
                if not a.isdigit():
                    print("Invalid input")
                    continue

                if int(a) > r:
                    print("wrong ans! Try a lower number")
                elif int(a) < r:
                    print("wrong ans! Try a higher number")
                else:
                    print("Right answer!")
                    break

        elif difficulty == 3:
            r = random.randint(1,300)
            a = -1
            while(a != r):
                a = input("Guess a number between 1 to 300:")
                if not a.isdigit():
                    print("Invalid input")
                    continue

                if int(a) > r:
                    print("wrong ans! Try a lower number")
                elif int(a) < r:
                    print("wrong ans! Try a higher number")
                else:
                    print("Right answer!")
                    break
            
        else:
            print("Invalid choices")
            break

choose_difficulty()

# Making it more intresting 