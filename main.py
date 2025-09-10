import tkinter as tk
import PIL as pillow
from tkinter import messagebox

#vars

buttons = []
cards = {
    0:{"name":"unnamed monster","strength":1,"speed":1,"stealth":1,"cunning":1},
    1:{"name":"unnamed monster","strength":1,"speed":1,"stealth":1,"cunning":1},
    2:{"name":"unnamed monster","strength":1,"speed":1,"stealth":1,"cunning":1},
    3:{"name":"unnamed monster","strength":1,"speed":1,"stealth":1,"cunning":1},
    4:{"name":"unnamed monster","strength":1,"speed":1,"stealth":1,"cunning":1},
    5:{"name":"unnamed monster","strength":1,"speed":1,"stealth":1,"cunning":1},
    6:{"name":"unnamed monster","strength":1,"speed":1,"stealth":1,"cunning":1},
    7:{"name":"unnamed monster","strength":1,"speed":1,"stealth":1,"cunning":1},
    8:{"name":"unnamed monster","strength":1,"speed":1,"stealth":1,"cunning":1},
    9:{"name":"unnamed monster","strength":1,"speed":1,"stealth":1,"cunning":1}
    
    

}
idx = 0
root = tk.Tk()

#function
def buttonmonsters(id):
    global idx
    idx = id 
    print(idx,id)
    print(idx,"pressed")
    selectedcard.config(text=f"selected card\n{idx}monster")
    

def addbutton():
    print("peen ")
    print(idx)
    if not idx in cards:
       messagebox.showerror("test")
       return
    mainframe.pack_forget()
    main2frame.pack_forget()
    addframe.pack(fill="both",expand=True)

    nameinput.insert(0,cards[idx]["name"])
    strengthinput.insert(0,cards[idx]["strength"])
    speedinput.insert(0,cards[idx]["speed"])
    stealthinput.insert(0,cards[idx]["stealth"])
    cunninginput.insert(0,cards[idx]["cunning"])



def preview():
    if int(strengthinput.get()) > 25:
        cards[idx]["strength"] = 25
    elif int(strengthinput.get()) ==  0:
        cards[idx]["strength"] = 1
    else:
        cards[idx]["strength"]= int(strengthinput.get())

    if int(speedinput.get()) > 25:
        cards[idx]["speed"] = 25
    elif int(speedinput.get()) ==  0:
        cards[idx]["speed"] = 1
    else:
        cards[idx]["speed"]= int(speedinput.get())
    
    if int(stealthinput.get()) > 25:
        cards[idx]["stealth"] = 25
    elif int(stealthinput.get()) ==  0:
        cards[idx]["stealth"] = 1
    else:
        cards[idx]["stealth"]= int(stealthinput.get())
    
    if int(cunninginput.get()) > 25:
        cards[idx]["cunning"] = 25
    elif int(cunninginput.get()) ==  0:
        cards[idx]["cunning"] = 1
    else:
        cards[idx]["cunning"]= int(cunninginput.get())
    cards[idx]["name"] = nameinput.get()
    print("saving")

    addframe.pack_forget()
    previewframe.pack(fill="both",expand=True)
    nameresult.config(text=cards[idx]["name"])
    strengthresult.config(text=cards[idx]["strength"])
    speedresult.config(text=cards[idx]["speed"])
    stealthresult.config(text=cards[idx]["stealth"])
    cunningresult.config(text=cards[idx]["cunning"])

def validate_numeric_input(new_text):
        if new_text.isdigit() or new_text == "":
            return True
        else:
            return False   
    
def backedit():
    previewframe.pack_forget()
    addframe.pack(fill="both",expand=True)

def viewcard():
    mainframe.pack_forget()
    main2frame.pack_forget()
    previewframe.pack(fill="both",expand=True)
    nameresult.config(text=cards[idx]["name"])
    strengthresult.config(text=cards[idx]["strength"])
    speedresult.config(text=cards[idx]["speed"])
    stealthresult.config(text=cards[idx]["stealth"])
    cunningresult.config(text=cards[idx]["cunning"])


def saving():
    previewframe.pack_forget()
    mainframe.pack(side="top")
    main2frame.pack(fill="both",expand=True)
    nameinput.delete(0,'end')
    strengthinput.delete(0,'end')
    speedinput.delete(0,'end')
    stealthinput.delete(0,'end')
    cunninginput.delete(0,'end')

def deletecard():
    cards[idx]["name"] = "unnamed monster"
    cards[idx]["strength"] = 1
    cards[idx]["speed"] = 1
    cards[idx]["stealth"] = 1
    cards[idx]["cunning"] = 1

#code setup
root.title("Monster Card Catalogue")
root.geometry("670x350")
vcmd = root.register(validate_numeric_input)

mainframe = tk.Frame(root,bg="#1f57a2",width=670,height=220)
mainframe.pack(side="top")
main2frame = tk.Frame(root,bg="#1f57a2",width=670,height=0)
main2frame.pack(fill="both",expand=True)



