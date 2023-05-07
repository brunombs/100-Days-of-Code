from art import logo
players_and_bid = {}
game_on = True
print(logo)
# Add names and bids.
while game_on == True:
    name = str(input("What is the name of the bidder?\n"))
    bid = float(input("What is the bid? R$"))
    players_and_bid[name.capitalize()] = bid
    stop = str(input("Are there any other bidders? Type 'YES' or 'NO'\n"))
    if stop == "no":
        game_on = False

# Find the highest bid
def find_highest_bid():
    highest_bid = 0
    winner = ''
    total = len(players_and_bid)
    for bid in players_and_bid:
        bid_amount = players_and_bid[bid]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bid
    print(f'The winner is {winner} with a bid of R${highest_bid:.2f}')
    if total == 1:
        print(f'{total} is the total amount of bid')
    else:
        print(f'{total} is the total amount of bids')


find_highest_bid()