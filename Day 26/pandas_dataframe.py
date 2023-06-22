import pandas

student_dict = {
    "student": ["Karpo", "Hannu", "Pekka"],
    "score": [56, 86, 21]
}

data = pandas.DataFrame(student_dict) # Creating DataFrame from dictionary
#   student  score
# 0   Karpo     56
# 1   Hannu     86
# 2   Pekka     21

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key, value)
    # student['Karpo', 'Hannu', 'Pekka']
    # score[56, 86, 21]

# Looping through DataFrame:
# for (key, value) in data.items():
    # print(key)
    # student
    # score
    # print(value)
    # 0    Karpo
    # 1    Hannu
    # 2    Pekka
    # Name: student, dtype: object
    # 0    56
    # 1    86
    # 2    21
    # Name: score, dtype: int64

# Loop through rows of a data frame
for (index, row) in data.iterrows():
    print(row.student)
    # student    Karpo
    # score         56
    # Name: 0, dtype: object
    # student    Hannu
    # score         86
    # Name: 1, dtype: object
    # student    Pekka
    # score         21
    # Name: 2, dtype: object