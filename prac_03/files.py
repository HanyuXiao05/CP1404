# Question 1
out_file = open("name.txt", "w")
name = input("Enter your name: ")
out_file.write(name)
out_file.close()

# Question 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Hi", name)

# Question 3
with open('numbers.txt', 'r') as in_file:
        first_number = int(in_file.readline().strip())
        second_number = int(in_file.readline().strip())
result = first_number + second_number
print(result)

# Question 4
result = 0
with open('numbers.txt', 'r') as in_file:
        for line in in_file:
            result += int(line.strip())   
print(result)
