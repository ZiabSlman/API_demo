import model
import pandas

students_db = pandas.read_csv('data/Students.csv')
students = students_db.to_dict(orient='records')
user_1 = model.Users(**students[0])
user_2 = model.Users(**students[1])
user_3 = model.Users(**students[2])

subjects_db = pandas.read_csv('data/Subjects.csv')
subjects = subjects_db.to_dict(orient='records')
subject_1 = model.Subjects(**subjects[0])
subject_2 = model.Subjects(**subjects[1])
subject_3 = model.Subjects(**subjects[2])