import time
import os
import pandas as pd
import math
from datetime import datetime
from os.path import join, getsize
from datetime import datetime

class CommonMetaMinion:

    ex = ['*']



    def get_meta_inf(self, path):

        def convert_size(size_bytes):
            if size_bytes == 0:
                return "0B"

            size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
            i = int(math.floor(math.log(size_bytes, 1024)))
            p = math.pow(1024, i)
            s = round(size_bytes / p, 2)

            return "%s %s" % (s, size_name[i])


        try:

            common_data = {
                "File_name": [path.rsplit('/', 1)[-1]],
                'File_path': [path],
                "File_size_bytes": [os.stat(path).st_size],
                "File_size": [convert_size(os.stat(path).st_size)],
                "Creation_time": [time.ctime(os.path.getctime(path))],
                "Modification_time": [time.ctime(os.path.getmtime(path))]
            }

            print(common_data)
            return common_data

        except:
            print(f"{path} is broken and cannot be read!")
            return None

        except:
            print(f"{path} is broken and cannot be read!")
            return None
      
