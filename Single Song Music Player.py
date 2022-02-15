from tkinter import *
from tkinter import ttk
import pygame

class window:
    pygame.mixer.init()
    
    def __init__(self,root) -> None:
        self.root=root
        self.root.geometry('200x100')
        Label(self.root,text="Lover By Diljit Dosanjh.mp3").pack()
        ttk.Button(self.root,text="Play",command=self.play).pack()
        ttk.Button(self.root,text="Stop",command=self.pause).pack(pady=5)
    
    def play(self):
        pygame.mixer.music.load("Enter the path of music file ")
        pygame.mixer.music.play(loops=0)

    def pause(self):
        pygame.mixer.music.stop()
        pass



if __name__ == "__main__":
    win=Tk()

    window(win)
    win.mainloop()
