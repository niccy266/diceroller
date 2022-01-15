from random import randint
from time import sleep

help_ = """
Enter any positive number to roll a dice with that many sides
Enter Nothing to reroll the last dice (rolls a 20 if no dice have been rolled)
"h" for help
"q" to quit"""

def main() :
    startrolling()
    exit(0)

def startrolling():
    num = "pass"
    lastnum = "20"
    while(True) :
        if(num in ["0",""]) : num = lastnum; continue
        else :
            if(rolldice(num)) : lastnum = num
            num = input("\nHow many sides are on the next dice? ")
            if(num in ["0",""]) : num == lastnum; continue
            if(num.lower() in ["exit","quit","q","e"]) : break
            if(num.lower() in ["thanks","thankyou","tnks","thanq"]):
                num = "pass"
                print("you're welcome : )")
            if(num.lower() in ["h", "help"]):
                num = "pass"
                print(help_)
    
    print("Happy rolling!")
    sleep(.8)

def rolldice(num):
    if(num == "pass") : return False
    if(not num.isdigit() or int(num) < 0) :
        print("That wasn't a positive integer. (enter to reroll, q to quit)")
        return False
    elif(not num in ["0",""]):
        print("\trolled a\t", randint(1,int(num)), "on a \td" + num)
    return True

if(__name__ == "__main__") :
    main()
    
