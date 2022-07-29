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
#miFrame.config(width = '550', height='550')


#Label
miLabel = Label(miFrame, text='Costo/Beneficio por crepa')
miLabel.grid(row=0,column=1)

#Entry
#Ingrediente 1
cuadro1=Entry(miFrame)
cuadro1.grid(row=1,column=1)
cuadro1.config(justify='center')
labelcuadro1=Label(miFrame,text='Ingrediente 1: ',padx = 10,pady=15)
labelcuadro1.grid(row=1,column=0)

#Ingrediente 2
cuadro2=Entry(miFrame)
cuadro2.grid(row=2,column=1)
cuadro2.config(justify='center')
labelcuadro2=Label(miFrame,text='Ingrediente 2: ',padx = 10,pady=15)
labelcuadro2.grid(row=2,column=0)

#Ingrediente 2
cuadro3=Entry(miFrame)
cuadro3.grid(row=3,column=1)
cuadro3.config(justify='center')
labelcuadro3=Label(miFrame,text='Ingrediente 3: ',padx = 10,pady=15)
labelcuadro3.grid(row=3,column=0)

if __name__ == '__main__':
    raiz.mainloop()