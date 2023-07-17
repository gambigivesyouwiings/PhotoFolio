from flask import Flask, render_template, request, url_for, flash
from flask_googlemaps import GoogleMaps, Map, icons
import requests
import json
import smtplib
import os
from dotenv import load_dotenv


load_dotenv("C:/Users/User/OneDrive/Documents/environment variables/gh.txt")
map_api = os.getenv("map_api")
app = Flask(__name__)

app.config['GOOGLEMAPS_KEY'] = os.getenv("google_key")
GoogleMaps(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact_us", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        # if email != "":
        #     flash("Your message has been sent. Thank you!")
        print(email)
    return render_template("contact.html")


@app.route("/mservices")
def service():
    return render_template("services.html")


@app.route("/reception")
def gallery():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 37.4419,
                'lng': -122.1419,
                'infobox': "<b>Hello World</b>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': 37.4300,
                'lng': -122.1400,
                'infobox': "<b>Hello World from other place</b>"
            }
        ]
    )
    gmap = Map(
        identifier="gmap",
        varname="gmap",
        lat=37.4419,
        lng=-122.1419,
        markers={
            icons.dots.green: [(37.4419, -122.1419), (37.4500, -122.1350)],
            icons.dots.blue: [(37.4300, -122.1400, "Hello World")],
        },
        style="height:400px;width:600px;margin:0;",
    )

    return render_template("gallery2.html", mymap=mymap, sndmap=sndmap, gmap=gmap)


@app.route("/about_us")
def about():
    return render_template("about2.html")


@app.route("/msample")
def sample():
    return render_template("sample-inner-page.html")


@app.route("/tribe")
def single():
    return render_template("gallery-single1.html")


@app.route("/sheraton")
def single2():
    return render_template("gallery-single2.html")


if __name__ == "__main__":
    app.run()
