for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')

# b. count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')

# c. print n stars. Ask the user for a number, then print that many stars (*), all on one line.
stars_num = int(input("Number of stars: "))
for i in range(stars_num):
    print('*', end=' ')
    
# d. print n lines of increasing stars
for i in range(stars_num+1):
    print('*'*i)