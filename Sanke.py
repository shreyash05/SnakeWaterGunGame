import random
i=0
j=0
k=0
while(i<=5):
    list = [1, 2, 3]
    a = random.choice(list)
    print(a)

    print("Eneter your choice:1 for snake , 2 for water, 3 for gun =>")
    ch = int(input())

    if ch==1 and a==2 or ch==2 and a==3 or ch==3 and a==1 :
        print("You won this roun!")
        j=j+1

    elif ch==2 and a==1 or ch==3 and a==2 or ch==1 and a==3:
        print("You losed this round!")
        k=k+1

    elif ch==1 and a==1 or ch==2 and a==2 or ch==3 and a==3:
        print("Round drawed!")

    else:
        print("Please enter valide choice")
    i=i+1
if j>k :
    print("--------------------------")
    print("Congratulation!")
    print("You won the GAME!")
    print("--------------------------")

elif j==k:
    print("--------------------------")
    print("Match Draw")
    print("--------------------------")

else:
    print("--------------------------")
    print("You Losed")
    print("--------------------------")