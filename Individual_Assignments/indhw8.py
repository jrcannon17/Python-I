from tkinter import *


class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
      
#make labels    
        self.lbl1 = Label(self, text="What would you like delivered?")
        self.lbl1.grid(row=1,column=0,sticky=W)
        
        self.ent_name = Entry(self,width=80)
        self.ent_name.grid(row=1,column=1,columnspan=5,sticky=W)

        self.lbl2 = Label(self, text= "Options")
        self.lbl2.grid(row=2,column=2)

        self.lbl3 = Label(self, text="Delivery Method:")
        self.lbl3.grid(row=3,column=0)
#make buttons. Set automatically to drone as selected method 
        self.method = StringVar()
        self.method.set("drone")

        Radiobutton(self,text="Flying Drone($10)",variable=self.method,
                    value="drone").grid(row=4,column=0)

        Radiobutton(self,text="Self Driving Car($20)",variable=self.method,
                    value="car").grid(row=5,column=0)

        Radiobutton(self,text="Giant Robot($1000)",variable=self.method,
                    value="robot").grid(row=6,column=0)

        

#make check boxes set to the right    

        self.lbl4 = Label(self, text="Addons:")
        self.lbl4.grid(row=3,column=3)
     

      

        self.express = BooleanVar()
        Checkbutton(self,text="Express Delivery (+$30)",
                    variable=self.express).grid(row=4,column=3)

        self.not_broke = BooleanVar()
        Checkbutton(self,text="Mostly Not Broken (+20)",
                    variable=self.not_broke).grid(row=5,column=3)

        
    

        self.smile = BooleanVar()
        Checkbutton(self,text="With a Smile (+1)",
                    variable=self.smile).grid(row=6,column=3)

     
      
#set the text and main command button 
        self.button0 = Button(self,text= "Confirm Delivery" ,command=self.update_bttn)
        self.button0.grid(row=7,column=2)

        self.txt0 = Text(self,width=70,height=4,wrap=WORD)
        self.txt0.grid(row=8,column=0,columnspan=10,rowspan=3, sticky=W)
        
    def update_bttn(self):
        cost = 0
#can make shorter?
        message = "You have selected to have a " + self.ent_name.get() + " delivered by " + self.method.get()     
        addon = []

        if self.method.get() == "drone":
            cost += 10

        if self.method.get() == "car":
            cost += 20

        if self.method.get() == "robot":
            cost += 1000

#combined text and cost in one to save space      

        if self.express.get():
            addon.append(" with express delivery")
            cost += 30

        if self.not_broke.get():
            addon.append(" mostly not broken")
            cost += 20

        if self.smile.get():
            addon.append(" with a smile")
            cost += 1

        if addon == []:
            message +=  " with no options"
        else:
            message += ",".join(addon) + "."

        message += " Your total delivery fee is: $" + str(cost)
#delete message after insert to start new order.
        self.txt0.delete(0.0, END)
        self.txt0.insert(0.0,message)
     
            
##
##        
        
        
       

##
      
        
        

# main
root = Tk()
root.title("Robot Delivery System")
root.geometry("560x265")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
