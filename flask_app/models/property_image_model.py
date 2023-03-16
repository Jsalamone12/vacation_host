from flask_app.config.mysqlconnection import connectToMySQL
from flask import session 
from flask_app.models.user_model import User
from flask_app import DATABASE

class Property_image:
    def __init__ (self,data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.property_id = data['property_id']
        self.image_url = data['image_url']

    @classmethod
    def get_all_properties_with_property_images(cls, form):
        data= {
        **form,
        'user_id' : session['uid']
        }

        query = """
        SELECT * FROM properties LEFT JOIN property_images 
        ON properties.id = property_images.property_id;
        """

        return connectToMySQL(DATABASE).query_db(query, data)
