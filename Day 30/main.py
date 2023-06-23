# FileNotFound
# with open("a_file.txt") as file:
#     file.readlines()

#KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["apple", "banana", "pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text+5)

# try, except, else, finally block

# try: # This block will test the excepted error to occur
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     # print(a_dictionary["non_existent_key"])
#     print(a_dictionary["key"])
# except FileNotFoundError: # Here you can handle the error
#     print("File not found, creating")
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exists")
# else: # If there is no exception then this block will be executed
#     content = file.read()
#     print(content)
# finally: # Finally block always gets executed either exception is generated or not
#     file.close()
#     print("File was closed.")
#     raise KeyError("My own error")


# raise keyword throws error

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
bmi = weight / height ** 2
print(bmi)