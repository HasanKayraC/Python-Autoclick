from pynput.mouse import Button, Controller
import time
import tkinter as tk
import shutil

root= tk.Tk()
mouse = Controller()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def hello ():  
    label1 = tk.Label(root, text= 'İşlem başlatılıyor..', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    time.sleep(1)
    mouse.position=(250,250)    
    
    for x in range(20):
        mouse.press(Button.left)
        time.sleep(1)

    
button1 = tk.Button(text='Uzun Süreli Tıklama için Bana Tıkla',command=hello)
canvas1.create_window(150, 150, window=button1)



root.mainloop()
