#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Bauyrzhan Ospan"
__copyright__ = "Copyright 2018, KazPostBot"
__version__ = "1.0.1"
__maintainer__ = "Bauyrzhan Ospan"
__email__ = "bospan@cleverest.tech"
__status__ = "Development"

from flask import Flask, render_template, request, Markup, jsonify
import time
import random
import datetime, socket
import json


app = Flask(__name__)  # Creating new flask app
passcode = ""
timer = 30
telegram = ""

# Main functions

# Get IP as string of the host machine
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def write_json(data, name):
    with open(name, 'w') as outfile:
        json.dump(data, outfile)


def read_json(name):
    with open(name, 'r') as f:
        return json.load(f)


def init_all():
    data = read_json("./data/config.json")
    passcode = data["passcode"]
    telegram = data["telegram"]
    timer = data["timer"]


# Main page
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", **locals())
# End of main page

# Admin enter page
@app.route("/login/", methods=["GET", "POST"])
def login():
    alert = "Введите пароль"
    return render_template(
        "login.html", **locals())
# End of admin login page

# Choosing cell to load
@app.route("/robot/", methods=["GET", "POST"])
@app.route("/robot/<destination>/", methods=["GET", "POST"])
def robot(destination = None):
    alert = "Выберите ячейку"
    file = "./data/cells_ID.json"
    cell = read_json(file)

    for i in range(len(cell)):
        if cell[i] != 0:
            cell[i] = "Занято"
        else:
            cell[i] = "Свободно"

    cell0 = cell[0]
    cell1 = cell[1]
    cell2 = cell[2]
    cell3 = cell[3]

    if request.method == "POST":
        passcodenew = request.form['passcode']
        if passcode == passcodenew:
            msg = "Кто-то зашел в кабинет"
            # naboox.send_tlg_msg(msg, ids)
            return render_template(
                "robot.html", **locals())
        else:
            alert = "Вы ввели неправильный пароль"
            msg = "Кто-то пытался зайти в кабинет, используя неправильный пароль"
            # naboox.send_tlg_msg(msg, ids)
            return render_template(
                "destination.html", **locals())

    if destination:
        return render_template(
            "robot.html", **locals())


# Main flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777, debug=True)