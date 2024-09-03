from art import logo
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
print(logo)
end_bid = False
bid_info = {}
while not end_bid:
  name = input("Enter name of the bidder: \n")
  bid = int(input("Enter the bid: \n"))
  bid_info[name] = bid
  repeat = input("type 'yes' if others want to bid else type 'no': \n")
  if repeat == "no":
    list_info = bid_info.values()
    for name,bid in bid_info.items():
      highest = max(list_info)
      if highest == bid:
        namme = name
        bidd = bid
    print(f"The winner is {namme} with a bid of {bidd}")
    end_bid = True
  else:
    clear_screen()