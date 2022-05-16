no_of_guess=9
number=18
flag=0
n=no_of_guess
print("You have ",no_of_guess," guesses to identify the number")
while (no_of_guess>0):
    input1=int(input("\nEnter your number: "))
    no_of_guess=no_of_guess-1
    if input1>number:
        print("The number is less than ",input1)
        print("Number of guesses left: ",no_of_guess)
    elif input1<number:
        print("The number is greater than ",input1)
        print("Number of guesses left: ",no_of_guess)
    else:
        print("\nyou won!!!")
        flag=1
        break
if flag==1:
    print("you took ",n-no_of_guess," guesses to finish")
else:
    print("Game over :(")