# numbers = [1,2,3]
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)

name="Kimmo"
letters_list = [letter for letter in name]
print(letters_list)

range(1,5)
range_list = [n * 2 for n in range(1,5)]
print(range_list)

# Conditional list comprehension
# numbers = [new_item for item in items if test]
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Filtering even numbers
result = [num for num in numbers if num % 2 == 0]
print(result)

# Challenge 1
names = ['Alex', "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# names if name length is smaller than 5 characters
short_names = [name for name in names if len(name) < 5]
# Uppercase name if name length is more than 5 characters
long_names = [name.upper() for name in names if len(name) > 5]
print(short_names,long_names)

str = int("42\n")
print(str)