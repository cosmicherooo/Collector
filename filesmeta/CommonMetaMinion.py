import time
import os
import pandas as pd
import math
from datetime import datetime
from os.path import join, getsize
from datetime import datetime

class CommonMetaMinion():

    ex = ['*']

    def get_meta_inf(self, path):
        try:

            common_data = {
                "File_name": path.rsplit('/', 1)[-1],
                'File_path': path,
                "File_size_bytes": os.stat(path).st_size,
                "File_size": convert_size(os.stat(path).st_size),
                "Creation_time": time.ctime(os.path.getctime(path)),
                "Modification_time": time.ctime(os.path.getmtime(path))
            }


            return common_data

        except:
            print(f"{path} is broken and cannot be read!")
            return None
      
