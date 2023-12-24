import time
import os
import pandas as pd
import math
from datetime import datetime
from os.path import join, getsize
from staff.Collector import Collector


def top_10_files_weight(user, directory_exp, directory_save):


    your_collector = Collector(user, directory_exp, directory_save)
    is_db_relevant = your_collector.last_database_formation()

    if is_db_relevant[0] == 1:

        path_to_db = your_collector.directory_save + "/" + str(is_db_relevant[1])

        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()
        cursor.execute("SELECT File_name, File_size FROM files_info ORDER BY File_size_bytes DESC LIMIT 10")

        dict_files = {}

        for row in cursor.fetchmany(10):
            dict_files[str(row[0])] = str(row[1])

        connection.close()


        print(f"Your database is relatively new. Here is your top-10 largest files on your hard disk:")
        print(dict_files)

        return dict_files

    elif is_db_relevant[0] == 0:

        path_to_db = your_collector.directory_save + "/" + str(is_db_relevant[1])

        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()
        cursor.execute("SELECT File_name, File_size FROM files_info ORDER BY File_size_bytes DESC LIMIT 10")

        dict_files = {}

        for row in cursor.fetchmany(10):
            dict_files[str(row[0])] = str(row[1])

        connection.close()



        print(f"You need to refresh your hard disk statistics!!! Here is your top-10 largest files on your hard disk:")
        print(dict_files)
        return dict_files

    elif is_db_relevant is None:

        print("There is no data about your hard disk")
        return None


your_top_10_largest_files = top_10_files_weight("Vanya", "/Users/karnaukhovivan/Desktop/Магистратура 2 курс", "/Users/karnaukhovivan/Desktop/dir_stat")
