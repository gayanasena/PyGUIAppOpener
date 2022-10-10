import tkinter as tk #for gui
from tkinter import filedialog,Text
import os #run apps

root = tk.Tk()
apps = []

if os.path.isfile('Save.txt'):
    with open('Save.txt','r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = tempApps
        print(tempApps)

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File")
    filetypes=(("executables","*exe"),("all files", "*.*"))
    print(filename)

    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

    apps.append(filename)

def runApp():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Applications", padx=10, pady=5, fg="white", bg="#263D42", command=runApp)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('Save.txt','w') as f:
    for app in apps:
        f.write(app+',')
