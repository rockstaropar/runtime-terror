x = int(input())
pascal = []
pascal.append([])
for f in range(0,16):
	pascal[0].append(0)
pascal[0].append(1)
print()
for f in range(0,16):
	pascal[0].append(0)
#to input the first line of 1024 elements which for my algo is important
for i in range(1,x+1):
	pascal.append([])
	c=0
	for k in range(0,33):
		pascal[i].append((pascal[i-1][c])+(pascal[i-1][c-1]))
		c+=1
for h in range(0,x):
	print(pascal[h])
##formula solver starts here
y = int(input("enter index of(x+y)"))
print("the coeffecients of its expasion are",pascal[y])
