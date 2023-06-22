with open("./file1.txt") as file1:
    num1 = file1.readlines()

with open("./file2.txt") as file2:
    num2 = file2.readlines()

numbers1 = [int(num) for num in num1]
numbers2 = [int(num) for num in num2]

result = [number for number in numbers1 if number in numbers2]
print(result)