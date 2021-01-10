

#9.20
#9.21
#9.22
from tkinter import *
import random



class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
#import random number between 0-9
#can either make game true or false, in this case true to prove false
        self.random_num = random.randint(0,9)
        self.game = True 
        
        

    def create_widgets(self):
        self.lbl = Label(self, text= "Enter your guess: ")
        self.lbl.grid()
        self.guess_ent = Entry(self)
        self.guess_ent.grid()
        self.guess_ent.bind('<Return>', self.key)
        self.bttn = Button(self, text= "Enter", command = self.reveal)
        self.bttn.grid()

    def reveal(self):
        guess = int(self.guess_ent.get())
        if guess == self.random_num:
#we don't need to import message box if we call it outright as shown below
            messagebox.showinfo(message = "You guessed right! Let's do it again!")
            self.game = False
#we destroy the root if guessed right, closing the window entirely 
            root.destroy()
        else:
            self.guess_ent.delete(0, END)

    def key(self, event):
        self.reveal()

    
            
            
            
            
    



#main
        
root = Tk()
root.title("Guessing Game!")
root.geometry("255x185")
app = Application(root)
root.mainloop()

while app.game == False:
    app.game = True
    root = Tk()
    root.title("Guessing Game!")
    root.geometry("255x185")
    app = Application(root)
    root.mainloop()
    
    
