import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from datetime import datetime
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

#creating flask app variable
app = Flask(__name__)

#conecting app to mongo database
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

#app variable connecting to pymongo
mongo = PyMongo(app)


#first route creation
@app.route("/")
#finds data to rener on trips page
@app.route("/find_trips")
def find_trips():
    trips = list(mongo.db.trips.find())
    return render_template("trips.html", trips=trips)


#route to search function
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    trips = list(mongo.db.trips.find({"$text": {"$search": query}}))
    return render_template("trips.html", trips=trips)



#sign up function
@app.route("/register", methods=["GET", "POST"])
def register():
    date = datetime.now()
    day = date.day
    month = date.month
    year = date.year
    date_stamp = str(day)+"-"+str(month)+"-"+str(year)
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        #logic to stop duplicate usernames
        if existing_user:
            flash("Username already used!")
            return redirect(url_for("register"))

        #dictioary for user data
        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "joined":date_stamp
        }
        #creates user database
        mongo.db.users.insert_one(register)

        #put user into session
        session["user"] = request.form.get("username")
        user = register["username"]
        flash("Welcome " + user + " to Trip Discoverer!")
        return redirect(url_for('find_trips'))
    return render_template("register.html")


#sign in function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        #logic to validate user sign in
        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome back, {}".format(request.form.get("username")))
                #directs user to trips page if successfully signed in
                return redirect(url_for('find_trips'))
            else:
                #invalid password
                flash("Username and/or Password is incorrect")
                return redirect(url_for("login"))
    
        else:
            #username does not exist
            flash("Username and/or Password is incorrect")
            return redirect(url_for("login"))
           

    return render_template("login.html")


#Sign out function
@app.route("/logout")
def logout():
    #logs out user by clearing session cookie
    flash("You have signed out!")
    session.pop("user")
    return redirect(url_for('find_trips'))


#Add trip function
@app.route("/add_trip", methods=["GET", "POST"])
def add_trip():
    #creating date variables for timestamp
    date = datetime.now()
    day = date.day
    month = date.month
    year = date.year
    date_stamp = str(day)+"-"+str(month)+"-"+str(year)
    if request.method == "POST":
        #dictionary to pass added trip data to database
        trip = {
            "category_name": request.form.get("category_name"),
            "trip_name": request.form.get("trip_name"),
            "region": request.form.get("region"),
            "city": request.form.get("city"),
            "address": request.form.get("address"),
            "post_code": request.form.get("post_code"),
            "trip_description": request.form.get("trip_description"),
            "website": request.form.get("website"),
            "trip_rating": request.form.get("trip_rating"),
            "trip_review":request.form.get("trip_review"),
            "created_by": session["user"],
            "added":date_stamp
        }
        #adds trip to database
        mongo.db.trips.insert_one(trip)
        flash("Trip Successfully Added")
        #directs ser to trips page after trip added
        return redirect(url_for("find_trips"))
    #variable to render list of categories in database on add trip temaplte form
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add-trip.html", categories=categories)
    # if session:
    #     return render_template("add-trip.html", categories=categories)


#edit function
@app.route("/edit_trip/<trip_id>", methods=["GET", "POST"])
def edit_trip(trip_id):
    if request.method == "POST":
        #creates new dictionary to pass any updated informaiton to database
        edit = {
            "category_name": request.form.get("category_name"),
            "trip_name": request.form.get("trip_name"),
            "region": request.form.get("region"),
            "city": request.form.get("city"),
            "address": request.form.get("address"),
            "post_code": request.form.get("post_code"),
            "trip_description": request.form.get("trip_description"),
            "trip_rating": request.form.get("trip_rating"),
            "trip_review":request.form.get("trip_review"),
            "created_by": session["user"]
        }
        #updates edited informaiton to database
        mongo.db.trips.update_one({"_id": ObjectId(trip_id)}, {"$set": edit})
        flash("Trip Successfully Updated")
        return redirect(url_for("find_trips"))
    trip = mongo.db.trips.find_one({"_id": ObjectId(trip_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit-trip.html", trip=trip, categories=categories)


#function to delete trip
@app.route("/delete_trip/<trip_id>")
def delete_trip(trip_id):
    mongo.db.trips.delete_one({"_id": ObjectId(trip_id)})
    flash("Trip Successfully Deleted")
    return redirect(url_for("find_trips"))


#function to list users on admin's users page
@app.route("/user_list")
def user_list():
    users = mongo.db.users.find()
    return render_template("users.html", users=users)
    # if session["user"] == "admin".lower():
    #     return render_template("users.html", users=users)



#function for admin to delete user
@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    flash("User Successfully Deleted")
    return redirect(url_for("user_list"))


#runs app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)