from tkinter import *
import time as tm


pencere = Tk()



def display_time():
    anlik_zaman = tm.strftime("%H:%M:%S")
    saat["text"] = anlik_zaman
    saat.after(200,display_time)

pencere.title("Mert'in Saati")
pencere.geometry("1100x300")

saat = Label(pencere, bg="black", fg="red", font=("Open Sans","200","bold") )
saat.pack()
display_time()



mainloop()
