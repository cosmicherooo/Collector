import time
import os
import pandas as pd
import math
from datetime import datetime
from os.path import join, getsize

from staff.collector import Collector

def main(): 

  harddisk_stat = Collector.getting_statisitcs()
  write_to_csv(harddisk_stat)

if __name__ == "__main__":
    main()
  
