#example - print odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#part a
for i in range (0, 110, 10):
    print(i, end=' ')
print()

#part b
for i in range (20, 0, -1):
    print(i, end=' ')
print()

#part c
number_of_stars = int(input("Number of Stars: "))
for i in range (0, number_of_stars, 1):
    print("*", end ='')
print()

#part d
number_of_lines = int(input("Number of Lines: "))
for i in range (0, number_of_lines + 1):
    print("*" * i)
print()
