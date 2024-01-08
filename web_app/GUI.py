import sys
import os
import math
import time
import pytz
from datetime import datetime

import tkinter as tk
from tkinter import *

from utils.num_of_flies import num_of_flies
from utils.top_10_ext import top_10_extensions
from utils.top_10_files_weight import top_10_files_weight

collect_1 = Collector("Vanya", "/Users/karnaukhovivan/Desktop/3 курс", "/Users/karnaukhovivan/Desktop/dir_stat")
path_to_db = collect_1.directory_save + "/" + collect_1.last_database_formation()[1]
num_of_files_db = num_of_files("Vanya", "/Users/karnaukhovivan/Desktop/3 курс", "/Users/karnaukhovivan/Desktop/dir_stat")
your_top_10_extensions = top_10_extensions("Vanya", "/Users/karnaukhovivan/Desktop/Магистратура 2 курс", "/Users/karnaukhovivan/Desktop/dir_stat")
your_top_10_largest_files = top_10_files_weight("Vanya", "/Users/karnaukhovivan/Desktop/3 курс", "/Users/karnaukhovivan/Desktop/dir_stat")


is_db_relevant = collect_1.last_database_formation()[2]
dtobject = datetime.fromtimestamp(is_db_relevant, pytz.utc)
localtz = pytz.timezone('Europe/Moscow')
localdt_db_formation = dtobject.astimezone(localtz)
time_of_db_index = f"Ваша база данных была создана: {localdt_db_formation}."
files_in_system = f"В вашей системе {num_of_files_db} файлов."



root = Tk()
root.title("Статистика вашего жесткого диска")
photo = tk.PhotoImage(file='fun.png')
root.iconphoto(False, photo)
root.config(bg="#DFC8C8")
root.config()
root.resizable(True, True)
root.minsize(100, 200)
root.maxsize(1000, 1200)
root.geometry(f"500x600+100+200")


myLabel1 = Label(root,
                 text="Статистика по вашему жетскому диску",
                 bg="#DFC8C8",
                 font=('Arial', 15, 'bold'))
myLabel2 = Label(root,
                 text=files_in_system,
                 bg="#DFC8C8")
myLabel3 = Label(root,
                 text=time_of_db_index,
                 bg="#DFC8C8")


def quit():
    label = tk.Label(root, text='new')
    label.grid(row=4, column=0)

button_quit = Button(root,
                 text="Quit",
                 command=root.destroy)


def top_10_ext_tk():
   top_10_ext_print = [f"{extension} - {your_top_10_extensions[extension]}" for extension in your_top_10_extensions]

   to_print = "\n\n".join(top_10_ext_print)
   res_wind = tk.Toplevel(root)
   res_wind.title("Top 10 Extensions")

   text_widg = Text(res_wind, wrap=tk.WORD)
   text_widg.insert(tk.END, to_print)
   text_widg.pack(expand=True, fill=tk.BOTH)

def top_10_files_tk():

    top_10_files_print = [f"{size} - {your_top_10_largest_files[size]}" for size in your_top_10_largest_files]

    to_print = "\n\n".join(top_10_files_print)
    res_wind = tk.Toplevel(root)
    res_wind.title("Top-10 Extensions")

    text_widg = Text(res_wind, wrap=tk.WORD)
    text_widg.insert(tk.END, to_print)
    text_widg.pack(expand=True, fill=tk.BOTH)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Top-10 Extensions", command=top_10_ext_tk)
filemenu.add_command(label="Top-10 Files Weight", command=top_10_files_tk)


filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Dataset Info", menu=filemenu)



button_quit.grid(row=0, column=1)
myLabel1.grid(row=1, column=0)
myLabel2.grid(row=2, column=0)
myLabel3.grid(row=3, column=0)
root.config(menu=menubar)

if __name__ == "__main__":
    root.mainloop()
