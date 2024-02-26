#Write a program that classifies a traingle based on the lengths
#get three inputs values of lengths, determine if lengths are equal--equilateral,isosceles(two sides are equal),scalene(no sides are equal)

side1 = int(input("Enter the length of side1"))
side2 = int(input("Enter the length of side2"))
side3 = int(input("Enter the length of side3"))

if side1 == side2 == side3:
    print("It is a Equilateral triangle")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("It is a isosceles triangle")
elif side1 != side2 or side2 != side3 or side3 != side1:
    print("It is a scalene traingle")
#else:
    #print(NA)
