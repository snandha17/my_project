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
# arrange the values in list
rps = [rock,paper,scissors]
# create a user input space
user_value = int(input("Enter the value like 0 Rock ,1 paper ,2 scissors \n"))
if user_value < 0 or user_value > 2:
    print("YOu enter a invalid number. Game Over. You lose")
else:
    uv=[]
    if user_value == 0:
        uv.append(rps[0])
        print(rock)
        print("Rock")
    elif user_value == 1:
        uv.append(rps[1])
        print(paper)
        print("paper")
    else:
        uv.append(rps[2])
        print(scissors)
        print("scissors")
# create a random output for the computer
    cg = random.choice(rps)
    print(cg)
    co = list()
    co.append(cg)
    if uv[0] == rock and co[0] == scissors :
        print("You win")
    elif uv[0] ==paper and co[0] == scissors:
        print("You lose")
    elif uv[0] == rock and co[0] == paper:
        print("You lose")
    elif uv[0] == paper and co[0] == rock:
        print("You win")
    elif uv[0] == scissors and co[0] == rock:
        print("You lose")
    elif uv[0] == scissors and co[0] == paper :
        print("You win")
    else:
        print("Draw")

# other ways

user_value1 = int(input("Enter the value like 0 Rock ,1 paper ,2 scissors \n"))
if user_value1 < 0 or user_value1 > 2:
    print("YOu enter a invalid number. Game Over. You lose")
print(rps[user_value1])
computer_choice = random.randint(0,2)
print("Computer choice:")
print(rps[computer_choice])

if user_value1 == computer_choice:
    print("Draw")
elif computer_choice == 2 and user_value1 == 0:
    print("You win")
elif computer_choice < user_value1:
    print("You loss")
elif user_value1 < computer_choice:
    print("You win")
elif user_value1 == 0 and computer_choice == 2:
    print("You loss")




