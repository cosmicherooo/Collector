import time
import os
import pandas as pd
import math
from datetime import datetime
from os.path import join, getsize
import Collector

def num_of_files(your_path = '/Users/karnaukhovivan/Desktop/hard_disk_files_statisitcs.csv'):

    if Collector.find_file() is None:
        database_stat = Collector.getting_statisitcs(needed_path = "/Users/karnaukhovivan/Desktop")
        Collector.write_to_csv(database_stat)

        counted_files = database_stat.shape[0]

        print(f"There are {counted_files} files on your hardware.")

    else:

        if (time.time() - Collector.find_file()[3]) / 86400 > 2:

            print("You need to refresh the statistics of your hardware. Data might be invalid")

            database_stat = pd.read_csv(your_path)
            counted_files = database_stat.shape[0]

            print(f"There are {counted_files} files on your hardware.")

        else:

            print("Your statistics has been created less than 2 days ago")

            database_stat = pd.read_csv(your_path)
            counted_files = database_stat.shape[0]

            print(f"There are {counted_files} files on your hardware.")



    return counted_files
