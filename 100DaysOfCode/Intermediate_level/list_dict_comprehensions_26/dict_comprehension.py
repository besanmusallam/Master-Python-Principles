import random
import pandas as pd


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score >= 50}
print(passed_students)

student_df = pd.DataFrame(pd.Series(students_scores), columns=['Score'])
student_df.index.name = 'Student'
student_df.reset_index(inplace=True)
print(student_df)

for (index, row) in student_df.iterrows():
    print(row.Score)

