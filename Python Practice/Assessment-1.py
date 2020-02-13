2)

d={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
e={'plus':'+','minus':'-','multily':'*','divide':'/'}
s=input("Enter the expression: \n")
l=s.split(" ")
# print(l)
for k in d:
    if l[0]==k:
        a=d.get(k)
    if l[2]==k:
        b=d.get(k)
# print(a,b)
for key in e:
    if l[1]==key:
        x=a+e.get(key)+b
       
print(eval(x))

***************************************************************************************************

3)

num=int(input("Enter a number : "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
elif num % 3 == 0 and num % 5 != 0:
    print("Divisible only by 3")
elif num % 3 != 0 and num % 5 == 0:
    print("Dvisible only by 5")
else:
    print("Not divisible by both 3 or 5")


#=======================o/p======================================

Enter a number : 15                                                                                                           
Divisible by both 3 and 5

***************************************************************************************************

4)

num1 = int(input("Enter starting range: "))
num2 = int(input("Enter ending range: "))
sum = 0
for  i in range(num1, num2):
    if i % 3 == 0:
        sum += i
print(sum)


#=======================o/p======================================

Enter starting range: 2                                                                                                       
Enter ending range: 20                                                                                                        
63
 
***************************************************************************************************

5)

import calendar

dob = input("Enter Birthdate (yyyy-mm-dd) : ")
date = dob.split("-")
day = calendar.weekday(int(date[0]),int(date[1]),int(date[2]))
print(day)
print(calendar.day_name[day])

#=======================o/p======================================

Enter Birthdate (yyyy-mm-dd) : 2020-03-24                                                                                                                
1                                                                                                                                                        
Tuesday

***************************************************************************************************