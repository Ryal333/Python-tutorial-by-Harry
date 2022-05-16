List1=[]
i=0
while(True):
    itn=int(input("Enter number: "))
    if itn <= 100:
        List1.insert(i,itn)
        i=i+1
        print(List1)
        continue
    print("congrats Number is greater than 100")
    break




