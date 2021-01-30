 # allows run GUI
import tkinter as tk
from tkinter import filedialog, Text 
 # allows running apps
import os


#function to run apps


 # body structure of app
root = tk.Tk()

#add canvas to make it larger and add color

canvas = tk.Canvas(root, height=700, width=700, bg="#f7007b")
canvas.pack()

# add inside container
frame = tk.Frame(root, bg="#08e1d7")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#add button
openFile = tk.Button(root, text="Open File", padx=10, pady=5, 
fg="black", bg="#08e1d7" command="addApp")
openFile.pack()
#add button
runApp = tk.Button(root, text="Run Applications", padx=10, pady=5, 
fg="black", bg="#08e1d7") 

runApp.pack()
# run gui
root.mainloop()