import tkinter as tk
import PIL as pillow

#vars

buttons = []
root = tk.Tk()
root.title("Monster Card Catalogue")
root.geometry("670x500")

mainframe = tk.Frame(root,bg="#1f57a2",width=670,height=500)
mainframe.pack(fill="both",expand=True)

title = tk.Label(mainframe,text="Monster Card Catalogue",bg="#1f57a2",font=("Anton",30,"bold"))
title.grid(row=0,column=0,columnspan=5)

#function

def monsterbuttons():
    i=0
    for row in range(2):
        for col in range(5):
            print("bleh")
            hold = tk.Button(mainframe, text=f"monster{i+1}",width=12,height=5,bg="#a6a6a6")
            hold.grid(row=row+1, column=col,padx=20,pady=10)
            buttons.append(hold)
            i += 1 

#code

monsterbuttons()
root.mainloop()