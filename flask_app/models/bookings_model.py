from flask_app.config.mysqlconnection import connectToMySQL
from flask import session 
from flask_app.models.user_model import User
from flask_app import DATABASE

class Booking:
    def __init__ (self, data):
        self.id = data['id']
        self.created_at = data['created_at'] 
        self.updated_at = data['updated_at']
        self.guest_id = data['guest_id']
        self.property_id = data['property_id']
        self.check_in = data['check_in']
        self.check_out = data['check_out']
        self.number_of_guest = data['number_of_guest']
        self.total_price = data['total_price']
        self.status = data['status']

        
    @classmethod
    def get_one_guest_with_bookings(cls, form):
        data= {
        **form,
        'user_id' : session['uid']
        }

        query = """
        SELECT * FROM users LEFT JOIN bookings 
        ON bookings.guest_id = users.id 
        LEFT JOIN reviews  
        ON reviews.booking_id = bookings.id WHERE users.id = session['uid];
        """

        return connectToMySQL(DATABASE).query_db(query, data)