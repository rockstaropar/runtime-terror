x=int(input("Enter num:x"))
y=int(input("Enter num:y"))
st=0
if(y>x):
    print("end")
else:
    while(x!=y):
        if(x-y>5):
            y=y+5
            st=st+1
            if(y==x):
                break
        else:
            y=y+5
            st=st+1
            while(x!=y):
                y=y-1
                st=st+1
            if(y==x):
                break
print("minimum step=",st)
