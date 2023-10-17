import time
import os
import pandas as pd
import math
from datetime import datetime
from os.path import join, getsize
from staff.Collector import Collector



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
        your_db = pd.read_csv(path_to_db)
        your_db['File_extension'] = your_db['File_path'].apply(get_extension)
        df_extensions_overall = your_db['File_extension'].value_counts()

        df_extensions_overall_top_10 = df_extensions_overall.head(n=10)

        print(f"Your database is relatively new. Here is your top-10 extensions:")
        print(df_extensions_overall_top_10)

        return df_extensions_overall_top_10

    elif is_db_relevant[0] == 0:

        path_to_db = your_collector.directory_save + "/" + str(is_db_relevant[1])
        your_db = pd.read_csv(path_to_db)
        your_db['File_extension'] = your_db['File_path'].apply(get_extension)
        df_extensions_overall = your_db['File_extension'].value_counts()

        df_extensions_overall_top_10 = df_extensions_overall.head(n=10)

        print(f"You need to refresh your hard disk statistics!!! Here is your top-10 extensions:")
        print(df_extensions_overall_top_10)
        return df_extensions_overall_top_10

    elif is_db_relevant is None:

        print("There is no data about your hard disk")
        return None


your_top_10_extensions = top_10_extensions("Vanya", "/Users/karnaukhovivan/Desktop/Магистратура 2 курс", "/Users/karnaukhovivan/Desktop/dir_stat")




