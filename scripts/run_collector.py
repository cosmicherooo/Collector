import time
import os
import pandas as pd
import math
from datetime import datetime
from os.path import join, getsize

from staff.collector import Collector
from filesmeta import Gru, CommonMetaMinion, ImageMinion, MsOfficeMinion, PdfMinion


collect_1 = Collector("Vanya", "/Users/karnaukhovivan/Desktop/3 курс", "/Users/karnaukhovivan/Desktop/dir_stat")
print(collect_1)
data_frame_test = collect_1.get_statistics()
print(data_frame_test)
collect_1.write_csv_file()
answer = collect_1.last_database_formation()
print(answer)
  
