#Condition
#Loops
a = 10
b = 20
if a > b:
    print("a > b")
else :
    print("a < b")

#max between 3 numbers
num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
num3 = int(input("Enter num3"))

if num1 > num2 and num1 > num3:
    print("Max is",num1)
elif num2 > num1 and num2 > num3:
    print("Max is",num2)
else:
    print("Max is",num3)

#FOR LOOP
for i in range(1,11): #range() is started from zero
    print("Hello Sneha")

#While loop
i = 0
while i < 5:
    print("i")
    i = i + 1

#Progarm question
#print grades
score = int(input("Enter the score"))
if score >= 90 and score <= 100:
    print("Grade-A")
elif score >= 80 and score =< 89:
    print("Grade-B")
elif score >= 70 and score =< 79:
    print("Grade-C")
elif score >= 60 and score =< 69:
    print("Grade-D")
#elif score > 0 and score < 59:
    #print("Grade-F")
else:
    print("Grade-F")