#1
name = input("Please type name: ")
out_file = open(f"{name}.txt", "w")
out_file.write(name)
out_file.close()

#2
out_file = open(f"{name}.txt", "r")
content = out_file.read()
print(f"Hello {content}!")

#3
in_file = open("numbers.txt", "r")
line_1 = int(in_file.readline())
line_2 = int(in_file.readline())
print(f"sum of first two values is: {line_1 + line_2}")
in_file.close()

#4
with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        total += int(line)
print(f"Sum of all values is {total}")