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
        your_db = pd.read_csv(path_to_db)

        your_db_sorted_by_weight = your_db.sort_values('File_size_bytes',
                                                       ascending=False)

        top_10_largest_files = your_db_sorted_by_weight.head(n=10)

        top_10_largest_files_dict = dict(list(zip(top_10_largest_files["File_name"], top_10_largest_files['File_size'])))

        print(f"Your database is relatively new. Here is your top-10 largest files on your hard disk:")
        print(top_10_largest_files_dict)

        return top_10_largest_files_dict

    elif is_db_relevant[0] == 0:

        path_to_db = your_collector.directory_save + "/" + str(is_db_relevant[1])
        your_db = pd.read_csv(path_to_db)

        your_db_sorted_by_weight = your_db.sort_values('File_size_bytes',
                                                       ascending=False)

        top_10_largest_files = your_db_sorted_by_weight.head(n=10)

        top_10_largest_files_dict = dict(list(zip(top_10_largest_files["File_name"], top_10_largest_files['File_size'])))



        print(f"You need to refresh your hard disk statistics!!! Here is your top-10 largest files on your hard disk:")
        print(top_10_largest_files_dict)
        return top_10_largest_files_dict

    elif is_db_relevant is None:

        print("There is no data about your hard disk")
        return None


your_top_10_largest_files = top_10_files_weight("Vanya", "/Users/karnaukhovivan/Desktop/Магистратура 2 курс", "/Users/karnaukhovivan/Desktop/dir_stat")
