#Astrologer's starts

n=int(input("enter the number: "))
b=int(input("Enter  1 or 0: "))
if b==1:
    i=1
    while i<=n :
        print(i*("*"))
        i=i+1
elif b==0 :
    i=n
    while i>=1 :
        print(i*("*"))
        i=i-1
else:
    print("wrong input!!! ")