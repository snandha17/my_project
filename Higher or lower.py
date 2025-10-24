import random
from game_data import data
from art import vs,logo


def choices(value_insert):
    """Choice a ramdom data in game data"""
    selected_value = random.choice(value_insert)
    return selected_value

def formate(datas):
    """Make the data in correct formate to print"""
    return f"{datas["name"]},{datas['description']},{datas['country']}."

def follows(datas):
    """Fetch follower count to compare"""
    return datas['follower_count']

first_data = choices(data)
formate(first_data)
compare_A = follows(first_data)
second_data = choices(data)
formate(second_data)
compare_B = follows(second_data)

loss = False
score = 0
while not loss:
    print(logo)
    print(f"compare A: {formate(first_data)}")
    print(vs)
    print(f"compare B: {formate(second_data)}")

    user_value = input("Who has more followers? Type 'A' or 'B':").lower()

    if first_data == second_data:
        loss = False
    elif compare_A > compare_B:
        if user_value == 'a':
            score += 1
            print(f"You won,Score is {score}")
            second_data = choices(data)
            compare_B = follows(second_data)
        else:
            print(f"You loss,Score is {score}")
            loss = True
    elif compare_B > compare_A:
        if user_value == 'b':
            score += 1
            print(f"you won,Score is {score}")
            first_data = choices(data)
            compare_A = follows(first_data)
        else:
            print(f"You loss,Score is {score}")
            loss = True
