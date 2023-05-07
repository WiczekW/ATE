# function returning list of paths to .abs files

from tkinter import filedialog
from global_data import abs_to_analyze
import glob


def search_abs():
    global abs_to_analyze
    folder_selected = filedialog.askdirectory()
    key_abs_files = folder_selected + '/*.abs'
    key_abs_files = key_abs_files.replace('/', '\\')
    abs_list = glob.glob(key_abs_files)
    abs_to_analyze = abs_list
    print(abs_to_analyze)
    pass

