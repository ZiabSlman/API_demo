import model
import pandas
from extensions import app, db


def create_students_seeds():
    students_db = pandas.read_csv('data/Students.csv')
    students = students_db.to_dict(orient='records')
    user_1 = model.Users(**students[0])
    user_2 = model.Users(**students[1])
    user_3 = model.Users(**students[2])
    return [user_1, user_2, user_3]


def create_subjects_seeds():
    subjects_db = pandas.read_csv('data/Subjects.csv')
    subjects = subjects_db.to_dict(orient='records')
    subject_1 = model.Subjects(**subjects[0])
    subject_2 = model.Subjects(**subjects[1])
    subject_3 = model.Subjects(**subjects[2])
    return [subject_1, subject_2, subject_3]


@app.cli.command('create_db')
def create_db():
    db.create_all()
    print('database created successfully')


@app.cli.command('drop_db')
def drop_db():
    db.drop_all()
    print('database dropped successfully')


@app.cli.command('seed_db')
def seed_db():
    students: list = create_students_seeds()
    subjects: list = create_subjects_seeds()
    db.session.add_all(students)
    print('students were added to the session successfully')
    db.session.add_all(subjects)
    print('subjects were added to the session successfully')
    db.session.commit()
    print('session committed successfully!')
