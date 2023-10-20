import time
import os
import pandas as pd
import math
from datetime import datetime
from os.path import join, getsize
from datetime import datetime


class Collector:

    time_of_creation_sec = time.time()
    time_of_creation_stand = ((str(datetime.now()))[:(str(datetime.now())).rfind('.')]).replace(':', '.')

    def __init__(self, user_init, directory_exp_init, directory_save_init):

        self.user = user_init
        self.directory_exp = directory_exp_init
        self.directory_save = directory_save_init

    def form_csv_name(self):

        csv_name = self.user + "_" + self.time_of_creation_stand + ".csv"
        return csv_name

    def get_statistics(self):

        g = Gru()
        minion_ms_office = MsOfficeMinion()
        minion_image = ImageMinion()
        minion_pdf = PdfMinion()
        minion_common = CommonMetaMinion()
        minion_list_ext = [minion_ms_office, minion_image,
                           minion_pdf, minion_common]

        for minion in minion_list_ext:
            g.add_minion(minion)

        check = 0

        memory_data = None

        for root, dirs, files in os.walk(self.directory_exp):
            try:
                for fn in files:

                    path = os.path.join(root, fn)
                    print(path)

                    metadata_dict = g.get_meta_inf(path)
                    print(metadata_dict)

                    df_cycle_metadata = pd.DataFrame.from_dict(metadata_dict)

                    print(df_cycle_metadata)

                    if check == 0:
                        memory_data = df_cycle_metadata

                    else:

                        print(memory_data)

                        memory_data = pd.concat([memory_data, df_cycle_metadata],
                                                axis=0)

                    check += 1


            except:
                print(f"{path} is broken and cannot be considered")

        print("Database has been created")

        return memory_data

    def write_csv_file(self):

        os.makedirs(self.directory_save,
                    exist_ok=True)


        self.get_statistics().to_csv(self.directory_save + "/" + self.form_csv_name(),
                                     index=True)

        print(f"Database named {self.form_csv_name()} is in the path: {self.directory_save}")

    def last_database_formation(self):

        list_check_names = os.listdir(self.directory_save)

        # Только сейчас понял, что можно не доставать время создания файла из названия, а просто брать из метаданных файла... Но пусть тут будет, потом переделаю.
        # Через коленку получилось, но тем не менее забавное решение, по-моему...
        if len(list_check_names) > 1:

            list_check = list(map(lambda x: x.replace(str(self.user) + "_", ''), list_check_names))
            list_check = list(map(lambda x: x.replace('.csv', ''), list_check))
            list_check = list(map(lambda x: x.replace('.', ':'), list_check))
            list_check = list(map(lambda x: x.replace(' ', 'T'), list_check))
            list_check.remove(':DS_Store')

            list_check = list(map(lambda x: time.strptime(x, '%Y-%m-%dT%H:%M:%S'), list_check))
            list_check = list(map(lambda x: time.mktime(x), list_check))
            list_check.sort()
            latest_file = list_check[len(list_check) - 1]

            if time.time() - latest_file < 172_800:
                print(
                    f"Your hard disk stats were compiled {(time.time() - latest_file) / 86_400} days ago. It is relatively new.")

                func_return_pos = [1, list_check_names[len(list_check_names) - 1]]

                return func_return_pos

            else:
                print(f"Your hard disk stats were compiled {(time.time() - latest_file) / 86_400} days ago. You need to refresh your database.")

                func_return_neg = [0, list_check_names[len(list_check_names) - 1]]

                return func_return_neg



        else:
            print("There is no stats about your hard disk")
            return None
