n=int(input())
for i in range(1,n):
    for k in range(n-i,0,-1):
        print(" ",end="\t")
    for j in range(i,2*i):
        print(j,end="\t")
    for j in range(2*i-2,i-1,-1):
        print(j,end="\t")

    print()
