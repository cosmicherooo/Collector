import sqlite3
import time
import os
import pandas as pd
import math
from datetime import datetime
from os.path import join, getsize
from staff.Collector import Collector


def num_of_files(user, directory_exp, directory_save):

    your_collector = Collector(user, directory_exp, directory_save)
    is_db_relevant = your_collector.last_database_formation()

    if is_db_relevant[0] == 1:

        path_to_db = your_collector.directory_save + "/" + str(is_db_relevant[1])

        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM files_info")
        results = cursor.fetchall()
        connection.close()

        print(f"Your database is relatively new and your hard disk contains {len(results)} files.")

        return len(results)

    elif is_db_relevant[0] == 0:

        path_to_db = your_collector.directory_save + "/" + str(is_db_relevant[1])

        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM files_info")
        results = cursor.fetchall()
        connection.close()

        print(f"Your database is relatively new and your hard disk contains {len(results)} files.")

        print(f"You need to refresh your hard disk statistics!!! However, your hard disk contains {number_of_files} files.")
        return len(results)

    elif is_db_relevant is None:

        print("There is no data about your hard disk")
        return None



print(num_of_files("Vanya", "/Users/karnaukhovivan/Desktop/3 курс", "/Users/karnaukhovivan/Desktop/dir_stat"))
