# Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).

a = float(input("Enter  the length of side a: "))
b = float(input("Enter  the length of side b: "))
c = float(input("Enter  the length of side c: "))

if a == b == c:
    print("The triangle is equilateral.")
elif a == b or a == c or b == c:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")

