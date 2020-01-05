from StackDemo import Stack

st = Stack()
ch = 0
while (1):
    print('1->Push')
    print('2->Pop')
    print('3->Peep')
    print('4->Display')
    print('5->Exit')
    ch = int(input('Enter your choice: '))
    if (ch == 1):
        Num = int(input('Enter the number'))
        st.push(Num)
    elif (ch == 2):
        Num = st.pop()
        if (Num == -1):
            print('Stack is empty')
        else:
            print('Popped number is ', Num)

    elif (ch == 3):
        print('Top element', st.peep())
    elif (ch == 4):
        print(st.display())
    elif (ch == 5):
        break;
    else:
        print('Wrong input')
