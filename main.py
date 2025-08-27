import tkinter as tk
import PIL as pillow

#vars

buttons = []
root = tk.Tk()
root.title("Monster Card Catalogue")
root.geometry("670x500")



#function
def mainmenusetup():
    mainframe = tk.Frame(root,bg="#1f57a2",width=670,height=500)
    mainframe.pack(fill="both",expand=True)

    title = tk.Label(mainframe,text="Monster Card Catalogue",bg="#1f57a2",font=("Anton",30,"bold"))
    title.grid(row=0,column=0,columnspan=5)

    sortbutton = tk.Button(mainframe,text="sort",width=10,height=1)
    sortbutton.grid(row=1,column=0)

    i=0
    for row in range(2):
        for col in range(5):
            print("bleh")
            hold = tk.Button(mainframe, text=f"monster{i+1}",width=12,height=5,bg="#a6a6a6",command=lambda idx=i: buttonmonsters(idx))
            hold.grid(row=row+2, column=col,padx=20,pady=10)
            buttons.append(hold)
            
            i += 1 
    addcard = tk.Button(mainframe,text="add card",width=10,height=1)
    addcard.grid(row=4,column=0)
    removecard = tk.Button(mainframe,text="add card",width=10,height=1)
    removecard.grid(row=4,column=1)
    editcard = tk.Button(mainframe,text="add card",width=10,height=1)
    editcard.grid(row=4,column=2)
    printcard = tk.Button(mainframe,text="add card",width=10,height=1)
    printcard.grid(row=4,column=3)
    selectedcard = tk.Label(mainframe,text="selected card")
    selectedcard.grid(row=4,column=4)
    viewcard = tk.Button(mainframe,text="add card",width=10,height=1)
    viewcard.grid(row=4,column=5)

def buttonmonsters(idx):
    print(idx,"pressed")
#code

mainmenusetup()
root.mainloop()