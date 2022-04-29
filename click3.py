import tkinter as tk
from pynput.mouse import Button, Controller
import time
import shutil

mouse = Controller()
window = tk.Tk()

window.rowconfigure([0,1], minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)



frm_entry = tk.Frame(master=window)
sure_input = tk.Entry(master=frm_entry, width=10)
sure_input.grid(row=0, column=1)
frm_entry.grid(row=0, column=1)
sure=sure_input.get()

def basiliTut ():  
    # Mouse istenen konuma gidecek 1 sn sonra
    time.sleep(2)
    mouse.position=(450,450)    
    
    # Mouse kaç kez basılı kalacak
    for x in range(5):
        mouse.press(Button.left)
        # Basılı bekleme süresi x tekrar sayisi
        time.sleep(sure)

def tikla ():
    # Mouse istenen konuma gidecek 1 sn sonra
    time.sleep(2)
    mouse.position=(250,250)    
    
    # Mouse kaç kez basılı kalacak
    for x in range(5):
        mouse.press(Button.left)
        # Basılı bekleme süresi x tekrar sayisi
        time.sleep(sure)


btn_1 = tk.Button(master=window, text="Basılı Tut",command=basiliTut)
btn_1.grid(row=1, column=0, sticky="nsew")

btn_2 = tk.Button(master=window, text="AutoClick",command=tikla)
btn_2.grid(row=1, column=2, sticky="nsew")


window.mainloop()