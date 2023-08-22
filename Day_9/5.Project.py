from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    # bidding_record is the dictionary i.e bid
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your Name?\n")
    bid_price = input("What is your bid price? \n$")
    # add the inputs to a dictionary
    bids[name] = bid_price
    # print(bids)
    # code to end the loop
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'?\n").lower
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        
        
    




 

