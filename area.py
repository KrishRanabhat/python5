import math

radius = float(input("Enter the radius of the circle:"))
side = float(input("Enter the side length of the square:"))
length = float(input("Enter the length of the rectangle:"))
width = float(input("Enter the width of the rectangle:"))

circle_area = math.pi * radius * radius

square_area = side * side

rectangle_area = length * width

print(f"The area of the circle is: {circle_area:.2f}")
print(f"The area of the square is: {square_area:.2f}")
print(f"The area of the rectangle is: {rectangle_area:.2f}") 




