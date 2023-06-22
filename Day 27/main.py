# Unlimited argumentes
# def add(*args):
#     for arg in args:
#         print(arg)
def add(*args):
    print(args) # tuple (1,2,3,4)
    print(args[0]) # you can also access tuple by index
    sum = 0
    for n in args:
        sum += n
# Return: 10
add(1,2,3,4)


########################################
# Many keyworded arguments
def calculate(**kwargs):
    print(kwargs) # dictionary {'add': 3, 'multiply': 5}
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    print(kwargs["add"]) # Returns 3



calculate(add=3, multiply=5)