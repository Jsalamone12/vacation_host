from flask_app.config.mysqlconnection import connectToMySQL
from flask import session 
from flask_app.models.user_model import User
from flask_app import DATABASE

class Amenity:
    def __init__ (self,data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.property_id = data['property_id']
        self.name = data['name']

    @classmethod
    def get_all_properties_with_amenities(cls, form):
        data= {
            **form,
            'user_id' : session['uid']
        }

        query = """
         SELECT * FROM properties JOIN amentities 
         ON properties.id = amenities.property_id;
        """

        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def create(cls, property_id, name):
        data = {
            "property_id" : property_id,
            "name" : name
        }

        query = """
        INSERT INTO amenities 
        (property_id,
        name)

        VALUES(
        %(property_id)s,
        %(name)s
        )
        """
        return connectToMySQL(DATABASE).query_db(query, data)