# #Task4
# #Question 1#Even and add list
main_list =[10,501,22,37,100,999,87,351]
even_list=[]
odd_list=[]
for number in main_list:
    if number%2==0:
        even_list.append(number)

    else:
        odd_list.append(number)
print('even list' , even_list)
print('odd_list', odd_list)

# #Question2 # Prime number list
main_list =[10,501,22,37,100,999,87,351]
primenumber_list=[]
for number in main_list:
    if number>1:
        for i in range(2,number):
            if number%i==0:
                break
        else:
            primenumber_list.append(number)
print('primenumber list' , primenumber_list)

#Question3 #Happy numbers
main_list =[10,501,22,37,100,999,87,351]
Happynumbers_list=[]
for number in main_list:
    original = number
    while number!=1 and number!=4:
        total=0
        while number>0:
            digit = number%10
            total =total+digit*digit
            number=number//10
        number=total
    if number ==1:
        Happynumbers_list.append(original)

print('Happynumbers list' , Happynumbers_list)

#Question4 #Sum of first and last digit.
number=int(input('Enter the number', ))
last_digit=number%10
while number>9:
    number=number//10
count=last_digit+number
print('The summ of first and last digit of number is',count)

#Question5 #All the ways from 1,2,5,10 to make count of 10
sum = 10
for i in range(0,sum//1+1):
    for j in range(0,sum//2+1):
        for k in range(0,sum//5+1):
            for l in range(0,sum//10+1):
                if (1*i + 2*j + 5*k + 10*l)==10:
                    print(f"1 rupee:{i} , 2 rupee:{j}, 5 rupee:{k},10 rupee:{l}")
                    print('---------------------------------------------')

#Question6 #Duplicate of 3 lists
list1=[1,2,3,4,5,6,7,8]
list2=[4,5,6,7,9,10,11,12]
list3=[2,4,6,8,10,12,14,15]
for i in list1:
    for j in list2:
        for k in list3:
            if i==j==k:
                print('common element is',i)

#Question7 #First non repeating element in list
list=[1,1,2,2,3,3,4,5,6,7,7]
length=len(list)
for i in range(0,length):
    if i==0:
        if (list[i]!=list[i+1]):
            print('First non repeating elements in list is',list[i])
            break
    elif i==(length-1):
        if (list[i]!=list[i-1]):
            print('First non repeating elements in list is',list[i])
            break
    else:
        if list[i] != list[i-1] and list[i] != list[i+1]:
            print('First non repeating elements in list is',list[i])
            break

#Question8 #Find minimum element in sorted list
list=[3,345,4545,23,52,626,978,96]
sortedlist=sorted(list)
print('sortedlist is',sortedlist)
print('The minimum element is',sortedlist[0])

#Question9 #Find triplet in given list
list1=[10,20,30,9]
value =59
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        for k in range(j+1,len(list1)):
            if list1[i]+list1[j]+list1[k] == value:
                print('Triplet is ',list1[i],list1[j],list1[k])

#Question10 #sub list with sum=0
list1=[4,2,-3,1,6]
value =0
sublist=[]
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        for k in range(j+1,len(list1)):
            if list1[i]+list1[j]+list1[k] == value:
                sublist.append([list1[i],list1[j],list1[k]])
                print('Sublist is',sublist)

        
