import re
import csv
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import sys




root = tk.Tk()
root.title("Set List")
root.configure(background="white")
root.geometry("800x300")
root.minsize(800, 300)
root.maxsize(800, 300)

def UploadError():
    messagebox.showerror('File Error', 'Error: This was not a .txt file')


filename = ''
txt = '.txt'
def UploadAction(event=None):
    global filename
    filename = filedialog.askopenfilename() 
    if filename.endswith(txt):
        print('Selected:', filename)
    else:
        UploadError()

def destroy():
    global filename
    if filename.endswith(txt) == False:
        UploadError()
    else:
        root.destroy()

def check():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        print('Exiting program..')
        sys.exit(0)

topText = tk.Label(root, text='Choose a .txt file to upload here')
fileOpen = tk.Button(root, text='Choose file', padx=20, pady=10, command=UploadAction)
upload = tk.Button(root, text='Upload', padx=20, pady=10, command=destroy)


topText.place(x=400, y=50, anchor=CENTER)
fileOpen.place(x=400, y=150, anchor=CENTER)
upload.place(x=400, y=250, anchor=CENTER)

root.protocol("WM_DELETE_WINDOW", check)

root.mainloop()

# Skriv ønsket filnavn ↓ på den tabel-fil, som skal genereres
generated_csvfile = "loremipsum.csv"

# Her åbnes text-filen
txtfile_imported = open(filename, "rt")

# Her dannes en liste med de ord i textfilen, som er fremhævet med fed ( html ≈ <strong> )
newfile = txtfile_imported.read()               # Her læses indholdet af filen ind i "newfile"
pattern = "<strong>(.*?)</strong>"              # Her defineres mønsteret
ord_liste = re.findall(pattern, newfile)
length = len(ord_liste) 
print(ord_liste)       # Her dannes listen og gemmes som "ord_list"

print("\nDer er " + str(length) + " ord i alt.\n")
# print(ord_liste)

# Her dannes filen "generated_csvfile.csv"
ordliste_fil = open(generated_csvfile, "w")
ordliste_fil.write("")
ordliste_fil.close()

# Her skrives ordene ind i csv-filen - opdelt med 6 ord i hvert sæt
set_list = []
sets = 0
set_counter = 1
word_counter = 0
counting = True
words = 0

for strungs in ord_liste:
    words += 1
    if words % 6 == 0:
        set_list = ord_liste[:6:]
        np.random.shuffle(set_list)
        print(set_list)
        for i in set_list:
            ordliste_fil = open(generated_csvfile, "a")
            if word_counter % 6 == 0 :
                ordliste_fil.write("-------- set " + str(set_counter) + " ---\n")
                set_counter += 1
            ordliste_fil.write(i+"\n")
            word_counter += 1
            ordliste_fil.close()
