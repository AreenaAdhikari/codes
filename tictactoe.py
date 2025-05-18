theBoard = {'7': '','8':'','9':'',
            '4':'','5':'','6':'',
            '1':'','2':'','3':''}
board_keys=[]
for key in theBoard:
    board_keys.append(key)
def printBoard(board):
    print(board['7']+'|'+['8']+'|'+['9'])
    print('-+-+-')
    print(board['4']+'|'+['5']+'|'+['6'])
    print('-+-+-')
    print(board['1']+'|'+['2']+'|'+['3'])
    print('-+-+-')
def game():
   turn = 'X' 
   count = 0
for i in range(10):
    printBoard(theBoard)
    print("It is your turn"+turn+"Move in which place?")
move = input()
if theBoard[move] == '':
    theBoard[move] = turn
    count +=1
else:
    print("this place is already filled.\nMove to which place?")
    continue;
if count >=5:
    if theBoard['7'] == theBoard['8'] == theBoard['9'] ! = ' ':
     printBoard(theBoard)
     print("\nGame Over.\n")
     print("****"+turn+"won.****")
     break
    elif theBoard['1'] == theBoard['2'] == theBoard['3'] ! = ' ':
     printBoard(theBoard)
     print("\nGame Over.\n")
     print("****"+turn+"won.****")
     break
    elif theBoard['1'] == theBoard['4'] == theBoard['7'] ! = ' ':
     printBoard(theBoard)
     print("\nGame Over.\n")
     print("****"+turn+"won.****")
     break
    elif theBoard['2'] == theBoard['5'] == theBoard['8'] ! = ' ':
     printBoard(theBoard)
     print("\nGame Over.\n")
     print("****"+turn+"won.****")
     break
    elif theBoard['3'] == theBoard['6'] == theBoard['9'] ! = ' ':
     printBoard(theBoard)
     print("\nGame Over.\n")
     print("****"+turn+"won.****")
     break




