#imports
import tkinter as tk
from tkinter import ttk 
import PIL as pillow
from PIL import Image,ImageTk
from tkinter import messagebox
import os 


#arrey to hold the buttons
buttons = []

#inital data
cards = {
    0:{"name":"Vexscream","strength":1,"speed":6,"stealth":21,"cunning":19,"lock":True,"image":"vexscream"},
    1:{"name":"Dawnmirage","strength":5,"speed":15,"stealth":18,"cunning":22,"lock":True,"image":"dawnmirage"},
    2:{"name":"Blazegolem","strength":15,"speed":20,"stealth":23,"cunning":6,"lock":True,"image":"blazegolem"},
    3:{"name":"Moldvine","strength":21,"speed":18,"stealth":14,"cunning":5,"lock":True,"image":"moldvine"},
    4:{"name":"Vortexwing","strength":19,"speed":13,"stealth":19,"cunning":2,"lock":True,"image":"vortexwing"},
    5:{"name":"Froststep","strength":14,"speed":14,"stealth":17,"cunning":4,"lock":True,"image":"froststep"},
    6:{"name":"Wispghoul","strength":17,"speed":19,"stealth":3,"cunning":2,"lock":True,"image":"wispghoul"}

}


root = tk.Tk()

#function

#when the button is pressed it logs the id of the button to a global var
def buttonmonsters(id):
    global idx
    idx = id 
    #checks if the card id has a name and sets it to either empty or the id name
    if not idx in cards:
        selectedcard.config(text="selected card\nempty")
    else:  
        selectedcard.config(text="selected card\n"+cards[idx]["name"])
    

def addbutton():

    #checks if the there is already data in the selected id
    if idx in cards:
        messagebox.showerror("Monster Card Catalogue","Data already present")
        return
    
    # if not creates a temp data for the user to change
    cards[idx] = {"name":"","strength":1,"speed":1,"stealth":1,"cunning":1}
    

    #loads the correct frame
    mainframe.pack_forget()
    main2frame.pack_forget()
    addframe.pack(fill="both",expand=True)

    #loads the temp data into the inputs
    nameinput.insert(0,cards[idx]["name"])
    strengthinput.insert(0,cards[idx]["strength"])
    speedinput.insert(0,cards[idx]["speed"])
    stealthinput.insert(0,cards[idx]["stealth"])
    cunninginput.insert(0,cards[idx]["cunning"])

#card editor
def editbutton():

    #check if there is data in the selected id 
    if idx not in cards:
        messagebox.showerror("Monster Card Catalogue","No data present")
        return

    #checks if the id allows editing
    if cards[idx]["lock"] == True:
        messagebox.showerror("Monster Card Catalogue","Data cannot be edited")
        return
    
    #loads the correct frame
    mainframe.pack_forget()
    main2frame.pack_forget()
    addframe.pack(fill="both",expand=True)

    #loads the data into the inputs
    nameinput.insert(0,cards[idx]["name"])
    strengthinput.insert(0,cards[idx]["strength"])
    speedinput.insert(0,cards[idx]["speed"])
    stealthinput.insert(0,cards[idx]["stealth"])
    cunninginput.insert(0,cards[idx]["cunning"])

#viewing the card before saving
def preview():

    #checks if a value is either 25 > or < 0 and sets them to their upper and lower limits else it just sets them normally
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

    #sets the name to the name and sets lock to false
    cards[idx]["name"] = nameinput.get()
    cards[idx]["lock"] = False

    #set the correct frame
    addframe.pack_forget()
    previewframe.pack(fill="both",expand=True)

    #set the correct outputs for the user to check and make sure they are all correct
    nameresult.config(text=cards[idx]["name"])
    strengthresult.config(text=cards[idx]["strength"])
    speedresult.config(text=cards[idx]["speed"])
    stealthresult.config(text=cards[idx]["stealth"])
    cunningresult.config(text=cards[idx]["cunning"])


#checks if the character is digit or not and outputs true if it is and false if not
def validate_numeric_input(new_text):
        if new_text.isdigit() or new_text == "":
            return True
        else:
            return False   
    
