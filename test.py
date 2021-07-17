from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk

import os, json, utils
import numpy as np
from PIL import Image, ImageTk

window = ThemedTk(theme="clearlooks")
ttk.Button(window, text="Quit", command=window.destroy).pack()
window.mainloop()


# # helpers\
# root = ThemedTk(theme="arc")
# root.title("Data Viewer")
# top = ttk.Frame(root)
# bottom = ttk.Frame(root)
# top.pack(side=tk.TOP)
# bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
# canvas = tk.Canvas(root,width=700,height=700)
# canvas.pack(in_=top, side=tk.LEFT, fill=tk.BOTH, expand=True)

# text = ttk.Label(root, width=30, height=1, text="")
# text.pack(in_=top, side=tk.LEFT, fill=tk.BOTH, expand=True)
# counter_text = ttk.Label(root, width=30, height=1, text="")
# counter_text.pack(in_=top, side=tk.LEFT, fill=tk.BOTH, expand=True)
# counter_text.configure(text="Current Video: " + str(1) + "/" + str(10))

# root.mainloop()