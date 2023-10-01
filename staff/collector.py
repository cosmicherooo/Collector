import time
import os
import pandas as pd
import math
from datetime import datetime
from os.path import join, getsize


class Collector:

    num_calls = 0

    def __call__(self):
        self.num_calls += 1  # считает количество вызовов, причем задаем self., так как мы работаем с конкретным экземпляром класса


    # Функция, которая принимает путь, а по нему формирует датасет из названий файлов и их размера.
    def getting_statisitcs(needed_path = "/Users/karnaukhovivan/Desktop"):

        # функция для перевода байтов в другие размерности информации
        def convert_size(size_bytes):
            if size_bytes == 0:
                return "0B"

            size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
            i = int(math.floor(math.log(size_bytes, 1024)))
            p = math.pow(1024, i)
            s = round(size_bytes / p, 2)

            return "%s %s" % (s, size_name[i])

        list_of_paths = []
        list_of_files = []
        list_of_sizes = []
        list_of_creation = []
        list_of_modification = []

        for root, dirs, files in os.walk(needed_path):
            try:
                for fn in files:
                    path = os.path.join(root, fn)
                    size = os.stat(path).st_size
                    creation_time = os.path.getctime(path)
                    modification_time = os.path.getmtime(path)

                    list_of_files.append(fn)
                    list_of_sizes.append(size)
                    list_of_paths.append(path)
                    list_of_creation.append(time.ctime(creation_time))
                    list_of_modification.append(time.ctime(modification_time))

            except:
                print(f"{needed_path} is broken and cannot be considered")

        df_sys_files = pd.DataFrame()
        df_sys_files['File_Name'] = list_of_files
        df_sys_files['File_path'] = list_of_paths
        df_sys_files['File_size'] = list_of_sizes
        df_sys_files['Creation_time'] = list_of_creation
        df_sys_files['Modification_time'] = list_of_modification

        df_sys_files = df_sys_files.sort_values(by=['File_size'],
                                                ascending=False)

        # перевожу тут, чтобы нормально расставил по возрастанию, основываясь только на байтах
        df_sys_files['File_size'] = df_sys_files['File_size'].apply(convert_size)


        print("Database has been created")

        return df_sys_files

    # запись базы данных в формат csv
    def write_to_csv(data_base,
                     name_of_file="hard_disk_files_statisitcs.csv",
                     path_to_write='/Users/karnaukhovivan/Desktop'):


        # я тут решил объявить имя файла, чтобы потом легко получать по нему статистику (когда был создан в особенности)
        # наверное, это как-то можно держать через класс и проверять, когда он последний раз вызывался и так далее, но пока не нашел, как это сделать

        os.makedirs(path_to_write,
                    exist_ok=True)
        data_base.to_csv(path_to_write + "/" + name_of_file,
                        index=True)

        return f"Database named {name_of_file} is in the path: {path_to_write}"

    # Функция для того, чтобы искать файл, лучше вызывать без первого параметра, чтобы искал именно то, что мы назначили как имя файла со сводной статистикой в функции выше
    def find_file(name = "hard_disk_files_statisitcs.csv",
                  path = '/Users/karnaukhovivan/Desktop'):

        def convert_size(size_bytes):
            if size_bytes == 0:
                return "0B"

            size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
            i = int(math.floor(math.log(size_bytes, 1024)))
            p = math.pow(1024, i)
            s = round(size_bytes / p, 2)

            return "%s %s" % (s, size_name[i])


        for root, dirs, files in os.walk(path):
            if name in files:

                path = os.path.join(root, name)
                size = convert_size(os.stat(path).st_size)
                creation_time = os.path.getctime(path)
                modification_time = os.path.getmtime(path)

                return os.path.join(path), size, creation_time, modification_time



