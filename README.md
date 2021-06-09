# Rock-Paper-Scissor-game-in-python

## Simple rock paper scissor game using random function

## Program

    import random
    
    print("Welcome to Rock Paper Scissors Game")
    print("-----------------------------------")
    
    print("\nEnter r for Rock\nEnter p for Paper\nEnter s for Scissors\n")
    
    player = input("\nEnter your choice r,p,s : ")
    lists=["r","p","s"]
    com = random.choice(lists) 
    
    print(f"\nComputer\'s choice : {com}") 
    print(f"Your choice       : {player}\o")
    
    if player == com:
      print("draw")
    elif (player == "r") and (com=="s"):
      print("you won")
    elif (player == "s") and (com=="p"):
      print("you won")
    elif (player == "p") and (com=="r"):
      print("you won")
    else:
        print("you loose")

You can use ascii art to make it more intresrting and can be modified many way and you are always welcome to do so.
