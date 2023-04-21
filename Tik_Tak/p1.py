game=['_','_','_','_','_','_','_','_','_']
i=1
while i<10:
    if i%2==0:
        pos=int(input("Enter a turn => "))
        if game[pos-1]=='_':
            game[pos-1]='\033[32mX'
        else:
            print("Already occupied")
            i=i-1
    else:
        pos=int(input("Enter b turn => "))
        if game[pos-1]=='_':
            game[pos-1]='\033[91mO'
        else:
            print("Already occupied")
            i=i-1

    print("After",i,"turn")
    print("*"*27)
    print("*"*6,"|",game[0],"|",game[1],"|",game[2],"|","*"*6)
    print("*"*6,"|",game[3],"|",game[4],"|",game[5],"|","*"*6)
    print("*"*6,"|",game[6],"|",game[7],"|",game[8],"|","*"*6)
    print("*"*27)
    if game[0]==game[1] and game[0]==game[2] and game[2]=="\033[91mO":
        print("B is winner :)")
        i=15
    elif game[0]==game[1] and game[0]==game[2] and game[2]=="\033[32mX":
        print("A is winner :)")
        i=15
    elif game[3]==game[4] and game[3]==game[5] and game[5]=="\033[91mO":
        print("B is winner :)")
        i=15
    elif game[3]==game[4] and game[3]==game[5] and game[5]=="\033[32mX":
        print("A is winner :)")
        i=15
    elif game[6]==game[7] and game[6]==game[8] and game[8]=="\033[91mO":
        print("B is winner :)")
        i=15
    elif game[6]==game[7] and game[6]==game[8] and game[8]=="\033[32mX":
        print("A is winner :)")
        i=15
    elif game[0]==game[3] and game[0]==game[6] and game[6]=="\033[91mO":
        print("B is winner :)")
        i=15
    elif game[0]==game[3] and game[0]==game[6] and game[6]=="\033[32mX":
        print("A is winner :)")
        i=15
    elif game[1]==game[4] and game[1]==game[7] and game[7]=="\033[91mO":
        print("B is winner :)")
        i=15
    elif game[1]==game[4] and game[1]==game[7] and game[7]=="\033[32mX":
        print("A is winner :)")
        i=15
    elif game[2]==game[5] and game[2]==game[8] and game[8]=="\033[91mO":
        print("B is winner :)")
        i=15
    elif game[2]==game[5] and game[2]==game[8] and game[8]=="\033[32mX":
        print("A is winner :)")
        i=15
    elif game[2]==game[4] and game[2]==game[6] and game[6]=="\033[91mO":
        print("B is winner :)")
        i=15
    elif game[2]==game[4] and game[2]==game[6] and game[6]=="\033[32mX":
        print("A is winner :)")
        i=15
    elif game[0]==game[4] and game[0]==game[8] and game[8]=="\033[91mO":
        print("B is winner :)")
        i=15
    elif game[0]==game[4] and game[0]==game[8] and game[8]=="\033[32mX":
        print("A is winner :)")
        i=15
    i=i+1