#sets the correct frame based on the back to editing button press 
def backedit():
    previewframe.pack_forget()
    addframe.pack(fill="both",expand=True)

#goes to the card viewing frame
def cardview():
    #loads the correct frame
    mainframe.pack_forget()
    main2frame.pack_forget()
    viewframe.pack(fill="both",expand=True)


    #sets the output to the correct values
    nameviewoutput.config(text=cards[idx]["name"])
    strengthviewoutput.config(text=cards[idx]["strength"])
    speedviewoutput.config(text=cards[idx]["speed"])
    stealthviewoutput.config(text=cards[idx]["stealth"])
    cunningviewoutput.config(text=cards[idx]["cunning"])
    totalviewoutput.config(text=(cards[idx]["cunning"]+cards[idx]["stealth"]+cards[idx]["speed"]+cards[idx]["strength"]))


def saving():
    previewframe.pack_forget()
    mainframe.pack(side="top")
    main2frame.pack(fill="both",expand=True)
    nameinput.delete(0,'end')
    strengthinput.delete(0,'end')
    speedinput.delete(0,'end')
    stealthinput.delete(0,'end')
    cunninginput.delete(0,'end')
    buttons[idx].config(text=cards[idx]["name"])

def deletecard():
    if idx not in cards:
        messagebox.showerror("Monster Card Catalogue","Invaild data location")
        return
    
    if cards[idx]["lock"] == True:
        messagebox.showerror("Monster Card Catalogue","Data cannot be deleted")
        return

    del cards[idx]

    buttons[idx].config(text="empty")
    selectedcard.config(text="selected card\nempty")

def backmenu():
    viewframe.pack_forget()
    mainframe.pack(side="top")
    main2frame.pack(fill="both",expand=True)

def sort_cards(cards, stat, reverse=True):
    sorted_items = sorted(cards.values(), key=lambda x: x[stat], reverse=reverse)
    return {i: card for i, card in enumerate(sorted_items)}


#code setup
root.title("Monster Card Catalogue")
root.geometry("670x350")
vcmd = root.register(validate_numeric_input)

test = sort_cards(cards,"cunning",True)
print(test)
folder_path = "images"  
imagearrey = {}


for filename in os.listdir(folder_path):
    if filename.lower().endswith((".png")):
        img_path = os.path.join(folder_path, filename)
        name = os.path.splitext(filename)
        print(filename)
        image = Image.open(img_path)
        image = image.resize((88,75), Image.LANCZOS)
        holds = ImageTk.PhotoImage(image)
        imagearrey[name[0]] = holds
        print(imagearrey)

def imagecombo(event):
    imagelaabel.config(image=imagearrey[imageselecter.get()])
    cards[idx]["image"] = [imageselecter.get()]
    buttons[idx].config(image=imagearrey[imageselecter.get()])

#code 
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
        if i in cards:
            hold = cards[i]["name"]
        else:
            hold = "empty"
        print("bleh")
        hold = tk.Button(mainframe, text=hold,width=88,height=80,bg="#a6a6a6",command=lambda idx=i: buttonmonsters(idx),relief='flat',compound="top",font=("Anton",8,"bold"))
        if i in cards:
            hold.config(image=imagearrey[cards[i]["image"]])
        else:
            hold.config(image=imagearrey["empty"])
        hold.grid(row=row+2, column=col,padx=20,pady=10)
        buttons.append(hold)
            
        i += 1 
addcard = tk.Button(main2frame,text="add card",width=10,height=2,relief='flat',font=("Anton",8,"bold"),command=addbutton)
addcard.grid(row=-0,column=0,padx=20,pady=10)
removecard = tk.Button(main2frame,text="remove card",width=10,height=2,relief='flat',font=("Anton",8,"bold"),command=deletecard)
removecard.grid(row=0,column=1,padx=14,pady=10)
editcard = tk.Button(main2frame,text="edit card",width=10,height=2,relief='flat',font=("Anton",8,"bold"),command=editbutton)
editcard.grid(row=0,column=2,padx=14,pady=10)
viewcard = tk.Button(main2frame,text="view card",width=10,height=2,relief='flat',font=("Anton",8,"bold"),command=cardview)
viewcard.grid(row=0,column=3,padx=14,pady=10)
selectedcard = tk.Label(main2frame,text="selected card\n",font=("Anton",8,"bold"),width=12,height=2)
selectedcard.grid(row=0,column=4,padx=12,pady=10)
printcard = tk.Button(main2frame,text="print card",width=10,height=2,relief='flat',font=("Anton",8,"bold"))
printcard.grid(row=0,column=5,padx=12,pady=10)

