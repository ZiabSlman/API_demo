from app import db
from sqlalchemy import String, Column, PrimaryKeyConstraint, Integer, Float
import os

class Users(db.Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    faculty = Column(String)
    field_of_study = Column(String)
    active_semesters = Column(Integer)
    grade_average = Column(Float)


class Subjects(db.Model):
    __tablename__ = 'Subjects'
    id = Column(Integer, primary_key=True)
    subject_name = Column(String)
    lecturer = Column(String)
    target_semester = Column(String)
    credits = Column(String)
    success_criteria = Column(Integer)


class CompletedSubjects(db.Model):
    id = Column(Integer, primary_key=True)
