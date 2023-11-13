#Lesson 16

#Example 1
#write a program that asks for a number samller than 10
x=int(input("give me a number smaller than 10:"))
if x<10:
    print("thank you")

#Example 2
#write a program that asks for a number smaller or equal than 10
x=int(input("give me a number smaller than or equal to 10:"))
if x<=10:
    print("thank you")

#Example 3
#write a program that asks for a number smaller or equal than 10 but greater than or equal to 5
x=int(input("give me a number smaller than or equal to 10 But greater than or equal to 5:"))
if x<=10:
    if x>=5:#IF a if inside another if we call it nesting like a nesting doll.
        print("thank you")


#Example 4
#write a program that asks for a number smaller or equal than 10 but greater than or equal to 5
x=int(input("give me a number smaller than or equal to 10 But greater than or equal to 5:"))
if x>10:
    print("no, you picked a number too big")
elif x<5:
    print("No, you pick a number too small")
else:
    print("Thank you")

#The difference between if if if if and if elif elif else is that the first situation all the ifs are INDIPENDENT
#But in the second situation ONLY ONE if the ifs can happen

#Example 5
#which of these two codes runs correctly?
x=int(input("give me an integer"))
if x>1000:
    print("wow, your x is really large, are you sure? ok!")
if x>100:
    print("Tat is a big x, okay")
if x>10:
    print("good x")
if x<=10:
    print("perfect x")
#lets check the elif
x=int(input("give me an integer"))
if x>1000:
    print("wow, your x is really large, are you sure? ok!")
elif x>100:
    print("Tat is a big x, okay")
elif x>10:
    print("good x")
else:
    print("perfect x")

#Example 6
#write some code that asks for the temperature,if the temperature is more than 25,print it is too hot
#if it is less than 20 print it is too cold
#But if it is between 20 and 25 print that the temperature is perfect
Temperature=int(input("Tell me today's temperature:"))
if Temperature>25:
    print("It is too hot")
elif Temperature<20:
    print("It is too cold")
else:
    print("It is perfect")
