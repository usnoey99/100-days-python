# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
def find_winner(bidding_dic):
    max = 0
    winner = ""

    # Compares the highest bid
    for bidder in auction_dic:
        if auction_dic[bidder] > max:
            max = auction_dic[bidder]
            winner = bidder

    print("\n" * 3)
    print(f"The winner is <{winner}> with a bid of ${auction_dic[winner]}.")
    print("\n" * 3)


from art import logo

print("\n" * 3)
print(logo)

auction_dic = {}

while 1:
    bidder_name = input("What is your name?: ")
    bid_amount = int(input ("What is your bid?: $")) # Don't forget to change the type!

    auction_dic[bidder_name] = bid_amount


    another_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    print("\n" * 3)
    if another_bidder == "yes":
        continue
    else: # another_bidder == "no"
        find_winner(auction_dic)
        break

