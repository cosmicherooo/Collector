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

            file_name = {"File_name": path.rsplit('/', 1)[-1]}
            path_to_file = {'File_path': path}
            size_bytes = {"File_size_bytes": os.stat(path).st_size}
            size = {"File_size": convert_size(os.stat(path).st_size)}
            creation_time = {"Creation_time": time.ctime(os.path.getctime(path))}
            modification_time = {"Modification_time": time.ctime(os.path.getmtime(path))}

            common_data = {**file_name, **path_to_file,
                           **size_bytes, **size, **creation_time,
                           **modification_time}

            return common_data

        except:
            print(f"{path} is broken and cannot be read!")
            return None
      
