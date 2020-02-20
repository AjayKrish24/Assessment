# 1)

import random
numbers = []
for i in range(0,10):
    if i not in numbers:
        numbers.append(random.randrange(0,50))
print(numbers)
number = random.choice(numbers)
print(number)
print("3 chances to find the number?  Enter the number you guess : ")
for x in range(3):
    guess = int (input ())
    if x <= 1:
        if guess == number:
            print("You guessed correctly")
            break
        elif guess<=number+5 and guess>=number-5:
            print("You are close,try again")

        else:
            print("Wild guess ")
    else:
        if guess==number:
            print("You guessed correctly ")
            break
        else:
            print("Oops you are out of chances better luck next time")
   
#=======================o/p======================================         
[40, 19, 34, 2, 40, 15, 34, 44, 6, 49]                                                                                                                   
34                                                                                                                                                       
3 chances to find the number?  Enter the number you guess :                                                                                              
33                                                                                                                                                       
You are close,try again
22
Wild guess
43                                                                                                                                                       
Oops you are out of chances better luck next time                                                                                                        
                                                 

*************************************************************************************************** 

# 2)

num_dic = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9","plus":"+","minus":"-","divide":"%","product":"*"}

exp = input("Enter the string: ")
exp_list = exp.split(" ")
a = ""
for x in exp_list:
    for k,v in num_dic.items():
        if x == k:
            a = a + num_dic.get(k)
number = str(eval(a))
for x,y in num_dic.items():
    if number == y:
        print(x)

#=======================o/p======================================
Enter the string: one plus two                                                                                                                           
three 

***************************************************************************************************

# 3)

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

# ***************************************************************************************************

# 4)

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
 
# ***************************************************************************************************

# 5)

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

# ***************************************************************************************************
