print(type(str(21)))
name ="ANimesh"
print(name[5])#index starts with 0
#we can not change the chachters of string eg name[1]="D" will not work
print(name[0:2])#last wala exculding and first wal inculding
print(name[:2])#same as name[0:4] it will automatically take first index i.e 0
print(name[0:])#it will automatically take last index value i.r length-1

#negative index
'''h--> -1
   s--> -2
   .
   .
   A-->-7
   '''
print(name[-7])
print(name[1:2])
print(name[-3:-1])
#skiping values
#it will print from 0 to 6-1=5 by skiping every skipping 2 chacter
d=name[0:6:2]
print(d)
#string function
print(len(name))#length function
print(name.endswith("esh"))#true
print(name.startswith("AN"))#true
print(name.count("a"))#count number of "a"
str1="hello my work my job my routine"
print(str1.count("my"))
print(name.capitalize())#only makes the first word in string capital all other samll
print(str1.find("job"))#display index of first occurence of j in job
#returns -1 if not find
print(str1.replace("my","your"))

#escape sequence
print("my name is animesh.\nTyping is my job")
#\t gives tab
#\\ gives a backslash
#\' prints qoute


