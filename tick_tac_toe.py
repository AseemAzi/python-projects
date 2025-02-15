tic =["_","_","_",
      '_','_',"_",
      '_','_','_']
def print_tic():
    print(f" {tic[0]} │ {tic[1]} │ {tic[2]} ")
    print("───┼───┼───")
    print(f" {tic[3]} │ {tic[4]} │ {tic[5]} ")
    print("───┼───┼───")
    print(f" {tic[6]} │ {tic[7]} │ {tic[8]} ")
    print("\n")

def winning_():
    win_combinations= [(0, 1, 2), (3, 4, 5), (6, 7, 8),    
                    (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                    (0, 4, 8), (2, 4, 6)]
    
    for a,b,c in win_combinations:
        
        if  tic[a]==tic[b]==tic[c] and tic[a] in ['X',"O"]:
            return tic[a]
    return None

print_tic()
game_over = False
current_player = "X"
while not game_over:
    print(f"current_player:{current_player}")
    try:
        user= int(input("enter a number(0-8):"))
        if 0<= user <=8 and tic[user] not in ['X', "O"]:
            tic[user]= current_player
            print_tic()
        else:
            print("invalid move")
            continue
    except ValueError:
        print("invalid input!!!  enter number b/w:(0-8)")
    winner = winning_()
    if winner:
        print_tic()
        print(f" winner is {winner}")
        game_over = True
        break
    if "_" not in tic:
        print_tic()
        print("It's a draw!")
        game_over = True
        break
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'