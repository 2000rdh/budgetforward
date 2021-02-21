from flask import Flask, render_template, redirect, url_for, request, flash, session
from keys import *
import mysql.connector
import random
from matplotlib import pyplot as plt
import numpy as np
import os

app = Flask(__name__)
print(HOSTNAME)
global nums
app.secret_key = KEY

mydb = mysql.connector.connect(
    host=HOSTNAME,
    user=USERNAME,
    password=PASSWORD,
    database=DATABASE
    )

cursor = mydb.cursor()

@app.route("/")
def home():
    return render_template("welcome.html")

@app.route("/login", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("login.html")    

@app.route("/budget", methods=['GET', 'POST'])
def budget():
    if request.method == 'GET':

        cursor.execute("SELECT * FROM [redacted]")
        myresult = cursor.fetchall()
        print(random.choice(myresult))
        return render_template("home.html")

    if request.method == 'POST':

        return render_template("home.html")

@app.route("/visual", methods=['GET', 'POST'])
def res():
    l = [0, 0, 0, 0, 0, 0, 0]
    x = 0
    while x < 7:
        cursor.execute("SELECT * FROM [redacted]")
        myresult = cursor.fetchall()
        l[x] = (random.choice(myresult))
        x+=1

    output1 = l[0]
    output2 = l[1]
    output3 = l[2]
    output4 = l[3]
    output5 = l[4]
    output6 = l[5]
    output7 = l[6]
    return render_template('vis.html', output1=output1, output2=output2, output3=output3, output4=output4, output5=output5, output6=output6, output7=output7)


# @app.route("/visual", methods=['GET','POST'])
# def visual():
#     session['rent'] = request.form['rentBillsAmount']
#     session['food'] = request.form['foodAmount']
#     session['kids'] = request.form['kidsAmount']
#     session['home'] = request.form['homeAndGiftsAmount']
#     session['fitness'] = request.form['fitnessAmount']
#     session['beauty'] = request.form['beautyAndWellnessAmount']
#     session['nums'] = [session['rent'], session['food'], session['kids'], session['home'], session['fitness'], session['beauty']]
#     data = session['nums']
#     labels = ['Rent', 'Food', 'Kids', 'Home', 'Fitness', 'Beauty']
#     fig = plt.figure(figsize =(10,7))
#     plt.pie(data, labels = labels)
#     plt.savefig('piechart.png')
#     pic = os.path('piechart.png')
#     return render_template("vis.html", user_image = pic)
   
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
