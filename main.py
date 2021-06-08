import random
player = input("enter your choice r,p,s:\n")
lists=["r","p","s"]
com = random.choice(lists) 
print(f"computer:{com}")
print(f"player:{player}")
if player == com:
  print("draw")
elif (player == "r") and (com=="s"):
  print("you win")
elif (player == "s") and (com=="p"):
  print("you win")
elif (player == "p") and (com=="r"):
  print("you win")
else:
    print("you loose")
