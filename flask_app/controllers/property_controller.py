from flask_app import app
from flask_app.models.user_model import User
from flask_app.models import property_model

from flask import render_template, request, redirect, session, flash

@app.route('/home')
def home(): 
    return render_template("vacation_rental.html")

@app.route('/')
def index():
    return redirect('/home')

@app.route('/properties')
def properties(): 
    if not 'uid' in session:
        flash('please log in first')
        return redirect('/')
        
    logged_in_user = User.find_one_by_first_name(session['uid'])

    property = property_model.Property.get_all_properties_with_amenities(id)

    return render_template("properties.html", user=logged_in_user, property = property)

@app.route('/add_property')
def add_property():
    return render_template('add_property.html')

@app.route('/create_property', methods=['POST'])
def create_property():

    property_info = {
        **request.form,
        "amenities" : property_model.Property.get_amenities(request.form)

    }
    property_model.Property.create(property_info)
    return redirect('/')

@app.route('/bookings')
def bookings(): 
    return render_template("bookings.html")

@app.route('/reviews')
def reviews(): 
    return render_template("reviews.html")

@app.route('/stripe')
def stripe(): 
    return render_template("stripe.html")

@app.route('/success')
def success(): 
    return render_template("success_payment.html")