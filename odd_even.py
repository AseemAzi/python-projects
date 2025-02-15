import random
def batting():
    print("batting")
    player_score = 0
    while True:
        try:
            play_mov= int(input("enter a number (1-6):"))
            if play_mov > 6:
                print("invalid input ")
                continue
            comp_mov= random.randint(1,6)
            print("comp_move:",comp_mov)
            if play_mov== comp_mov:
                break
            else:
                player_score+=play_mov
                print(f"player_score:{player_score}")
        except ValueError:
            print("invalid input") 
    return player_score    

def bowling():
    print("you are bowling")
    computer_score = 0
    while True:
        try:
            play_mov = int(input("enter a number (1-6):"))
            if play_mov > 6:
                print("invalid input ")
                continue
            comp_mov = random.randint(1,6)
            print("comp_move:",comp_mov)
            if comp_mov==play_mov:
                break
            else:
                computer_score+=comp_mov
                print(f"computer_score:{computer_score}")
        except ValueError:
            print("invalid input")
    return computer_score


def main():
    tose = random.choice(["batting","bowling"])
    if tose == "batting":
        player_score = batting()
        computer_score = bowling()
    else:
        computer_score = bowling()
        player_score = batting()
        
    if computer_score > player_score:
         print(f"computer wins with score of {computer_score}, player_score:{player_score}")
    elif computer_score < player_score:
         print(f"you wins wit score of {player_score} ,computer_score:{computer_score}")

main()