title = tk.Label(mainframe,text="Monster Card Catalogue",bg="#1f57a2",font=("Anton",30,"bold"))
title.grid(row=0,column=0,columnspan=5)

sortbutton = tk.Button(mainframe,text="sort",width=10,height=1)
sortbutton.grid(row=1,column=0)

i=0
for row in range(2):
    for col in range(5):
        print("bleh")
        hold = tk.Button(mainframe, text=f"monster{i+1}",width=12,height=5,bg="#a6a6a6",command=lambda idx=i: buttonmonsters(idx),relief='flat',font=("Anton",8,"bold"))
        hold.grid(row=row+2, column=col,padx=20,pady=10)
        buttons.append(hold)
            
        i += 1 
addcard = tk.Button(main2frame,text="add card",width=10,height=2,relief='flat',font=("Anton",8,"bold"),command=addbutton)
addcard.grid(row=-0,column=0,padx=20,pady=10)
removecard = tk.Button(main2frame,text="remove card",width=10,height=2,relief='flat',font=("Anton",8,"bold"),command=deletecard)
removecard.grid(row=0,column=1,padx=14,pady=10)
editcard = tk.Button(main2frame,text="edit card",width=10,height=2,relief='flat',font=("Anton",8,"bold"))
editcard.grid(row=0,column=2,padx=14,pady=10)
printcard = tk.Button(main2frame,text="view card",width=10,height=2,relief='flat',font=("Anton",8,"bold"),command=viewcard)
printcard.grid(row=0,column=3,padx=14,pady=10)
selectedcard = tk.Label(main2frame,text="selected card\n",font=("Anton",8,"bold"))
selectedcard.grid(row=0,column=4,padx=14,pady=10)
viewcard = tk.Button(main2frame,text="print card",width=10,height=2,relief='flat',font=("Anton",8,"bold"))
viewcard.grid(row=0,column=5,padx=14,pady=10)

addframe = tk.Frame(root,bg="#1f57a2",width=670,height=350)
title = tk.Label(addframe,text="Monster Card Catalogue",bg="#1f57a2",font=("Anton",30,"bold"))
title.pack()

namelabel = tk.Label(addframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Name:")
namelabel.place(x=270,y=60)
strengthlabel = tk.Label(addframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Strength:")
strengthlabel.place(x=270,y=100)
speedlabel = tk.Label(addframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Speed:")
speedlabel.place(x=270,y=140)
stealthlabel = tk.Label(addframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Stealth:")
stealthlabel.place(x=270,y=180)
cunninglabel = tk.Label(addframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Cunning:")
cunninglabel.place(x=270,y=220)


nameinput = tk.Entry(addframe,width=10,font=("Anton",20,"bold"))
nameinput.place(x=420,y=65)
strengthinput = tk.Entry(addframe,width=10,font=("Anton",20,"bold"), validate="key", validatecommand=(vcmd, '%P'))
strengthinput.place(x=420,y=105)
speedinput = tk.Entry(addframe,width=10,font=("Anton",20,"bold"), validate="key", validatecommand=(vcmd, '%P'))
speedinput.place(x=420,y=145)
stealthinput = tk.Entry(addframe,width=10,font=("Anton",20,"bold"), validate="key", validatecommand=(vcmd, '%P'))
stealthinput.place(x=420,y=185)
cunninginput = tk.Entry(addframe,width=10,font=("Anton",20,"bold"), validate="key", validatecommand=(vcmd, '%P'))
cunninginput.place(x=420,y=225)

savebutton = tk.Button(addframe,text="preview",width=10,height=1,relief='flat',font=("Anton",24,"bold"),command=preview)
savebutton.place(x=250,y=275)

previewframe = tk.Frame(root,bg="#1f57a2",width=670,height=350)

title = tk.Label(previewframe,text="Monster Card Catalogue",bg="#1f57a2",font=("Anton",30,"bold"))
title.pack()

namelabel = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Name:")
namelabel.place(x=270,y=60)
strengthlabel = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Strength:")
strengthlabel.place(x=270,y=100)
speedlabel = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Speed:")
speedlabel.place(x=270,y=140)
stealthlabel = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Stealth:")
stealthlabel.place(x=270,y=180)
cunninglabel = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Cunning:")
cunninglabel.place(x=270,y=220)

nameresult = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Name:")
nameresult.place(x=420,y=60)
strengthresult = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="")
strengthresult.place(x=420,y=100)
speedresult = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Speed:")
speedresult.place(x=420,y=140)
stealthresult = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Stealth:")
stealthresult.place(x=420,y=180)
cunningresult = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Cunning:")
cunningresult.place(x=420,y=220)
backbutton = tk.Button(previewframe,text="Back to edit",width=10,height=1,relief='flat',font=("Anton",20,"bold"),command=backedit)
backbutton.place(x=150,y=275)
savebutton = tk.Button(previewframe,text="Save Card",width=10,height=1,relief='flat',font=("Anton",20,"bold"),command=saving)
savebutton.place(x=350,y=275)


#code

root.mainloop()