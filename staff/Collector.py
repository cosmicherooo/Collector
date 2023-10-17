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

    def __init__(self, user, directory_exp, directory_save):

        self.user = user
        self.directory_exp = directory_exp
        self.directory_save = directory_save

    def form_csv_name(self):

        csv_name = self.user + "_" + self.time_of_creation_stand + ".csv"
        return csv_name

    def get_statistics(self):

        def convert_size(size_bytes):
            if size_bytes == 0:
                return "0B"

            size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
            i = int(math.floor(math.log(size_bytes, 1024)))
            p = math.pow(1024, i)
            s = round(size_bytes / p, 2)

            return "%s %s" % (s, size_name[i])

        check = 0
        memory_data = None

        for root, dirs, files in os.walk(self.directory_exp):
            try:
                for fn in files:

                    path = os.path.join(root, fn)
                    size = convert_size(os.stat(path).st_size)
                    creation_time = time.ctime(os.path.getctime(path))
                    modification_time = time.ctime(os.path.getmtime(path))

                    print(1)

                    data_in_cycle = [[fn,
                                      path,
                                      size,
                                      creation_time,
                                      modification_time]]

                    df_cycle = pd.DataFrame(data_in_cycle, columns=['File_Name', 'File_path',
                                                                    'File_size', 'Creation_time',
                                                                    'Modification_time'])

                    if check == 0:
                        memory_data = df_cycle


                    else:
                        memory_data = pd.concat([memory_data, df_cycle],
                                                ignore_index=True)

                    check += 1


            except:
                print(f"{path} is broken and cannot be considered")

        print("Database has been created")

        return memory_data

    def write_csv_file(self):

        os.makedirs(self.directory_save,
                    exist_ok=True)
        collect_1.get_statistics().to_csv(self.directory_save + "/" + self.form_csv_name(),
                                          index=True)

        print(f"Database named {self.form_csv_name()} is in the path: {self.directory_save}")

    def last_database_formation(self):

        list_check = os.listdir(self.directory_save)

        print(len(list_check))

        if len(list_check) != 1:

            list_check = list(map(lambda x: x.replace(str(self.user) + "_", ''), list_check))
            list_check = list(map(lambda x: x.replace('.csv', ''), list_check))
            list_check = list(map(lambda x: x.replace('.', ':'), list_check))
            list_check = list(map(lambda x: x.replace(' ', 'T'), list_check))
            list_check.remove(':DS_Store')

            list_check = list(map(lambda x: time.strptime(x, '%Y-%m-%dT%H:%M:%S'), list_check))
            list_check = list(map(lambda x: time.mktime(x), list_check))
            list_check.sort()
            latest_file = list_check[0]

            if time.time() - latest_file < 172_800:
                print(
                    f"Your hard disk stats were compiled {(time.time() - latest_file) / 86_400} days ago. It is relatively new.")

                return 1

            else:
                print(f"Your hard disk stats were compiled {(time.time() - latest_file) / 86_400} days ago. You need to refresh your database.")

                return 0



        else:
            print("There is no stats about your hard disk")
            return 0
