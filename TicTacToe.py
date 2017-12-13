import random

def display_board(board):
    print board[:3]
    print board[3:6]
    print board[6:]

def player_input():
    while (True):
        print "Enter input:"
        x = raw_input()
        if x == 'X' or x == 'O':
            break
    return x


def place_marker(board, marker, position):
    if position in xrange(1,10):
        board[position-1] = marker
        

def win_check(board,mark):
    if board[:3] == [mark,mark,mark]:
        return True
    elif board[3:6] == [mark,mark,mark]:
        return True
    elif board[6:] == [mark,mark,mark]:
        return True
    elif board[::4] == [mark,mark,mark]:
        return True
    elif board[2:8:2] == [mark,mark,mark]:
        return True
    elif board[::3] == [mark,mark,mark]:
        return True
    elif board[2::3] == [mark,mark,mark]:
        return True
    elif board[1::3] == [mark,mark,mark]:
        return True
    else:
        return False
        

def choose_first():
    p = random.randint(1,2)
    return p

def space_check(board, position):
    if position in xrange(1,10):
        if board[position-1] == 'X' or board[position-1] == 'O':
            return False
        else:
            return True
            
def full_board_check(board):
    result = True
    for i in board:
        if i != 'X' and i != 'O':
            result = False
            break
    return result
    
    
def player_choice(board):
    while(True):
        print 'Type position:'
        x = int(raw_input())
        if x in xrange(1,10):
            break
    isFree = space_check(board,x)
    if isFree:
        return x
        
        
def replay():
    response = False
    while(True):
        print 'Want to keep playing? Y/N'
        res = raw_input()
        if res == 'Y' or res == 'N':
            break
    if res == 'Y':
        response = True
    return response
    
print('Welcome to Tic Tac Toe!')
board = range(1,10)
display_board(board)
first = choose_first()
print 'Player ', str(first)
while True:
    marker = player_input()
    position = player_choice(board)
    if space_check(board, position):
        place_marker(board, marker, position)
        display_board(board)
        if win_check(board,marker):
            print 'Somebody won'
            if replay():
              board = range(1,10)
              display_board(board)
              first = choose_first()
            else:
              break
        else:
            if full_board_check(board):
                print 'Empateeeee'
                if replay():
                  board = range(1,10)
                  display_board(board)
                  first = choose_first()
                else:
                  break
            else:
                continue
    else: 
        continue
