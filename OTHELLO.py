"""
A Python module for the Othello game made during a university project.
Split into 12 functions so easy to see how the game was made and what each 
line of code does.
"""

from copy import deepcopy
def newGame(player1,player2):
    """
    Makes simple game dictoinary. Who and board are always the same
    however player1 and player2 names change depend on whats entered
    """
    game = {'player1' : player1,
            'player2' : player2,
            'who' : 1,
            'board' : [[0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0],
                       [0,0,0,2,1,0,0,0],
                       [0,0,0,1,2,0,0,0],
                       [0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0]]
            }

    return game

def printboard(board):
    """
    This first part checks every single tile of board. Any tile with 1's or 2's in
    get assinged X or O respectively.
    """
    board2=deepcopy(board)
    for i in range(8): #checks all rows
        for j in range(8): #checls all colms
            if board2[i][j]==1: 
                board2[i][j]="X" #any 1's puts X
            if board2[i][j]==2:
                board2[i][j]="O" #any 2's put O
            if board2[i][j]==0:
                board2[i][j]=" "
    """
    This part puts the borders on. I added bottom and right side to
    make it easier to see what to type when playing.
    It then makes up the centre of board step by step by checking 
    each entry for board for i and j hence str(board[i-1][j]).
    adding on lines |.
    """
    topborder = " |a|b|c|d|e|f|g|h|"
    horizontalborder = " +-+-+-+-+-+-+-+-+"
    print(topborder)
    print(horizontalborder)
    row = '' #row empty string to start
    k=1
    for i in range(1,9):#counts rows while printing the row in question
        row = str(i)#starts with row number
        for j in range(8):#loops through the lists values and turns the to strings adds them before printing them
            row += '|' + str(board2[i-1][j])
        row+= "|"+str(k)
        k=k+1    
        print(row)
    print(horizontalborder)
    print(topborder)
    return 

def strToIndex(s):
    """
    Code checks if (s) in correct format. Does this by removing spaces. Once spaces removed
    the length should be exaclty 2, if not the case then raises value error.
    The code then check s[0] and s[1] to see if only one is a number and only one is a letter.
    It then changes this input into tuple form we need.
    """
    letters=['A','B','C','D','E','F','G','H','a','b','c','d','e','f','g','h']
    if ' ' in s:
        s=s.replace(" ","")
    i = len(s)
    (r,c) = ("fail","fail")
    if i != 2:
        raise ValueError
    
    if i == 2:
        for j in range(2):
            try: 
                if int(s[j]) in range(1,9):
                      r = int(s[j])-1
            except ValueError:
                if s[j] in letters:
                            c = s[j]
                else:
                    raise ValueError
        if r == "fail" or c == "fail":
            raise ValueError
    for h in range(0, 16):
         if c==letters[h]:
             c=h
    if c>=8:
        c=c-8
            
    return (r,c)

    strToIndex(s)

def indexToStr(t):
    """
    Just reverses strToIndex. 
    """
    letters2=['a','b','c','d','e','f','g','h']
    s1=str(letters2[t[1]])
    s2 = str((t[0])+1)
    return s1+s2

