from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
BCRYPT = Bcrypt(app)

app.secret_key = "Brooklyn"

DATABASE = "vacation_rental_db"