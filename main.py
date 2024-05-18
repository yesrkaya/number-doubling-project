
numbers = [1, 2, 3, 4, 5]

with open('numbers.txt', 'w') as file:
    for number in numbers:
        file.write(f"{number}\n")

doubled_numbers = []
with open('numbers.txt', 'r') as file:
    for line in file:
        number = int(line.strip())
        doubled_numbers.append(number * 2)

with open('doubled_numbers.txt', 'w') as file:
    for number in doubled_numbers:
        file.write(f"{number}\n")

sum_of_doubled_numbers = sum(doubled_numbers)

print(f"Doubled Numbers: {doubled_numbers}")
print(f"Sum of Doubled Numbers: {sum_of_doubled_numbers}")
