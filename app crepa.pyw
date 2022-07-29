from tkinter import *
#Raíz
raiz = Tk()
raiz.title('La vuelta al mundo en 80 crepas')
raiz.resizable(0,0) #Para no dimensionar a mano
raiz.iconbitmap('happy_icon-icons.com_67810.ico')
raiz.geometry('580x570')
raiz.config(bg='#CFECFF')

#Frame
miFrame = Frame() #Debemos meterlo dentro de la raíz
miFrame.pack()
miFrame.config(bg = '#FBF7CE' )
miFrame.config(width = '550', height='550')

miLabel = Label(miFrame, text='Costo/Beneficio por crepa')
miLabel.pack()

if __name__ == '__main__':
    raiz.mainloop()