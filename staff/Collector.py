import time
import os
import pandas as pd
import math
from datetime import datetime
from os.path import join, getsize
from datetime import datetime
import sqlite3

class Collector:

    time_of_creation_sec = time.time()
    time_of_creation_stand = ((str(datetime.now()))[:(str(datetime.now())).rfind('.')]).replace(':', '.')

    def __init__(self, user_init, directory_exp_init, directory_save_init):

        self.user = user_init
        self.directory_exp = directory_exp_init
        self.directory_save = directory_save_init

    def form_sqlite_path(self):

        sqlite_name = self.user + "_" + self.time_of_creation_stand + ".db"
        sqlite_path = self.directory_save + "/" + sqlite_name

        return sqlite_path

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

        sqlite_path = self.form_sqlite_path()

        def db_insert(f):

            def wrapper(*args, **kwargs):
                connection = sqlite3.connect(sqlite_path)
                cursor = connection.cursor()

                cursor.execute('''
                CREATE TABLE IF NOT EXISTS files_info (
                File_name TEXT,
                File_path TEXT,
                File_size_bytes INTEGER,
                File_size INTEGER, 
                Creation_time TEXT,
                Modification_time TEXT,
                Title TEXT,
                Author TEXT, 
                Pages TEXT,
                category TEXT,
                comments TEXT,
                content_status TEXT,
                indetifier TEXT,
                keywords TEXT, 
                language TEXT, 
                last_modified_by TEXT,
                last_printed TEXT,
                modified TEXT,
                revision REAL,
                subject TEXT,
                version REAL,
                Image_height REAL,
                Image_width REAL,
                Image_format TEXT,
                Image_mode TEXT,
                Image_is_animated TEXT,
                Frames_in_image REAL
                )
                ''')

                dict_meta = f(*args, **kwargs)
                columns = ', '.join(dict_meta.keys())
                placeholders = ':' + ', :'.join(dict_meta.keys())
                cursor.execute('INSERT INTO files_info (%s) VALUES (%s)' % (columns, placeholders), dict_meta)
                connection.commit()
                connection.close()

            return wrapper

        @db_insert
        def meta_inf(path_1):

            metadata_dict_1 = g.get_meta_inf(path_1)

            return metadata_dict_1

        def file_iter():
            for root, dirs, files in os.walk(self.directory_exp):
                try:
                    for fn in files:
                        
                        if fn.startswith("."):
                            pass
                            
                        yield os.path.join(root, fn)

                except GeneratorExit:
                    print("Need to do some clean up.")
                    return



                #except:
                    #print(f"{os.path.join(root, fn)} is broken and cannot be considered")

        for file in file_iter():
            try:
                meta_inf(file)

            except:
                print(f"{file} is broken and cannot be considered")



    def last_database_formation(self):

        list_check_names = os.listdir(self.directory_save)
        list_check_names.sort()

        # Только сейчас понял, что можно не доставать время создания файла из названия, а просто брать из метаданных файла... Но пусть тут будет, потом переделаю.
        # Через коленку получилось, но тем не менее забавное решение, по-моему...
        if len(list_check_names) > 1:

            list_check = list(map(lambda x: x.replace(str(self.user) + "_", ''), list_check_names))
            list_check = list(map(lambda x: x.replace('.db', ''), list_check))
            list_check = list(map(lambda x: x.replace('.', ':'), list_check))
            list_check = list(map(lambda x: x.replace(' ', 'T'), list_check))
            list_check.remove(':DS_Store')
            print(list_check)

            list_check = list(map(lambda x: time.strptime(x, '%Y-%m-%dT%H:%M:%S'), list_check))
            list_check = list(map(lambda x: time.mktime(x), list_check))
            list_check.sort()
            latest_file = list_check[len(list_check) - 1]

            if time.time() - latest_file < 172_800:
                print(
                    f"Your hard disk stats were compiled {(time.time() - latest_file) / 86_400} days ago. It is relatively new.")


                func_return_pos = [1, list_check_names[len(list_check_names) - 1]]

                print(func_return_pos)

                return func_return_pos

            else:
                print(
                    f"Your hard disk stats were compiled {(time.time() - latest_file) / 86_400} days ago. You need to refresh your database.")

                func_return_neg = [0, list_check_names[len(list_check_names) - 1]]

                return func_return_neg

        print("Database has been created")
