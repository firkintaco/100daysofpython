# file = open("score.txt")
with open("score.txt") as file:
    print(file.read())

# with open("score.txt", "a") as file:
#     file.write("high_score = 12")
#     print(file.read())