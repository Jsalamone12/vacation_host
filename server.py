from flask_app import app
from flask_app.controllers import property_controller, user_controller 
from flask_app import BCRYPT, DATABASE






if __name__=="__main__":
    app.run(debug=True)

