import random
l=["siccor","rock","paper"]
while True:
    Ccount=0
    Usercount=0
    uc=int(input('''
Game star....
 1:yes
2:No/exit'''))
    if uc==1:
        for a in range(1, 6):
            user_input=int(input('''
1:paper
2:scissor
3:rock
'''))
        if user_input==1:
            uchoice="paper"
        elif user_input==2:
            uchoice="scissor"
        elif user_input==3:
            uchoice="rock"
        Cchoice = random.choice(l)
        if Cchoice==uchoice:
             print("computer value",Cchoice)
             print("user value,",uchoice)
             print("game draw")
             Ccount = Ccount+1
             Usercount =Usercount+1
        elif(uchoice=="rock" and Cchoice=="scissor")or(uchoice=="paper" and Cchoice=="rock")or(uchoice=="scissor"and Cchoice=="paper"):
             print("computer value", Cchoice)
             print("user value,", uchoice)
             print ("you win")
             Usercount = Usercount + 1
        else:
             print("computer value", Cchoice)
             print("user value,", uchoice)
             print("computer win")
             Ccount = Ccount + 1
        if Usercount==Ccount:
            print("finl game draw")
            print("user score",Usercount)
            print("computer scour",Ccount)
        elif Usercount>Ccount:
            print("final you win the game")
            print("user score", Usercount)
            print("computer scour", Ccount)
        else:
            print("final computer win the game")
            print("user score", Usercount)
            print("computer scour", Ccount)



    else:
        break;