def loadgame():
    """
    Loadgame tries to open game.txt file. This file, if in right format should be the same
    as the newGame dictoinary however the board could be filled with more entries and who could be on 
    either player. If wrong format it checks and raises ValueError.
    """
    try:
        f = open("game.txt",mode="rt",encoding="utf8")
    except FileNotFoundError:
        raise FileNotFoundError("Incorrect file name")   
    try:
        player1= ((f.readline()).replace(' ','')).replace('\n','')
        player2= ((f.readline()).replace(' ','')).replace('\n','')
    except TypeError:
        raise ValueError
    try:
        whosturn=int(f.readline())
    except ValueError:
        raise ValueError("Incorrect format")
    if whosturn != 1 and whosturn != 2:
        raise ValueError("Incorrect format")
        
    if player1=='' or player2=='':
        raise ValueError
    
    currentboard=f.readlines()
    
    if currentboard == []:
        raise ValueError("Incorrect format")
    
    currentboard2 =[]
    
    try:
        for j in range(8):
            currentboard2 += list((((currentboard[j]).replace(' ','')).replace('\n','')).replace(',',''))
    except IndexError:        
        raise ValueError("Incorrect format")
    
    try:
        for i in range(64):
            currentboard2[i]=int(currentboard2[i])
    except ValueError:
        raise ValueError("Incorrect format")
    except IndexError:
        raise ValueError("Incorrect format")
    
    if len(currentboard2) != 64:
        raise ValueError("Incorrect format")
        
    board=[]    
    h=[]
    for k in range(8):
        for l in range (8):
            board.append(currentboard2[k*8+l])
        h.append(board)  
        board=[]
    for p in range(8):
        for o in range(8):
            if h[p][o] !=  1 and h[p][o] != 2 and h[p][o] != 0:
                raise ValueError("Incorrect format")
        
    game = {'player1' : player1,
                'player2' : player2,
                'who' : whosturn, 
                'board' :h
    }

    return game

def getLine(board,who,pos,dir):
    """
    This function takes the current board, and then for who's turn it is, it works out
    all the possible positions that are would make a line with a valid dir. dir meaning the line is 
    a straight line. If thats diagonal horizontal or vertical.
    """
    linemade = []
    while 0<=pos[0]+dir[0]<8 and 0<=pos[1]+dir[1]<8:
        tile=(pos[0]+dir[0],pos[1]+dir[1])
        if board[tile[0]][tile[1]] == 0:
            
                return []
        if board[tile[0]][tile[1]] == who:
    
            return linemade
    
        else:
            linemade.append(tile)
            pos = tile

    if board[pos[0]][pos[1]]!=who:
        return []
    
    return linemade

def getValidMoves(board,who):
    """
    This function makes sure any positons in getLine are acctually valid moves for the player. Does this
    by making sure the chosen postion is empty and a players piece isnt already there. It then checks this 
    postion is in the getLine and would actually make a line. 
    """
    vm=[]
    for i in range(8):
            for j in range(8):
                if board[i][j] == 0:
                        for r in range(-1,2):
                            for t in range(-1,2):
                                if r != 0 or t != 0:
                                    if getLine(board,who,(i,j),(r,t))!=[]:
                                        if (i,j) not in vm:
                                             vm.append((i,j))
                
                     
    return vm
                                                                                                                                                                                                                                                                                                                                  
def makeMove(board,move,who):
    """
    This function makes the whole line the players pieces by using for (i,j) in 
    getLine(board,who,pos,(r,t)). This line and line below make any tile in the 
    getLine for chosen move the players pieces.Then enters the players piece into the
    postion requested (move) to finish the line off.
    """
    pos = move
    for i in range(8):
            for j in range(8):
                for r in range(-1,2):
                    for t in range(-1,2):
                        for (i,j) in getLine(board,who,pos,(r,t)):
                            board[i][j] = who
    board[move[0]][move[1]]=who
    
    return board

def scoreBoard(board):
    """
    Scoreboard keeps track of the score. Postive for player 1 winning. Negative
    for player 2 winning.
    """
    score = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                score +=1
            if board[i][j]== 2:
                score-=1
    return score

def suggestMove1(board,who):
    """
    Simple move calcultor for the computer to make. Just chooses the move that 
    will return the greatest score for the player. Rembering greater score for 
    player 2 means more negative.
    
    """
    board2 = deepcopy(board)
    valid = getValidMoves(board2,who)
    
    if who==1:
        orginal=-64
    else:
        orginal=64
    
    if valid==[]:
        return None
    else:
        if who == 1:
            for i in valid:
                board2 = deepcopy(board)
                score=scoreBoard(makeMove(board2,i,who))
                if score>=orginal:
                    move= i
                    orginal = score
        if who == 2:
            for i in valid:
                board2 = deepcopy(board)
                score=scoreBoard(makeMove(board2,i,who))
                if score<=orginal:
                    move= i
                    orginal = score
    return(move)
