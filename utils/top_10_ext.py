import time
import os
import pandas as pd
import math
from datetime import datetime
from os.path import join, getsize
from staff.Collector import Collector



from collections import Counter
import itertools
def top_10_extensions(user, directory_exp, directory_save):


    def get_extension(path_to_a_file):
        last_part = path_to_a_file.split("/")[-1]

        if "." in last_part:
            ex = path_to_a_file.split(".")[-1]
        else:
            ex = "У файла нет расширения"

        return ex

    your_collector = Collector(user, directory_exp, directory_save)
    is_db_relevant = your_collector.last_database_formation()

    if is_db_relevant[0] == 1:

        path_to_db = your_collector.directory_save + "/" + str(is_db_relevant[1])

        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()
        cursor.execute('SELECT File_name FROM files_info')
        # cursor.execute("ALTER TABLE files_info ADD COLUMN Extension varchar(32)")
        # names = list(map(lambda x: x[0], cursor.description))
        files = [file[0] for file in cursor.execute('SELECT File_name FROM files_info')]
        connection.close()

        extensions_files = list(map(get_extension, files))
        ext_stat = Counter(extensions_files)
        ext_stat = dict(sorted(ext_stat.items(), key=lambda x: x[1], reverse=True))
        ext_stat = dict(itertools.islice(ext_stat.items(), 2))


        print(f"Your database is relatively new. Here is your top-10 extensions:")
        print(ext_stat)

        return ext_stat

    elif is_db_relevant[0] == 0:

        path_to_db = your_collector.directory_save + "/" + str(is_db_relevant[1])
        connection = sqlite3.connect(path_to_db)
        cursor = connection.cursor()
        cursor.execute('SELECT File_name FROM files_info')
        # cursor.execute("ALTER TABLE files_info ADD COLUMN Extension varchar(32)")
        # names = list(map(lambda x: x[0], cursor.description))
        files = [file[0] for file in cursor.execute('SELECT File_name FROM files_info')]
        connection.close()

        extensions_files = list(map(get_extension, files))
        ext_stat = Counter(extensions_files)
        ext_stat = dict(sorted(ext_stat.items(), key=lambda x: x[1], reverse=True))
        ext_stat = dict(itertools.islice(ext_stat.items(), 2))

        print(f"You need to refresh your hard disk statistics!!! Here is your top-10 extensions:")
        print(ext_stat)
        return ext_stat

    elif is_db_relevant is None:

        print("There is no data about your hard disk")
        return None


your_top_10_extensions = top_10_extensions("Vanya", "/Users/karnaukhovivan/Desktop/Магистратура 2 курс", "/Users/karnaukhovivan/Desktop/dir_stat")




