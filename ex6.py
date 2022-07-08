import random
list1 = ["snake","water","gun"]
dictionary1={"s":"snake","w":"water","g":"gun"}
u = 0
c = 0
i = 1
flag = 0

print("WELCOME TO THE \"SNAKE WATER GUN\" GAME")
while i <= 10:
    i = i+1
    comp_choice = random.choice(list1)
    print("s - snake , w - water, g - gun")
    user_choice = input("Enter your choice: ")
    user_c = dictionary1[user_choice] #value in dictionary1 curresponding to the inputed value
    while user_choice in ("s", "w", "g"):
        if comp_choice == "snake" and user_choice == "w":
            c = c+1
            flag=1 #just to check which if statement is executed
        elif comp_choice == "snake" and user_choice == "g":
            u = u+1
            flag=2
        elif comp_choice == "water" and user_choice == "s":
            u = u+1
            flag=3
        elif comp_choice == "water" and user_choice == "g":
            c = c+1
            flag=4
        elif comp_choice == "gun" and user_choice == "s":
            c = c+1
            flag=5
        elif comp_choice == "gun" and user_choice == "w":
            u = u+1
            flag=6
        else:
            flag=7
        break
    print("Your choice = ", user_c , " & Computer choice = ", comp_choice)
    print("you: ", u, "comp: ", c)
    print(" ")

if u > c:
    print("You win :D")
elif u <c:
    print("Comp win :(")
else:
    print("Draw :/")
