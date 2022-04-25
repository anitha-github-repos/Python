from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)

bid = {}

any_bidders = True
while any_bidders:
  name = input("What is your name?: ")
  bid_value = int(input("What's your bid?: $"))
  if name in bid:
    bid[name] += bid_value
  else:
    bid[name] = bid_value
  check_for_others = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if check_for_others == 'yes':
    clear()
  else:
    any_bidders = False
    clear()
max_value =max(bid.values())
max_key = max(bid,key = bid.get)
print(f"The winner is {max_key} with a bid of ${max_value}.")