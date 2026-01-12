name = input("What's your name? ").strip()
if name:
    print(f"Hello, {name}!")
else:
    print("Hello!")
print("__________________________")
#Write a program that asks the user for the radius of a circle and the prints out the circumference of the circle.
import math

while True:
    try:
        r = float(input("Enter the radius of the circle: "))
        if r < 0:
            print("Radius must be non-negative.")
            continue
        break
    except ValueError:
        print("Please enter a number.")

circumference = 2 * math.pi * r
print(f"The circumference is: {circumference:.4f}")
print("__________________________")
#Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides.
def get_positive_float(prompt):
    while True:
        try:
            v = float(input(prompt))
            if v < 0:
                print("Value must be non-negative.")
                continue
            return v
        except ValueError:
            print("Please enter a number.")

length = get_positive_float("Enter the length: ")
width  = get_positive_float("Enter the width: ")

perimeter = 2 * (length + width)
area = length * width

print(f"Perimeter: {perimeter}")
print(f"Area: {area}")
print("__________________________")
#Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.
nums = []
for i in range(1, 4):
    while True:
        try:
            n = int(input(f"Enter integer #{i}: "))
            nums.append(n)
            break
        except ValueError:
            print("Please enter a valid integer.")

s = sum(nums)
product = nums[0] * nums[1] * nums[2]
average = s / 3

print(f"Sum: {s}")
print(f"Product: {product}")
print(f"Average: {average}")
print("__________________________")
#Write a program that asks the user to enter a mass in medieval units: talents, pounds, and lots
def get_nonnegative_float(prompt):
    while True:
        try:
            v = float(input(prompt))
            if v < 0:
                print("Please enter a non-negative number.")
                continue
            return v
        except ValueError:
            print("Please enter a number.")

talents = get_nonnegative_float("Enter talents: ")
pounds  = get_nonnegative_float("Enter pounds: ")
lots    = get_nonnegative_float("Enter lots: ")

POUNDS_PER_TALENT = 20
LOTS_PER_POUND = 32
GRAMS_PER_LOT = 13.3

total_lots = talents * POUNDS_PER_TALENT * LOTS_PER_POUND + pounds * LOTS_PER_POUND + lots
total_grams = total_lots * GRAMS_PER_LOT

kilograms = int(total_grams // 1000)
remaining_grams = total_grams - kilograms * 1000

print(f"The weight in modern units:")
print(f"{kilograms} kilograms and {remaining_grams:.2f} grams.")
print("__________________________")
#Write a program that draws two random combinations of numbers for a combination lock:
    #a 3-digit code where each number is between 0 and 9.
    #a 4-digit code where each number is between 1 and 6.
import random

code3 = [str(random.randint(0, 9)) for _ in range(3)]
code4 = [str(random.randint(1, 6)) for _ in range(4)]
print("random combinations")
print("3-digit code (each 0-9):", " ".join(code3))
print("4-digit code (each 1-6):", " ".join(code4))
print("__________________________")
print("Done, Thank you!")
print("__________________________")