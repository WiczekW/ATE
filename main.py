import tkinter as tk
import glob
import os
from tabulate import tabulate
from tkinter import filedialog
from ABS_analyzer import mass_to_dict

# console settings
cmd = 'mode 170, 100'
os.system(cmd)


# main data

abs_to_analyze = []
result_update = []

# main window
root = tk.Tk()
root.title('Simple ABS calculator')
root.geometry('300x25')

# functions


# segregating results
def view_result():
    global abs_to_analyze, result_update
    for i in abs_to_analyze:
        result_update.append(mass_to_dict(str(i)))

    for i in result_update:
        path_to_abs = i['name']
        path_to_folder = i['name']
        while path_to_folder[-1] != '\\':
            path_to_folder = path_to_folder[:-1]
        path_to_abs = path_to_abs.replace(path_to_folder, '')
        i['name'] = path_to_abs
    print(tabulate(result_update, headers="keys"))
    abs_to_analyze.clear()
    result_update.clear()
    pass


# searching abs files in folder
def search_abs():
    global abs_to_analyze
    abs_to_analyze.clear()
    folder_selected = filedialog.askdirectory()
    key_abs_files = folder_selected + '/*.abs'
    key_abs_files = key_abs_files.replace('/', '\\')
    abs_list = glob.glob(key_abs_files)
    abs_to_analyze = abs_list
    pass


# widget definition
button_one = tk.Button(root, text='Search folder', command=search_abs)
button_two = tk.Button(root, text='Calculate', command=view_result)

# widget location
button_one.grid(column=1, row=1)
button_two.grid(column=2, row=1)

root.mainloop()
