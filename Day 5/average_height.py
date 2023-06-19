# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
student_heights = [180, 124, 165, 173, 189, 169, 146]
total = 0
for height in student_heights:
    total += height
print(total)
print(round(total / len(student_heights)))
