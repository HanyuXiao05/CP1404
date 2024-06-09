import random

print(random.randint(5, 20))  # line 1
# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# I saw 17,5,11 on Line 1.The smallest number was 5, the largest was 20.


print(random.randrange(3, 10, 2))  # line 2
# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
# I saw 5,3,9 on line 2.The smallest number was 3, the largest number was 9.Line 2 couldn't produce a 4 because the step was 2.


print(random.uniform(2.5, 5.5))  # line 3
# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# I saw 4.393277910911185, 3.8390889952845204, 5.399700235507542 on line 3.The smallest number was 2.5, the largest was 5.5


# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
random_number = random.randint(0,100)
print(random_number)