# TODO-1: Ask the user for input
import art

def find_highest_value(dictionary):
    winner=""
    highest_value = 0
    for bid in dictionary:
        if  dictionary[bid] > highest_value:
            highest_value = dictionary[bid]
            winner = bid
    print(f"The winner is {winner}  with a bid of {highest_value}")

print(art.logo)
bid_again = False
Auction = {}
while not bid_again:
    User_name = input("What is your name: ")
    bid_value = int(input("What is your bid: $"))

    # TODO-2: Save data into dictionary {name: price}

    Auction[User_name] = bid_value

    # TODO-3: Whether if new bids need to be added

    discussion = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if discussion == "no":
        bid_again = True
        find_highest_value(dictionary=Auction)
    elif discussion == "yes":
        print("\n" * 50)
    else:
        print("please enter the correct spelling")
        bid_again = True

   # TODO-4: Compare bids in dictionary

# winner = max(Auction)
# max_value = max(Auction.values())
# print(f"The winner is {Auction}  with a bid of {max_value}")
