import tkinter as tk
import random
import api
#encoding: utf-8
#list of common country flags and their short names

class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Flag Guessing Game")
        self.geometry("500x200")
        self.resizable(False, False)
        #check file gui
        self.checkFile()
        self.caracterToNotShow = ["a","m", "i", "h", "c", "y", "e", "o", "u", "n", "s", "t", "l", "r", "d", "g", "b", "p", "f", "v", "k", "w", "z", "x", "j", "q"]
        self.createWidgets()
        
        self.mainloop()
        
    def createWidgets(self):
        self.country, self.short = api.guessRandom()
        self.flag = tk.PhotoImage(file=f"images/{self.short}.png")
        #resize the image
        self.flag = self.flag.subsample(20, 20)
        self.label = tk.Label(self, image=self.flag)
        self.label.pack()
        
        self.entry = tk.Entry(self)
        self.entry.pack()
        
        self.button = tk.Button(self, text="Guess", command=self.guess, relief=tk.FLAT, bg="white", fg="black", font=("Arial", 20))
        self.button.pack(side=tk.LEFT)
        #HINT
        self.hint = tk.Button(self, text="Hint", command=self.hint, relief=tk.FLAT, bg="white", fg="black", font=("Arial", 20))
        self.hint.pack(side=tk.RIGHT)
        
        self.resultLabel = tk.Label(self, text="", font=("Arial", 20))
        self.resultLabel.pack()
        
        
    def hint(self):
        name = self.country.lower()
        newName = ""
        for i in range(len(name)):
            if i % 2 == 0:
                newName += name[i]
            else:
                newName += "_"
                
                
        self.resultLabel.config(text=newName)
    
    def guess(self):
        print(self.entry.get().lower())
        print(self.country.lower())
        
        if self.entry.get().lower() == self.country.lower():
            self.resultLabel.config(text="Correct!")
            print("Correct!")
            self.country, self.short = api.guessRandom()
            #reset the gui
            self.label.destroy()
            self.entry.destroy()
            self.button.destroy()
            self.hint.destroy()
            
            self.resultLabel.destroy()
            self.createWidgets()
            
        else:
            self.resultLabel.config(text="Wrong!")
            print("Wrong!")
        #reset the game
    
    def checkFile(self):
        api.DownloadImage()
        
        
if __name__ == "__main__":
    a = GUI()