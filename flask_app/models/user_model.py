from flask_app.config.mysqlconnection import connectToMySQL
from flask import session, flash
from flask_app import DATABASE, BCRYPT
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
USERNAME_REGEX = re.compile(r'^[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.password = data['password']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.user_role = data['user_role']
        self.phone_number = data['phone_number']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, form):


        data = {
          **form,
            'password' : BCRYPT.generate_password_hash(form['password'])
        }

        query = """
        INSERT INTO users (
        email,
        password,
        first_name,
        last_name,
        phone_number,
        user_role
        )
        VALUES (
        %(email)s,
        %(password)s,
        %(first_name)s,
        %(last_name)s,
        %(phone_number)s,
        %(user_role)s
        );
        """

        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def find_one_by_email(cls, email):

        data = {
            'email' : email
        }

        query = """
        SELECT * FROM users 
        WHERE email  = %(email)s
        """

        results = connectToMySQL(DATABASE).query_db(query, data)

        if results:
            return cls(results[0])
        else:
            return False


    @staticmethod
    def validate_login(form):
        is_valid = True

        found_user = User.find_one_by_email(form['email'])
        print(found_user)
        if not found_user:
            is_valid = False
            flash("invalid login")
            print("inside found user conditional")
        elif not BCRYPT.check_password_hash(found_user.password, form['password']):
            is_valid = False 
            flash('invalid login')
            print("inside password conditional")
        return is_valid
    
    @staticmethod
    def validate(data):
        is_valid = True
        
        if len(data['first_name']) < 2:
            flash("first name is too short!")
            is_valid = False

        if not USERNAME_REGEX.match(data['first_name']):
            flash("must be letters!")
            is_valid = False

        if len(data['last_name']) < 2:
            flash("last name is too short!")
            is_valid = False

        if not USERNAME_REGEX.match(data['last_name']):
            flash("must be letters!")
            is_valid = False

        if not EMAIL_REGEX.match(data['email']):
            flash("not a vaild email address")
            is_valid = False

        if User.find_one_by_email(data['email']):
            flash('Email already registered')
            is_valid = False

        if len(data['password']) < 8:
            flash("password must be at least 8 characters")
            is_valid = False

        if data ['password'] != data['confirm_password']: 
            flash("Your passwords dont match")
            is_valid = False

        

        # if not(data['password']) < 3:  need to have contain ! and number
        #     flash("Username is too short!")
        #     is_valid = False
        
        return is_valid 
    
    @classmethod
    def find_one_by_first_name(cls, first_name):
        data = {
            'first_name' : first_name
        }

        query = """
        SELECT * FROM users 
        WHERE first_name  = %(first_name)s
        """

        results = connectToMySQL(DATABASE).query_db(query, data)

        if results:
            return cls(results[0])
        else:
            return False