# ------------------- Main function --------------------
def play():     
    print("*"*55)
    print("***"+" "*8+"WELCOME TO ADAM'S OTHELLO GAME!"+" "*8+"***")
    print("*"*55,"\n")
     
    """"
     This starting section works out players names, then makes the game 
     dictionary depending on whats been entered. If L entered skips asking 
    player 2's name and loads game.txt file as the dictionary.
    """ 
    print("Enter the players' names, or type 'C or 'L'.\n")
    player1 = (str(input("Player one, enter your name: ").replace(' ',''))).capitalize()
    while player1 == '':
        player1=(str(input("Name invalid.Player one enter a valid name:").replace(' ',''))).capitalize()
    if player1 == 'L':
        h=loadgame()
        player1=(h['player1']).capitalize()
        player2=(h['player2']).capitalize()
        who=h['who']
        board = h['board']
    else:
        player2 = (str(input("Player two, enter your name: ").replace(' ',''))).capitalize()
        while player2 == '':
            player2=(str(input("Name invalid.Player two enter a valid name:").replace(' ',''))).capitalize()
        who = 1
        g=newGame(player1,player2)
        board =g['board']
    
    
    """
    This part of code assigns whos go it is. It then takes the input and if its
    valid move returns new board and switches players go. If no more valid moves
    for either player it gets out of while loop. If player == 'c' they is 
    a small serpate code within the loops for what should happen.
    If player 1 entered L it will have loadedgame from the above code and just
    continue from where that game left off.
    """   
    while getValidMoves(board,1)!=[] or getValidMoves(board,2)!=[]:
        while who == 1:
            print("\n") #this just adds a new empty line
            printboard(board)
            valid = getValidMoves(board,who)
            if valid ==[]:
                print("No valid moves possible for "+player1+"(X), switching player. ")
                who = 2
            else:
                if player1 == 'C':
                    print("\n")
                    print("Computer (X) thinking...")
                    move = suggestMove1(board,who)
                    print("Computer (X) makes move "+indexToStr(move))
                    makeMove(board,move,who)
                    who = 2
                
                else:
                    move = input(player1+"'s turn (X). Make your move: ")
                    while move not in valid:
                        try: move = strToIndex(move)
                        
                        except ValueError:
                              move = input("Move invalid. Still "+player1+"'s turn (X). Make your move: ")
                        else:
                            if move in valid: 
                                        makeMove(board,move,who)
                                        who = 2 
        while who == 2:
            print("\n")
            printboard(board)
            valid = getValidMoves(board,who)
            if valid ==[]:
                print("No valid moves possible for "+player2+"(O), switching player. ")
                who = 1
            else:
                if player2 == 'C':
                    print("\n")
                    print("Computer (O) thinking...")
                    move = suggestMove1(board,who)
                    print("Computer (O) makes move "+indexToStr(move))
                    makeMove(board,move,who)
                    who = 1
                else:
                    move = input(player2+"'s turn (O). Make your move: ")
                    while move not in valid:
                        try: move = strToIndex(move)
                        
                        except ValueError:
                              move = input("Move invalid. Still "+player2+"'s turn (O). Make your move: ")
                        else:
                            if move in valid:
                                        makeMove(board,move,who)
                                        who = 1   
                                        
    """
    When no valid moves available it will no longer be in the above while loop. 
    Then the code below will be executed. It just wraps the game up giving 
    final score and who won.
    """                                  
    print("\n")             
    printboard(board)
    print("No more valid moves for either player.")
    print("Game over.")     
    score = scoreBoard(board)
    score1=str(score) #had to use this as couldnt str line above for some reason
    if score > 0:
        print(player1+"(X) is the winner! With a final score of: "+score1)    
    if score == 0:
        print("The game is a draw! As the final score was: "+score1) 
    if score < 0:
        print(player2+"(O) is the winner! With a final score of: "+score1) 

    
# the following allows your module to be run as a program
if __name__ == '__main__' or __name__ == 'builtins':
    play()


