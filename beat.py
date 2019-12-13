import os
import tkinter as tk
import time



def gifoeffnen(name, gifnr):

    print("Name: ", name, " gifnr: ", gifnr)
    giffenster = tk.Tk()

    label = tk.Label()
    label.pack()

    counter = 0

    while counter < gifnr:
        photo = tk.PhotoImage(file=name, format="gif -index " + str(counter))
        label.config(image=photo)
        time.sleep(0.05)
        giffenster.update()
        counter += 1

        if counter > gifnr:
            giffenster.destroy()



    #gifoeffnen("files/fist.gif", 21)