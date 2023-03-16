from flask_app.config.mysqlconnection import connectToMySQL
from flask import session 
from flask_app.models.user_model import User
from flask_app import DATABASE

class Review:
    def __init__ (self,data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.bookings_id = data['booking_id']
        self.rating = data['rating']
        self.comment = data['comment']

    @classmethod
    def get_one_property_with_reviews(cls, form):
        data= {
        **form,
        'user_id' : session['uid']
        }

        query = """
        SELECT * FROM properties LEFT JOIN bookings 
        ON bookings.property_id = properties.id 
        LEFT JOIN reviews ON reviews.booking_id = bookings.id 
        WHERE properties.id = session['uid];
        """

        return connectToMySQL(DATABASE).query_db(query, data)

