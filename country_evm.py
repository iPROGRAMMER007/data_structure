print("------------COUNTRY ELECTION------------")
print('')


a=0
b=0
c=0
d=0
e=0

true = bool

while true:

    print('Press 1 to vote INDIA')
    print("Press 2 to vote CHINA")
    print('Press 3 to vote AMARICA')
    print('Press 4 to vote JAPAN')
    print('Press 5 to vote BRITEN')
    print('')
    print('Press a number to vote : ', end="")

    n = int(input())

    if n==1:
        a=a+1
        print("You vote for INDIA")
        print("COUNTRY\t\t\t\t\tVOTE")
        print('')
        print("INDIA\t\t\t\t\t",a)
        print("CHINA\t\t\t\t\t",b)
        print("AMARICA\t\t\t\t\t",c)
        print("JAPAN\t\t\t\t\t",d)
        print("BRITEN\t\t\t\t\t",e)

    if n==2:
        b=b+1
        print("You vote for CHINA")
        print("COUNTRY\t\t\t\t\tVOTE")
        print('')
        print("INDIA\t\t\t\t\t",a)
        print("CHINA\t\t\t\t\t",b)
        print("AMARICA\t\t\t\t\t",c)
        print("JAPAN\t\t\t\t\t",d)
        print("BRITEN\t\t\t\t\t",e)

    if n==3:
        c=c+1
        print("You vote for AMARICA")
        print("COUNTRY\t\t\t\t\tVOTE")
        print('')
        print("INDIA\t\t\t\t\t",a)
        print("CHINA\t\t\t\t\t",b)
        print("AMARICA\t\t\t\t\t",c)
        print("JAPAN\t\t\t\t\t",d)
        print("BRITEN\t\t\t\t\t",e)

    if n==4:
        d=d+1
        print("You vote for JAPAN")
        print("COUNTRY\t\t\t\t\tVOTE")
        print('')
        print("INDIA\t\t\t\t\t",a)
        print("CHINA\t\t\t\t\t",b)
        print("AMARICA\t\t\t\t\t",c)
        print("JAPAN\t\t\t\t\t",d)
        print("BRITEN\t\t\t\t\t",e)


    if n==5:
        e=e+1
        print("You vote for BRITEN")
        print("COUNTRY\t\t\t\t\tVOTE")
        print('')
        print("INDIA\t\t\t\t\t",a)
        print("CHINA\t\t\t\t\t",b)
        print("AMARICA\t\t\t\t\t",c)
        print("JAPAN\t\t\t\t\t",d)
        print("BRITEN\t\t\t\t\t",e)

    print("Press y/Y to continue: ",end="")
    x = str(input())
    if x == 'y' or x == 'Y' :
        continue
    else:
        break









