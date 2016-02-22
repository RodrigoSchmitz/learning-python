#para acostumar melhor com a sintaxe, fazer um relógio simples em python seguindo esse tutorial no youtube https://www.youtube.com/watch?v=xCiPshN9nOs
#para usar é só escrever esse código no shell interativo do python
import tkinter

rel = tkinter.Label()
from time import strftime
rel.pack()
rel['font'] = 'Helvetica 120 bold'


def tic():
	rel['text'] = strftime('%H:%M:%S')

def tac():
	tic()
	rel.after(1000, tac)
tac()