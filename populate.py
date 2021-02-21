from flask import Flask, render_template, redirect, url_for, request, flash
from keys import *
import mysql.connector
import random
import os


app = Flask(__name__)
print(HOSTNAME)

mydb = mysql.connector.connect(
    host=HOSTNAME,
    user=USERNAME,
    password=PASSWORD,
    database=DATABASE
    )

with open("www.forbes.com_external_links.txt", "r") as a_file:
  for line in a_file:

    l = "\"" + line + "\""

    # query = 'INSERT INTO AllShops (SHOP) VALUES (%s)'
    # val = (line)

    cursor = mydb.cursor()
    cursor.execute("INSERT INTO ShopsList (Shops) VALUES(%s)" % l)

    mydb.commit()