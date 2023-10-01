import time
import os
import pandas as pd
import math
from datetime import datetime
from os.path import join, getsize
import Collector


def top_10_files_weight(your_path = '/Users/karnaukhovivan/Desktop/hard_disk_files_statisitcs.csv'):

    if Collector.find_file() is None:
        database_stat = Collector.getting_statisitcs(needed_path = "/Users/karnaukhovivan/Desktop")
        Collector.write_to_csv(database_stat)

        database_stat = database_stat.head(n=10)

        print(f"Here is top-10 largest on your hard disk")
        print(database_stat)

    else:

        if (time.time() - Collector.find_file()[3]) / 86400 > 2:

            print("You need to refresh the statistics of your hardware. Data might be invalid")

            database_stat = pd.read_csv(your_path)
            database_stat = database_stat.head(n=10)

            print(f"Here is top-10 largest on your hard disk (data might be invalid)")
            print(database_stat)

        else:

            print("Your statistics has been created less than 2 days ago")

            database_stat = pd.read_csv(your_path)
            database_stat = database_stat.head(n=10)

            print(f"Here is top-10 largest on your hard disk (data might be invalid)")
            print(database_stat)



    return database_stat
