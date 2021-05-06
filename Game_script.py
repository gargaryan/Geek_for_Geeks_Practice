count_start=int(input("Game Starts from : "))
def fun(count_start):
    while(count_start!=0):
        player1=int(input("Enter Player 1 : "))
        count_start-=player1
        print("player 1",count_start)
        if(count_start==0):
            return "player1"
        player2=int(input("Enter Player 2 : "))
        count_start-=player2
        print("Player2 ",count_start)
        if(count_start==0):
            return "player2"
print("Game loose by",fun(count_start))
