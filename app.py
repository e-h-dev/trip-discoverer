import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/find_trips")
def find_trips():
    trips = mongo.db.trips.find()
    return render_template("trips.html", trips=trips)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        

        if existing_user:
            flash("Username used!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        #put user into session
        session["user"] = request.form.get("username")
        user = register["username"]
        flash("Welcome " + user + " to Trip Discoverer! You have Successfully Registered")
        return redirect(url_for('find_trips'))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
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


@app.route("/logout")
def logout():
    #logs out user by clearing session cookie
    flash("You have logged out!")
    session.pop("user")
    return redirect(url_for('find_trips'))


@app.route("/add_trip", methods=["GET", "POST"])
def add_trip():
    if request.method == "POST":
        trip = {
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
        mongo.db.trips.insert_one(trip)
        flash("Trip Added")
        return redirect(url_for("find_trips"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add-trip.html", categories=categories)


@app.route("/edit_trip/<trip_id>", methods=["GET", "POST"])
def edit_trip(trip_id):
    if request.method == "POST":
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
        mongo.db.trips.update_one({"_id": ObjectId(trip_id)}, {"$set": edit})
        flash("Trip successfully updated")
        return redirect(url_for("find_trips"))
    trip = mongo.db.trips.find_one({"_id": ObjectId(trip_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit-trip.html", trip=trip, categories=categories)


@app.route("/delete_trip/<trip_id>")
def delete_trip(trip_id):
    mongo.db.trips.delete_one({"_id": ObjectId(trip_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("find_trips"))


@app.route("/user_list")
def user_list():
    users = mongo.db.users.find()
    trips = mongo.db.trips.find()
    return render_template("users.html", users=users, trips=trips)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)