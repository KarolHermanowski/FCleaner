import tkinter as tk
from tkinter import filedialog, Text
# import classes
# from classes.folder import Folder
import os
def main():
    files = os.listdir("C:\\Users\\Dzik")
    print(files)
    # root = tk.Tk()
    # canvas = tk.Canvas(root, height=700, width=700, bg="#6666ff")
    # canvas.pack()

    # frame = tk.Frame(root, bg="white")
    # frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    # btn = tk.Button(root, text="Open file", padx=10,
    #                 pady=5, fg="white", bg="#6666ff")
    # btn.pack()
    # root.mainloop()


if __name__ == '__main__':
    main()