addframe = tk.Frame(root,bg="#1f57a2",width=670,height=350)
title = tk.Label(addframe,text="Monster Card Catalogue",bg="#1f57a2",font=("Anton",30,"bold"))
title.pack()


imagelaabel = tk.Label(addframe,image=imagearrey["empty"])
imagelaabel.place(x=120,y=130)

combobox_options = list(imagearrey.keys())
imageselecter = ttk.Combobox(addframe,values=combobox_options)
imageselecter.place(x=100,y=100)
imageselecter.bind("<<ComboboxSelected>>", imagecombo)
imageselecter.set("empty")

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
namelabel.place(x=270,y=50)
strengthlabel = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Strength:")
strengthlabel.place(x=270,y=90)
speedlabel = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Speed:")
speedlabel.place(x=270,y=130)
stealthlabel = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Stealth:")
stealthlabel.place(x=270,y=170)
cunninglabel = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Cunning:")
cunninglabel.place(x=270,y=210)
totallabel = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Total Stats:")
totallabel.place(x=270,y=250)


nameresult = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="")
nameresult.place(x=420,y=50)
strengthresult = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="")
strengthresult.place(x=420,y=90)
speedresult = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="")
speedresult.place(x=420,y=130)
stealthresult = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="")
stealthresult.place(x=420,y=170)
cunningresult = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="")
cunningresult.place(x=420,y=210)
totalresult = tk.Label(previewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="")
totalresult.place(x=450,y=250)
backbutton = tk.Button(previewframe,text="Back to edit",width=10,height=1,relief='flat',font=("Anton",20,"bold"),command=backedit)
backbutton.place(x=150,y=300)
savebutton = tk.Button(previewframe,text="Save Card",width=10,height=1,relief='flat',font=("Anton",20,"bold"),command=saving)
savebutton.place(x=350,y=300)

viewframe = tk.Frame(root,bg="#1f57a2",width=670,height=350)

title = tk.Label(viewframe,text="Monster Card Catalogue",bg="#1f57a2",font=("Anton",30,"bold"))
title.pack()

namelabel = tk.Label(viewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Name:")
namelabel.place(x=270,y=50)
strengthlabel = tk.Label(viewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Strength:")
strengthlabel.place(x=270,y=90)
speedlabel = tk.Label(viewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Speed:")
speedlabel.place(x=270,y=130)
stealthlabel = tk.Label(viewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Stealth:")
stealthlabel.place(x=270,y=170)
cunninglabel = tk.Label(viewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Cunning:")
cunninglabel.place(x=270,y=210)
totallabel = tk.Label(viewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="Total Stats:")
totallabel.place(x=270,y=250)

nameviewoutput = tk.Label(viewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="")
nameviewoutput.place(x=420,y=50)
strengthviewoutput = tk.Label(viewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="")
strengthviewoutput.place(x=420,y=90)
speedviewoutput = tk.Label(viewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="")
speedviewoutput.place(x=420,y=130)
stealthviewoutput = tk.Label(viewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="")
stealthviewoutput.place(x=420,y=170)
cunningviewoutput = tk.Label(viewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="")
cunningviewoutput.place(x=420,y=210)
totalviewoutput = tk.Label(viewframe,bg="#1f57a2",font=("Anton",24,"bold"),text="")
totalviewoutput.place(x=450,y=250)
backbutton = tk.Button(viewframe,text="Back to menu",width=10,height=1,relief='flat',font=("Anton",20,"bold"),command=backmenu)
backbutton.place(x=250,y=290)


#code

root.mainloop()