import random
print("..................ROCK-PAPER-SCISSORS GAME........................")
c="yes"
while(True):
    if c=="yes":
        user_choice=int(input("choose 0 for rock,choose 1 for paper, choose 2 for scissors"))
        computer_choice=random.choice([0,1,2])
        print("computer choice is:",computer_choice)
        
        if(computer_choice==user_choice):
            print("the game draw")
        elif(computer_choice>user_choice):
            print("you lost the game")
        elif(user_choice>computer_choice):
            print("you won the game")
        elif(computer_choice==0 and user_choice==2):
            print("you lost the game")
        else:
            print("you won the game")
        c=input("are you wanted to play again (yes/no)").lower()
    else:
        print("you are exited")
        break



