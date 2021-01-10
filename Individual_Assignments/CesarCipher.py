from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.title_lbl = Label(self, text = "Caesar Cipher Encoder")
        self.title_lbl.grid()
        
        self.key_lbl = Label(self, text = "Key: ")
        self.key_lbl.grid()

        self.key_ent = Entry(self)
        self.key_ent.insert(0,"0")
        self.key_ent.grid()

        self.plaintext = Text(self, width = 50, height = 5, wrap = WORD)
        self.plaintext.grid()

        self.submit_bttn = Button(self, text = "Encode", command = self.encode)
        self.submit_bttn.grid()

        self.ciphertext = Text(self, width = 50, height = 5, wrap = WORD)
        self.ciphertext.grid()

    def caesar(self, letter, key):
        """ letter is a single text character, and key is an integer"""
        alpha = "abcdefghijklmnopqrstuvwxyz"
        
        if letter in alpha:
            new_index = (alpha.index(letter.lower()) + key)%26
            return(alpha[new_index])
        else:
            return(letter)
        

    def encode(self):
    
        user_in = self.plaintext.get(0.0, END)
        try:
            key = int(self.key_ent.get())
        except:
            empty_str = "Error Message"
        else:
            self.ciphertext.delete(0.0, END)
            empty_str = ""
            for letter in user_in:
                empty_str += self.caesar(letter, key)
        self.ciphertext.insert(0.0, empty_str)    

        

# main

root = Tk()
root.title("Caeser Cipher")
root.geometry("410x270")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
