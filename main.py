import math

a = int(input("Enter first vector..."))
b = int(input("Enter second vector..."))
angle = int(input("Enter angle between vectors..."))

cos_result = round(math.cos(math.radians(angle)), 2)
print("Value of cos",angle, ":" ,cos_result)

resultant = math.sqrt((a**2) + (b**2) + (2*a*b) * cos_result)

print("Resultant is:",resultant)