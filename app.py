 # allows run GUI
import tkinter as tk
from tkinter import filedialog, Text 
 # allows running apps
import os

 # body structure of app
root = tk.Tk()
#empty to add appended apps to
apps = []

#function to open apps
def addApp():  
    #to delete app acess to whats in frame
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfile(initialdir="/", title="Select file",
    filetypes=(("executables","*.exe"), ("all files", "*.*")))

# append to apps
    apps.append(filename)
    print(filename)
#create lable
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()
# to run the applications
#loop over apps and start application
def runApps():
    for app in apps:
        os.startfile(app)
#add canvas to make it larger and add color
canvas = tk.Canvas(root, height=700, width=700, bg="#f7007b")
canvas.pack()

# add inside container
frame = tk.Frame(root, bg="#08e1d7")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#add button
openFile = tk.Button(root, text="Open File", padx=10, pady=5, 
fg="black", bg="#08e1d7", command=addApp)

openFile.pack()
#add button
runApp = tk.Button(root, text="Run Applications", padx=10, pady=5, 
fg="black", bg="#08e1d7", command=runApps) 

runApp.pack()
# run gui
root.mainloop()

# loop over apps and openFile
with open('save.txt', 'w') as f:
    for apps in apps:
        f.write(app + ',')