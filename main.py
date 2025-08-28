import tkinter as tk
import PIL as pillow

#vars

buttons = []
root = tk.Tk()
root.title("Monster Card Catalogue")
root.geometry("670x500")



#function
def mainmenusetup():
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
    addcard = tk.Button(main2frame,text="add card",width=10,height=1,relief='flat',font=("Anton",8,"bold"))
    addcard.grid(row=-0,column=0,padx=20,pady=10)
    removecard = tk.Button(main2frame,text="remove card",width=10,height=1,relief='flat',font=("Anton",8,"bold"))
    removecard.grid(row=0,column=1,padx=14,pady=10)
    editcard = tk.Button(main2frame,text="edit card",width=10,height=1,relief='flat',font=("Anton",8,"bold"))
    editcard.grid(row=0,column=2,padx=14,pady=10)
    printcard = tk.Button(main2frame,text="view card",width=10,height=1,relief='flat',font=("Anton",8,"bold"))
    printcard.grid(row=0,column=3,padx=14,pady=10)
    selectedcard = tk.Label(main2frame,text="selected card",font=("Anton",8,"bold"))
    selectedcard.grid(row=0,column=4,padx=14,pady=10)
    viewcard = tk.Button(main2frame,text="view card",width=10,height=1,relief='flat',font=("Anton",8,"bold"))
    viewcard.grid(row=0,column=5,padx=14,pady=10)

def buttonmonsters(idx):
    print(idx,"pressed")
#code

mainmenusetup()
root.mainloop()