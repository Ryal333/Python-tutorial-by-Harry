#ryal_ryalf_ryale
#karl_karlf_karle
#daisy_daisyf_daisye

def getdate():
    import datetime
    return datetime.datetime.now()

def function_log() :
    with open(final_name,"a+") as f:
        log=str(input("Enter your log: "))
        date=str(getdate())
        f.write(date + "  " + log + "\n")
        print("successfully logged : " , date + "  " + log)


def function_retieve():
    with open(final_name, "r") as f:
        print(f.read())


a=input("Enter 1 for logging \nEnter 2 for retrieving\n--> ")
if a=="1" or a=="2"  :
    name = int(input("Enter\n 1 for Ryal\n 2 for Karl\n 3 for Daisy\n--> "))
    if name == 1:
        name = "ryal"
    elif name == 2:
        name = "karl"
    elif name == 3:
        name = "daisy"
    else:
        print("Wrong input!! ")
        exit()

    fore = int(input("Enter \n 1 for Food\n 2 for Exercise\n--> "))


    if fore == 1:
        fore = "f"
    elif fore == 2:
        fore = "e"
    else:
        print("Wrong input!!! ")
        exit()

    name1 = name + fore
    final_name = name1 + ".txt"

else:
    print("wrong inputttttt")


if a=="1" :
    function_log()
elif a=="2" :
    function_retieve()
else:
    exit()