#  Take three sides of a triangle as input and check if they form a valid triangle.

a =  float(input("Enter the first side of the triangle: "))
b =  float(input("Enter the second side of the triangle: "))
c =  float(input("Enter the third side of the triangle: "))

if a+b>c and a+c>b and b+c>a:
    print("The sides form a valid triangle.")
else:
    print("The sides do not form a valid triangle.")
