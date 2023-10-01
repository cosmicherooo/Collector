import time
import os
import pandas as pd
import math
from datetime import datetime
from os.path import join, getsize
import Collector



def top_10_files_weight(your_path = '/Users/karnaukhovivan/Desktop/hard_disk_files_statisitcs.csv'):

    def get_extension(path_to_a_file):
        last_part = path_to_a_file.split("/")[-1]

        if "." in last_part:
            ex = path_to_a_file.split(".")[-1]
        else:
            ex = "У файла нет расширения"

        return ex

    if Collector.find_file() is None:
        database_stat = Collector.getting_statisitcs(needed_path = "/Users/karnaukhovivan/Desktop")
        Collector.write_to_csv(database_stat)

        database_stat['File_extension'] = database_stat['File_path'].apply(get_extension)
        df_extensions_overall = database_stat['File_extension'].value_counts()

        df_extensions_overall_top_10 = df_extensions_overall.head(n=10)

        print(df_extensions_overall_top_10)

        print(f"Here is top-10 extensions on your hard disk")
        print(database_stat)

    else:

        if (time.time() - Collector.find_file()[3]) / 86400 > 2:

            print("You need to refresh the statistics of your hardware. Data might be invalid")

            database_stat = pd.read_csv(your_path)
            database_stat['File_extension'] = database_stat['File_path'].apply(get_extension)
            df_extensions_overall = database_stat['File_extension'].value_counts()

            df_extensions_overall_top_10 = df_extensions_overall.head(n=10)

            print(f"Here is top-10 extensions on your hard disk")
            print(df_extensions_overall_top_10)

        else:

            print("Your statistics has been created less than 2 days ago")

            database_stat = pd.read_csv(your_path)
            database_stat['File_extension'] = database_stat['File_path'].apply(get_extension)
            df_extensions_overall = database_stat['File_extension'].value_counts()

            df_extensions_overall_top_10 = df_extensions_overall.head(n=10)

            print(f"Here is top-10 extensions on your hard disk")
            print(df_extensions_overall_top_10)





    return database_stat





