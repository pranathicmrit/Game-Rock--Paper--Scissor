import random
print("Welcome to Rock Paper Scissors!")
print("-------------------------------")

###set up variables
cpuScore = 0
playerScore =0
tieScore = 0
possibleHands = ["rock", "paper", "scissor"]

def checkForWinner(playerHand, computerHand):
    if(playerHand == "rock" and computerHand == "paper"):
        print("Sorry you lost! :(")
        return "Cpu"
    elif(playerHand == "rock" and computerHand == "scissor"):
        print("Congrates! you win :)")
        return "Player"
    elif(playerHand == "scissor" and computerHand == "paper"):
        print("Congrates! you win :)")
        return "Player"
    elif(playerHand == "scissor" and computerHand == "rock"):
        print("Sorry you lost! :(")
        return "Cpu"
    elif(playerHand == "paper" and computerHand == "rock"):
        print("Congrates! you win :)")
        return "Player"
    elif(playerHand == "paper" and computerHand == "scissor"):
        print("Sorry you lost!")
        return "Cpu"
    else:
        print("It's a tie, play again!")
        return "Tie"

### start game loop
while(playerScore != 3 and cpuScore != 3):
    ###validate input
    while True:
        playerHand = input("\nPick a hand. rock, paper, or scissor:")
        if(playerHand == "rock" or playerHand == "paper" or playerHand == "scissor"):
            break
        else:
            print("Invalid input.Try again.")
    ### generate computer pick
    computerHand = random.choice(possibleHands)

    ###Print results
    print("Your hand:", playerHand)
    print("Cpu hand:", computerHand)
    result = checkForWinner(playerHand, computerHand)
    if(result == "Player"):
        playerScore += 1
    elif(result == "Cpu"):
        cpuScore += 1
    else:
        tieScore += 1
    print("Your Score:", playerScore, "Cpu Score:", cpuScore, "Tie Score:", tieScore)

print("Game Over! Thank you for playing :)")
