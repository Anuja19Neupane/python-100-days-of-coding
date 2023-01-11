
# boli lagako jasto ho. we should check who is going to invest greatest amount
# and declare them winner.
print("WELCOME TO SECRET AUCTION.")
# create a empty dictionary
bids = {}
bidding_fininshed = False
# aru biders baaki xa ki xaina vanera sodhda yes answer aayo vaney we should
# repeat this process.for this we need loop


def find_highest_bider(bidding_record):
    # to find highest bidder
    highest_bid = 0
    winner = ""
    # bidding_record={"anuja":234,"prashu":675}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}.  ")


while not bidding_fininshed:
    name = print(input("What is your name? "))
    price = print(int(input("How many bids would you like to apply? ")))
    bids[name] = price
    any_other = print(input("Are there any other bidders? type yes or no: "))
    if any_other == "no":
        bidding_fininshed = True
        find_highest_bider(bids)  # function call
    else:
        bidding_fininshed = False
