import tkinter as tk
import glob
from global_data import *
from tkinter import filedialog
from search_abs_in_folder import search_abs
from view_result import view_result

# main window
root = tk.Tk()
root.title('Simple ABS calculator')
root.geometry('300x25')


# widget definition
button_one = tk.Button(root, text='Search folder', command=search_abs)
button_two = tk.Button(root, text='Calculate', command=view_result)

# widget location
button_one.grid(column=1, row=1)
button_two.grid(column=2, row=1)
print(abs_to_analyze)
root.mainloop()
