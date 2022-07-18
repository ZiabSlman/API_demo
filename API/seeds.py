import model
import pandas

students_db = pandas.read_csv('Students.csv')
students = students_db.to_dict(orient='records')
user_1 = model.Users(**students[0])
user_2 = model.users(**students[1])
user_3 = model.Users(**students[2])

