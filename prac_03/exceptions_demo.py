"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When I input a character instead a number it will occur a ValueError.
2. When will a ZeroDivisionError occur?
When I input a zero in denominator it will occur a ZeroDivisionError.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
I added a while loop for checking no zero input in denominator.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print('Cannot divide by zero!')
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
