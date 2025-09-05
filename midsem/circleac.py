#WAF that takes radius of a circle & returns its circumference and area without import math
import math
def circle_properties(radius):
    circumference = 2 * 3.14 * radius
    area = 3.14 * radius ** 2
    return circumference, area

radius = int(input("Enter the radius of the circle: "))
circumference, area = circle_properties(radius)
print(f"The circumference of the circle is: {circumference}")
print(f"The area of the circle is: {area}")