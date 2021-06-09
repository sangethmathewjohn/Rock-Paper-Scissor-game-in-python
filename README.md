# Rock-Paper-Scissor-game-in-python

## Simple rock paper scissor game using random function

##Program

    import random
    player = input("enter your choice r,p,s:\n")
    lists=["r","p","s"]
    com = random.choice(lists) 
    print(f"computer:{com}")
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

You can use ascii art to make it more intresrting and can be modified many way and you are always welcome to do so.
