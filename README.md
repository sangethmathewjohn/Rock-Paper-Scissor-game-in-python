# Rock-Paper-Scissor-game-in-python

## Simple rock paper scissor game using random function

## Program

    import random
    
    print("Welcome to Rock Paper Scissor Game")
    
    print("\nEnter r for Rock\nEnter p for Paper\nEnter s for scissors\n")
    
    player = input("\nEnter your choice r,p,s : ")
    lists=["r","p","s"]
    com = random.choice(lists) 
    
    print(f"\nComputer\'s choice : {com}") 
    print(f"Your choice : {player}")
    
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
