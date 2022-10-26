n=int (input("Enter a number  "))
def fact(x):
    if(x==0 or x==1):
        return 1
    else:
        i=1
        prod=1
        while(i<=x):
            prod=prod*i
            i=i+1
        return prod

j=0
while(j<=n):
    
    r=0
    while(r<=j):
        ncr=int(fact(j)/(fact(j-r)*fact(r)))
        print(ncr,end="\t")
        r=r+1
    j=j+1
    print()

/*   concept used- nCr expansion binomial expressions nCr=n!/((n-r)!*r!)   */
