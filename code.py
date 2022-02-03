board={
    'T1':' ','T2':' ','T3':' ',
    'A1':' ','A2':' ','A3':' ',
    'C1':' ','C2':' ','C3':' '

}
player = 1       #first player
total_moves = 0  #count the moves
end_check = 0

def check():
    #checking the moves of player one
    #for horizontal condition
    if board['T1'] == 'X'and board['T2'] == 'X' and board['T3'] == 'X':
        print('Player one won')
        return 1
    if board['A1'] == 'X' and board['A2'] == 'X' and board['A3'] == 'X':
        print('Player one won')
        return 1
    if board['C1'] == 'X' and board['C2'] == 'X' and board['C3'] == 'X':
        print('Player one is won')
        return 1
    #for diagonal conditon
    if board['T1'] == 'X' and board['A2'] == 'X' and board['C3'] == 'X':
        print('Player one is won')
        return 1
    if board['T3'] == 'X' and board['A2'] == 'X' and board['C1'] == 'X':
        print('Player one is won')
        return 1
    #for vertical condition
    if board['T1'] == 'X'and board['A1'] == 'X' and board['C1'] == 'X':
        print('Player one won')
        return 1
    if board['T2'] == 'X' and board['A2'] == 'X' and board['C2'] == 'X':
        print('Player one won')
        return 1
    if board['T3'] == 'X' and board['A3'] == 'X' and board['C3'] == 'X':
        print('Player one is won')
        return 1
    #checking the moves of player two
    #for horizontal condition
    if board['T1'] == 'O'and board['T2'] == 'O' and board['T3'] == 'O':
        print('Player two won')
        return 1
    if board['A1'] == 'O' and board['A2'] == 'O' and board['A3'] == 'O':
        print('Player two won')
        return 1
    if board['C1'] == 'O' and board['C2'] == 'O' and board['C3'] == 'O':
        print('Player two is won')
        return 1
    #for diagonal conditon
    if board['T1'] == 'O' and board['A2'] == 'O' and board['C3'] == 'O':
        print('Player two is won')
        return 1
    if board['T3'] == 'O' and board['A2'] == 'O' and board['C1'] == 'O':
        print('Player two is won')
        return 1 
    #for vertical condition
    if board['T1'] == 'O'and board['A1'] == 'O' and board['C1'] == 'O':
        print('Player two won')
        return 1
    if board['T2'] == 'O' and board['A2'] == 'O' and board['C2'] == 'O':
        print('Player two won')
        return 1
    if board['T3'] == 'O' and board['A3'] == 'O' and board['C3'] == 'O':
        print('Player two is won')
        return 1
    return 0

    
    
print('T1|T2|T3')
print('- +- +-')
print('A1|A2|A3')
print('- +- +-')
print('C1|C2|C3')
print('====================')

while True:
    print(board['T1']+'|'+board['T2']+'|'+board['T3'])
    print('-+-+-')
    print(board['A1']+'|'+board['A2']+'|'+board['A3'])
    print('-+-+-')
    print(board['C1']+'|'+board['C2']+'|'+board['C3'])
    end_check = check()
    if total_moves == 9 or end_check == 1:
        break
    while True:     #input from player
        if player == 1:     #choose player
            p1_input = input('player one')
            if p1_input.upper() in board and board[p1_input.upper()] ==  ' ':
                board[p1_input.upper()] = 'X'
                player = 2
                break
            else:
                print('Invalid Input')
                continue

        else:
            p2_input = input('player two')
            if p2_input.upper() in board and board[p2_input.upper()] ==  ' ':
                board[p2_input.upper()] = 'O'
                player = 1
                break
            else:
                print('Invalid input')
                continue
    total_moves += 1
    print('=================')
    
