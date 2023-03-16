from flask_app.config.mysqlconnection import connectToMySQL
from flask import session 
from flask_app.models.user_model import User
from flask_app.models.amenity_model import Amenity
from flask_app import DATABASE

class Property:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.location = data['location']
        self.price_per_night = data['price_per_night']
        self.number_of_bedrooms = data['number_of_bedrooms']
        self.number_of_bathrooms = data['number_of_bathrooms']
        self.maximum_occupancy = data['maximum_occupacy']
        self.created_at = data['created_at'] 
        self.updated_at = data ['updated_at']
        self.host_id = data['host_id']
        self.amenities = []
        self.property_image = []

    @classmethod
    def create(cls, form):

        data= {
            **form,
            'host_id' : session['uid']
        }

        query = """
        INSERT INTO properties
        (
            title,
            description,
            location,
            price_per_night,
            number_of_bedrooms,
            number_of_bathrooms,
            maximum_occupancy,
            host_id,
            property_image
        )

        VALUES(
            %(title)s,
            %(description)s,
            %(location)s,
            %(price_per_night)s,
            %(number_of_bedrooms)s,
            %(number_of_bathrooms)s,
            %(maximum_occupancy)s,
            %(host_id)s,
            %(property_image)s
        )
        """

        property_id =  connectToMySQL(DATABASE).query_db(query, data)
        for amenity in form["amenities"]:
            Amenity.create(property_id, amenity)
        return property_id
            

    @classmethod
    def get_all_properties_with_host(cls, form):

        data= {
            **form,
            'user_id' : session['uid']
        }

        query = """
        SELECT * FROM properties 
        JOIN users ON users.id = properties.host_id;
        """

        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_amenities(cls, form):
        # print(form)
        amenities = []
        if "wifi" in form:
            amenities.append("wifi")
        if "pool" in form:
            amenities.append("pool")
        if "gym" in form:
            amenities.append("gym")
        if "kitchen" in form:
            amenities.append("kitchen")
        if "parking" in form:
            amenities.append("parking")

        return amenities
    
    @classmethod
    def get_all_properties_with_amenities(cls, property_id):

        data = {
            "property_id" : id
        }
        
        query="""
        SELECT * FROM properties 
        JOIN amenities ON property_id = properties.host_id;
        """

        results = connectToMySQL(DATABASE).query_db(query, data)

        if results:
            return cls(results[0])
        else:
            return False
