#calculator
from random import randint
list=[]
for i in range(20):
    n=randint(1,100)
    list.append(n)
for num in list:
    print(num)
for num in list:
    sum=num+num
avg=sum/len(list)
print(avg)

list.sort()
print(list)
print(list[-2])
print(list[1])
g=0
count=0
for num in list:
    if num%2==0:
        count=count+1
        print(count)
    elif num%2 !=0:
        g=g+1
        print(g)


    