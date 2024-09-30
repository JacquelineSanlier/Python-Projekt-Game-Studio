import json
from item import Item
from creature import Creature
import requests
from pathlib import Path

class Editorcontroller:
    def __init__(self):
        self.itemList:Item=[]
        self.gui=None
        self.itemStructureKnown:bool=False								#can only add new creatures if json struc is known
        self.numberOfRows:int=0
        self.currentIndex:int=0                                             #listpointer
        self.types:str=[]
        self.filename:str=""
    
    def setGui(self,gui):
        self.gui=gui
    
    def loadLocalItems(self):
        self.gui.setStatusNewItem("normal")
        self.gui.setStatusNewCreature("disabled")
        self.filename="items.json"
        self.loadLocal()

    def saveLocalItems(self):
        self.saveLocal()

    def loadLocalCreatures(self):    
        self.gui.setStatusNewItem("disabled")
        self.gui.setStatusNewCreature("normal")
        self.filename="creatures.json"
        self.loadLocal()

    def saveLocalCreatures(self):
        self.saveLocal()

    def loadLocal(self):
        self.currentIndex=0
        self.itemList:Item=[]
        self.types=[]
        with open(self.filename, "r") as f:
            json_object = json.load(f)
        for key,value in json_object['config'].items():                             # save attribut types in list
            self.types.append(value) 
        tmp=self.getType() 
        for itemdata in json_object[tmp]: 
            itemTemp=Item()
            for key,value in itemdata.items():
                setattr(itemTemp,key,value)
            self.itemList.append(itemTemp)    
        self.gui.clearScreen()
        self.numberOfRows=0    
        self.initGuiAttribute()       
        self.gui.enableButtons()        

    def saveLocal(self):
        items_data = []
        for item in self.itemList:
            item_dict = {}
            for key in item.__dict__.keys():  
                item_dict[key] = getattr(item, key)  
            items_data.append(item_dict)
        tmp=self.getType()
        json_object = {
            "config": {key: value for key, value in zip(self.itemList[0].__dict__.keys(), self.types)},  
            f"{tmp}": items_data
        }
        with open(self.filename, "w") as f:
            json.dump(json_object, f, indent=4)

    def pullItemsgithub(self):
        pass

    def pushItemsgithub(self):
        pass

    def showHelp():
        pass        

    def showPrevious(self):
        self.currentIndex-=1
        if self.currentIndex<0 : self.currentIndex=len(self.itemList)-1
        self.updateView()
    
    def showNext(self):
        self.currentIndex+=1
        if self.currentIndex>=len(self.itemList): self.currentIndex=0
        self.updateView()
        
    def initGuiAttribute(self):
        self.numberOfRows=0                                             #attribut counter
        state:str="normal"                                              # attribute can be edited (ID cant)
        zaehler:int=0
        self.gui.clearScreen()
        for key,value in self.itemList[0].__dict__.items():
            if key=="id": state="readonly"
            else: state="normal"
            self.gui.initAttributes(key,value,self.numberOfRows,state,self.types[zaehler]) # attributes unknown until json is loaded
            zaehler+=1
            self.numberOfRows+=1
        img="img/"+self.getType()+str(self.itemList[0].id)+".png"      # image name =type_id
        if((Path(img)).is_file()):                                      # does image exist?
            self.gui.showImage(img,self.numberOfRows)
        else:
            img="img/noimg.jpeg"
            if((Path(img)).is_file()):
                self.gui.showImage(img,self.numberOfRows)
    
    def updateView(self):
        self.numberOfRows=0
        for key,value in self.itemList[self.currentIndex].__dict__.items():
            self.gui.updateView(key,str(value),self.numberOfRows)
            self.numberOfRows+=1
        img="img/"+self.getType()+"_"+str(self.itemList[self.currentIndex].id)+".png"        
        if((Path(img)).is_file()):                                      # does image exist?
            self.gui.showImage(img,self.numberOfRows)
        else:
            img="img/noimg.jpeg"
            if((Path(img)).is_file()): 
                self.gui.showImage(img,self.numberOfRows)

    def createNew(self):      
        maxId:int=0
        item:Item=Item()
        for i in self.itemList:
            for key,value in i.__dict__.items():               
                if key=="id" and int(value)>int(maxId):
                    maxId=int(value)
        for key,value in self.itemList[self.currentIndex].__dict__.items():          
            if key=="id":
                setattr(item,key,maxId+1)         
            else:
                if isinstance(value,str):                  
                    setattr(item,key,"empty")                    
                elif isinstance(value,int):
                    setattr(item,key,0)                
                elif isinstance(value,float):
                    setattr(item,key,0.0)
                else :print("error")
        self.itemList.append(item)
        self.currentIndex=len(self.itemList)-1
        self.updateView()        
    
    def delete(self):               #cant delete last item)
        if len(self.itemList)>0:
            del self.itemList[self.currentIndex]
            self.showPrevious()

    def saveChanges(self):
        index:int=0                    # correct data types?
        msg:str="data saved"                          # message for typeerrors
        for key,value in self.itemList[self.currentIndex].__dict__.items():
            help=  self.gui.getEntryValue(index)
            if(self.types[index]=='int'):
                try:
                    help=int(help)
                except:
                    msg="type error"
            elif(self.types[index]=='float'):
                try:
                    help=float(help)
                except:
                    msg="type error"
            elif(self.types[index]=="str"):
                try:
                    help=str(help)
                except:
                    msg="type error"
            index+=1
        index=0
        if msg=="data saved":
            for key,value in self.itemList[self.currentIndex].__dict__.items():
                if isinstance(value,str):                  
                    value=str(self.gui.getEntryValue(index))                    
                elif isinstance(value,int):
                    value=int(self.gui.getEntryValue(index))                
                elif isinstance(value,float):
                    value=float(self.gui.getEntryValue(index)) 
                setattr(self.itemList[self.currentIndex],key,value)
                index+=1          
        self.gui.printStatus(msg)
        
    def getType(self):
        if self.filename=="items.json": return ("items")
        elif self.filename=="creatures.json": return("creatures")