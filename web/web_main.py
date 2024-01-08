import sqlite3
import time
import math
from datetime import datetime
from os.path import join, getsize
from staff.Collector import Collector
from utils.num_of_flies import num_of_flies
from utils.top_10_ext import top_10_extensions
from utils.top_10_files_weight import top_10_files_weight
import sys
import os
from flask import Flask, render_template, url_for
import time
import pytz
import datetime as dt

collect_1 = Collector("Vanya", "/Users/karnaukhovivan/Desktop/3 курс", "/Users/karnaukhovivan/Desktop/dir_stat")
path_to_db = collect_1.directory_save + "/" + collect_1.last_database_formation()[1]
num_of_files_db = num_of_files("Vanya", "/Users/karnaukhovivan/Desktop/3 курс", "/Users/karnaukhovivan/Desktop/dir_stat")
your_top_10_extensions = top_10_extensions("Vanya", "/Users/karnaukhovivan/Desktop/Магистратура 2 курс", "/Users/karnaukhovivan/Desktop/dir_stat")
your_top_10_largest_files = top_10_files_weight("Vanya", "/Users/karnaukhovivan/Desktop/3 курс", "/Users/karnaukhovivan/Desktop/dir_stat")
app = Flask(__name__)


@app.route("/")
@app.route('/home')
def index():
    is_db_relevant = collect_1.last_database_formation()[2]
    dtobject = datetime.fromtimestamp(is_db_relevant, pytz.utc)
    localtz = pytz.timezone('Europe/Moscow')
    localdt_db_formation = dtobject.astimezone(localtz)
    return render_template("index.html",
                           indexing_base = localdt_db_formation,
                           num_files = num_of_files_db)




@app.route("/extensions")
def about():
    top_10_ext = your_top_10_extensions

    return render_template("extensions.html",
                           top_10_ext = top_10_ext)

@app.route("/top_10_files")
def weight():
    top_weights = your_top_10_largest_files
    return render_template("top_10_weight.html",
                           top_10_files = top_weights)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
