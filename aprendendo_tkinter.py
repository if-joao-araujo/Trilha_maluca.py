"""
from tkinter import *
from tkinter import ttk

janela = Tk()
frame1 = Frame(janela)
frame1.pack()

butao = Button(frame1, text="Sim")
butao["width"] = 50
butao.pack(side="left")
butao.bind("")

butao2 = butao = Button(frame1, text="Não")
butao2["width"] = 50
butao2.pack(side="right")
janela.mainloop()"""
import pygame
print(pygame.__version__)


