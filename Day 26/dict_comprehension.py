# dict = {
#     "keys": ["Test1", "Test2"],
#     "values": ["Testi3", "Testi4"]
# }
#
# new_dict = {key.upper():value for (key,value) in dict.items()}
# print(new_dict)
names = ["Alex", "Beth", "Caroline", "Reaper", "Eleanor", "Freaddie"]
import random
# Generate random scores using random.randint() and create dictionary from list above
student_scores = {student:random.randint(0,100) for student in names}
# Result: {'Alex': 98, 'Beth': 69, 'Caroline': 34, 'Reaper': 68, 'Eleanor': 7, 'Freaddie': 78}
print(student_scores)


# Conditional Dictionary Comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

# New dictionary from student_scores if score is greater than 60
passed_students = {student:score for (student,score) in student_scores.items() if score > 60}
#Result: {'Alex': 98, 'Beth': 69, 'Reaper': 68, 'Freaddie': 78}
print(passed_students)



words = ['What', 'is', 'the', 'Airspeed', 'Velocity', 'of', 'an', 'Unladen', 'Swallow?']
# result = {new_key:new_value for item in list}
word_lengths = {word:len(word) for word in words}
# Result: {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}
print(word_lengths)

# Convert weather_c temperatures to fahrenheit's using dict comprehension
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {key:(value*9/5)+32 for (key,value) in weather_c.items()}
# Result: {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}
print(weather_f)

