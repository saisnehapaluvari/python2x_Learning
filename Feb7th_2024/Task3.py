#Explain the difference between "=" and "==" operator in python
#//The "=" symbol is defined as assignment operator,It requires one variable on its left and one variable on its right.
#// a = 10

#//The "==" symbol is comparison operator and it is called as equal to operator.
#It returns true if operands on either side are equal,other wise it returns false.
# 10 + 2 == 10
# False

#What does the "**" operator in python, how is it used?
#//The "**" operator is exponentation means "power property operator".
#// x = 2
#// y = 5
#//print(x ** y) ---> 2^5 = 2*2*2*2*2
#//output: 32

#What does the "^"operator in python,in what context it is commonly used?
#It is a logical operator
#It is a XOR Operator,Sets each bit if only one of two bits is 1.
#x ^ y

#Write a program for calculate area of a circle given its radius using the formula area = pi * r^2

r = int(input("Enter radius of circle"))
pi = 3.14
area = pi * (r ** 2)
print(area)