#Question1-map function
data={'Madhu':29,'Sabrish':33,'Aaribellie':1,'Anandy':15,'Gokul':15,'Maadhi':3}
print(data.items())
result=()
result=list(map(lambda x:x[0],filter(lambda x:x[1]>18,data.items())))
print(result)

#Question2-reduce function to find product of numbers
from functools import reduce
input1=[1,3,5,6,7,34,45,536,76]
result=reduce(lambda x,y:x*y,input1)
print(result)

#Question3-finding even number and squaring it
input1=(1,3,5,6,3,24,67,8,653)
result=()
result=list(map(lambda x:x*x,filter(lambda x:x%2==0,input1)))
print(result)

#Question4-check if given string is a number
input1=('new','123','name','542','who','34','43')
result=()
result=list(filter(lambda x:x.isdigit()==True,input1))
print(result)

#Question5-import year month day from datetime object'
from datetime import datetime
dt=datetime.now()
print(dt)
result=lambda x:(x.year,x.month,x.day)
print(result(dt))

#Question6-fibanocci using lambda
n = int(input("Enter number: "))
fibanocci=()
fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
for i in range(n):
    print(fibonacci(i), end=" ")