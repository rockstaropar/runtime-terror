import random
print("**********************")
print("WELCOME")
print("RULES:")
print("ENTER 0 FOR STONE ")
print("ENTER 1 FOR PAPER ")
print("ENTER 2 FOR SCISSORS ")
print("")
print("")
print("")
print("")
Y=0
C=0
for i in range(0,5):
    r1=random.randint(0,2)
    r2=int(input("ENTER YOUR CHOICE: "))
    if(r1==0):
        print("COMPUTER CHOSE STONE")
    if(r1==1):
        print("COMPUTER CHOSE PAPER")
    if(r1==2):
        print("COMPUTER CHOSE SCISSORS")
    if(r2==0):
        print("YOU CHOSE STONE")
    if(r2==1):
        print("YOU CHOSE PAPER")
    if(r2==2):
        print("YOU CHOSE SCISSORS")
    print("*********************")
    if(r1==0 and r2==0):
        print("DRAW")
    if(r1==0 and r2==1):
        print("YOU WON")
        Y=Y+1
    if(r1==0 and r2==2):
        print("COMPUTER WON")
        C=C+1
    if(r1==1 and r2==0):
        print("COMPUTER WIN")
        C=C+1
    if(r1==1 and r2==1):
        print("DRAW")
    if(r1==1 and r2==2):
        print("YOU WON")
        Y=Y+1
    if(r1==2 and r2==0):
        print("YOU WON")
        Y=Y+1
    if(r1==2 and r2==1):
        print("COMPUTER WON")
        C=C+1
    if(r1==2 and r2==2):
        print("DRAW")
print("")
print("")
print("")
print("")
print("****END OF THE MATCH****")
print("**SCORE**")
print("YOUR POINTS:",Y)
print("COMPUTER POINTS:",C)
if(Y>C):
    print("YOU WON THE MATCH")
elif(C>Y):
    print("YOU LOST THE MATCH")
else:
    print("DRAW")
print("**********")
    
    
