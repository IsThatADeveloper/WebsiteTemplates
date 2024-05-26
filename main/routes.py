import os
import secrets
from PIL import Image
from flask import Flask, render_template, url_for, flash, redirect, request, abort
from main import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

from main import app
import sqlite3
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
def book_appointment():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        datetime_str = request.form['datetime']
        datetime_obj = datetime.fromisoformat(datetime_str)
        date = datetime_obj.strftime('%Y-%m-%d')
        time = datetime_obj.strftime('%H:%M:%S')

        conn = sqlite3.connect('appointments.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO appointments (firstname, lastname, email, date, time)
                          VALUES (?, ?, ?, ?, ?)''', (firstname, lastname, email, date, time))
        conn.commit()
        conn.close()
        return redirect(url_for('book_appointment'))

    return render_template('mainpage.html')


    
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/test")
def test():
    return render_template('test.html', title='Test')



@app.route("/header_centerbar")
def header_centerbar():
    return render_template('/headers/header_centerbar.html', title='header_centerbar')

@app.route("/header_leftbar")
def header_leftbar():
    return render_template('/headers/header_leftbar.html', title='header_leftbar')

@app.route("/header_rightbar")
def header_rightbar():
    return render_template('/headers/header_rightbar.html', title='header_rightbar')



@app.route("/fullpage_footer")
def fullpage_footer():
    return render_template('/footers/fullpage_footer.html', title='fullpage_footer')

@app.route("/hardcoded_footer")
def hardcoded_footer():
    return render_template('/footers/hardcoded_footer.html', title='hardcoded_footer')

@app.route("/listed_footer")
def listed_footer():
    return render_template('/footers/listed_footer.html', title='listed_footer')


@app.route("/mainpage")
def mainpage():
    return render_template('mainpage.html', title='mainpage')

@app.route("/background_change")
def background_change():
    return render_template('/mainpages/background_change.html', title='background_change')

@app.route("/colour_change")
def colour_change():
    return render_template('/mainpages/colour_change.html', title='colour_change')

@app.route("/sidepages")
def sidepages():
    return render_template('/mainpages/sidepages.html', title='SidePages')


@app.route("/wave")
def wave():
    return render_template('/cards/wave.html', title='wave')

@app.route("/dental_preference")
def dental_preference():
    return render_template('/cards/dental_preference.html', title='dental_preference')


@app.route("/register1")
def register1():
    return render_template('/register/register1.html', title='register1')

@app.route("/login1")
def login1():
    return render_template('/login/login1.html', title='login1')

@app.route("/flip")
def flip():
    return render_template('/login/flip.html', title='flip')


@app.route("/banner")
def banner():
    return render_template('/banners/banner.html', title='Banner')