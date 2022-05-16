abc:
op1=int(input("enter the first operand: "))
opr=input("enter the operator: ")
op2=int(input("enter the second operand: "))
if opr=="+":
    result=op1+op2
elif opr=="-":
    result=op1-op2
elif opr == "*":
    result = op1 * op2
elif opr == "/":
    result = op1 / op2
else:
    result="invalid operator"

if op1==45 and op2==3 and opr=="*" :
    result=555
elif op1==56 and op2==9 and opr =="+":
    result=77
elif op1==56 and op2==6 and opr=="/":
    result=4
else:
    print(result)







# firstNum = input("Enter FirstNum :")
# operator = input("Enter operator :")
# secondNum = input("Enter SecondNum :")
# FaultyDict={"45*3":"555", "56+9":"77","56/6":"4"}
# expression = firstNum+operator+secondNum
# if expression in FaultyDict :
#     print (FaultyDict[expression])
# else:
#     print(eval(firstNum+operator+secondNum))
