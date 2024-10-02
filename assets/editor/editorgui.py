from tkinter import *
from tkinter import ttk                                       
from tkinter import font
from PIL import Image, ImageTk



class Editorgui:
    def __init__(self,Editorcontroller):
        self.label=[]                                       # list of labels = attributes
        self.text=[]
        self.entrystring=[]
        self.anzahl:int=0
        self.Editorcontroller=Editorcontroller
        self.root=Tk()
        self.root.title("Item & Creature Editor")
        width = self.root.winfo_screenwidth()  
        height = self.root.winfo_screenheight()
        self.root.geometry(str(width)+"x"+str(height))
        self.style = ttk.Style()
        self.root.option_add("*Font",('Verdana',12))

        self.frameTop = Frame(self.root, bg="lightblue")
        self.frameTop.pack_propagate(False)                                     # framesize fixed
        self.frameTop.pack(fill='both', expand=True)
        self.frameTop.pack()
        self.frameBottom = Frame(self.root)
        self.frameTop.grid(row=0, column=0,  sticky="nsew")                      # divide the view into 2 parts
        self.frameBottom.grid(row=2, column=0, sticky="nsew")
        self.frameTop.grid_propagate(False)                                     #fixed  size
        self.frameBottom.grid_propagate(False)

        self.buttonFrame = Frame(self.root)                                     
        self.buttonFrame.grid(row=1, column=0)
        self.buttonFrame.grid_columnconfigure(0, weight=1)
        self.buttonFrame.grid_columnconfigure(1, weight=1)

        self.statusLabel=ttk.Label(self.buttonFrame,text="",width=20)
        self.statusLabel.grid(row=0,column=0,padx=(10,10))
        self.buttonDel=ttk.Button(self.buttonFrame,text="Delete",command=self.Editorcontroller.delete,state="disabled")
        self.buttonDel.grid(row=0,column=1,padx=(0,10),pady=(0,0))
        self.buttonNew=ttk.Button(self.buttonFrame,text="New",command=self.Editorcontroller.createNew,state="disabled")
        self.buttonNew.grid(row=0,column=2,padx=(0,10),pady=(0,0))
        self.buttonSave=ttk.Button(self.buttonFrame,text="Save Changes",command=self.Editorcontroller.saveChanges,state="disabled")
        self.buttonSave.grid(row=0,column=3,padx=(0,10),pady=(0,0))
        self.buttonPrev=ttk.Button(self.buttonFrame,text="Previous",command=self.Editorcontroller.showPrevious,state="disabled")
        self.buttonPrev.grid(row=0,column=4,padx=(0,10),pady=(0,0))
        self.buttonNext=ttk.Button(self.buttonFrame,text="Next",command=self.Editorcontroller.showNext,state="disabled")
        self.buttonNext.grid(row=0,column=5,padx=(10,0),pady=(0,0))

        self.root.grid_rowconfigure(0, weight=50)                                    
        self.root.grid_rowconfigure(1, weight=1)                                    # button frame gets minimal weight
        self.root.grid_rowconfigure(2, weight=50)
        self.root.grid_columnconfigure(0, weight=1)                                 # width 100%

        menu_font = font.Font(size=14)
        menu=Menu(self.root)
        
        self.itemMenu=Menu(menu,tearoff=0,font=menu_font)
        self.itemMenu.add_command(label="Load Items",command=self.Editorcontroller.loadLocalItems)                       # ohne ()
        self.itemMenu.add_command(label="Save Items", command=self.Editorcontroller.saveLocalItems,state="disabled")        
        self.itemMenu.add_command(label="Load Creatures",command=self.Editorcontroller.loadLocalCreatures)                       # ohne ()
        self.itemMenu.add_command(label="Save Creatures", command=self.Editorcontroller.saveLocalCreatures,state="disabled")
        self.itemMenu.add_command(label="Pull Items from Github", command=self.Editorcontroller.pullItemsgithub,state="disabled")
        self.itemMenu.add_command(label="Push Items to Github", command=self.Editorcontroller.pushItemsgithub,state="disabled")
        menu.add_cascade(label="File", menu=self.itemMenu)
        self.creatureMenu=Menu(menu,tearoff=0,font=menu_font)
        self.creatureMenu.add_command(label="Help",command=self.Editorcontroller.showHelp,state="normal")
        
        menu.add_cascade(label="About",menu=self.creatureMenu,font=menu_font)       

        self.infoLabel=Label()
        self.table=ttk.Treeview()

        self.root.config(menu=menu)
        
    
   

    def initAttributes(self,key:str,value,index:int,state:str,type:str):
        label=ttk.Label(self.frameBottom,text=key)
        self.label.append(label)
        label.grid(row=index+1,column=0,sticky="e",padx=(0,10))
        style = ttk.Style()
        style.configure("type.TLabel", foreground="red") 
        typeLabel=ttk.Label(self.frameBottom,text=type,style="type.TLabel")
        typeLabel.grid(row=index+1,column=1,sticky="e",padx=(0,10))
        entry_var = StringVar()                                             # ttk.entry needs Stringvar() object
        entry_var.set(value)
        entry=ttk.Entry(self.frameBottom,textvariable=(entry_var))
        entry.configure(state=state)
        entry.grid(row=index+1,column=2)   
        self.text.append(entry)
        self.entrystring.append(entry_var)
        self.frameBottom.grid_rowconfigure(index, minsize=20)
    
    def showImage(self,name:str):
        image = Image.open(name)  
        scaled_image = image.resize((100,100))  
        self.tk_image = ImageTk.PhotoImage(scaled_image)
        label = ttk.Label(self.frameBottom, image=self.tk_image)
        label.grid(row=4,column=3,rowspan=50,sticky="n",padx=(20,0))        
        self.label.append(label)

    def updateView(self,key:str,value:str,index:int):
        self.label[index].config(text=key)
        if str(self.text[index].cget("state")) == "readonly":
            self.text[index].config(state="normal")
            self.text[index].delete(0, END)
            self.text[index].insert(0, value)
            self.text[index].config(state="readonly")
        else:
            self.text[index].delete(0,END)
            self.text[index].insert(0,value)

    def getEntryValue(self,index):
        return self.text[index].get()
    
    def setStatusNewItem(self,state):
        self.itemMenu.entryconfig("Save Items" , state=state)

    def setStatusNewCreature(self,state):
        self.itemMenu.entryconfig("Save Creatures" , state=state)
    def enableButtons(self):
        print("in buttons")
        self.buttonPrev.config(state="normal")
        self.buttonNext.config(state="normal")
        self.buttonDel.config(state="normal")
        self.buttonNew.config(state="normal")
        self.buttonSave.config(state="normal")

    def clearScreen(self):
        for label in self.label:
            label.destroy()
        self.entrystring=[]
        self.text=[]
        self.label=[]
        self.root.update()
    
    def printStatus(self,msg:str):
        self.statusLabel.config(text=msg)   
    
    def enableTable(self,columns:list):
        self.table.destroy()
        self.infoLabel.destroy()
        self.frameTop.update()
        
        columnWidth=int(int(self.root.geometry().split('x')[0])/len(columns))                    # tablewidth/ number of columns
        self.table = ttk.Treeview(self.frameTop, columns=columns, show='headings')
        scrollbar = ttk.Scrollbar(self.frameTop, orient=VERTICAL, command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='e')
        for col in columns:
            self.table.heading(col, text=col,command=lambda col=col: self.Editorcontroller.sortBy(col),anchor="center")
            self.table.column(col,width=columnWidth,anchor="center")
        self.table.pack(fill='both', expand=True)                                                   # table fills parent frame
        self.table.bind("<<TreeviewSelect>>", self.rowSelected)
    
    def addElements(self,elements:list):
        self.table.insert('',END, values=elements)
        
    def setHeader(self,key:str):
        self.table.heading(key, text=key)

    def rowSelected(self,event):
        item = self.table.focus()           
        print((self.table.item(item, 'values')[0]))                                                # select line
        self.Editorcontroller.processClickedItem((self.table.item(item, 'values')[0]))      # and return the 1rst value =id

    
    def showDocument(self,text:str):
        self.table.destroy()        
        self.infoLabel=Label(self.frameTop,text=text)
        self.infoLabel.pack()


    def startGui(self):
        self.root.mainloop()
    

    