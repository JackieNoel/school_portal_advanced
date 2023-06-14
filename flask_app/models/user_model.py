from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.classroom_model import Class
from flask_app.models.enrollment_model import Enrollment
import pprint
import re

email_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


db = 'student_portal'


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.current_grade = data['current_grade']
        self.role = data['role']
        self.email = data['email']
        self.password = data['password']
        self.classes = []

    @classmethod
    def save(query, data):
        query = 'INSERT INTO users(first_name, last_name, current_grade, role, email, password) VALUES(%(first_name)s, %(last_name)s, %(current_grade)s, %(role)s, %(email)s, %(password)s)'
        return connectToMySQL(db).query_db(query, data)