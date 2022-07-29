from tkinter import *
from tokenize import String

#Variables
#ingrediente1 = StringVar()
#ingrediente2 = StringVar()
#ingrediente3 = StringVar()
#gramos1 = IntVar()
#gramos2 = IntVar()
#gramos2 = IntVar()


#Raíz
raiz = Tk()
raiz.title('La vuelta al mundo en 80 crepas')
raiz.resizable(0,0) #Para no dimensionar a mano
raiz.iconbitmap('happy_icon-icons.com_67810.ico')
raiz.geometry('580x270')
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

#Gramos ingrediente 1
cuadro1_1=Entry(miFrame)
cuadro1_1.grid(row=1,column=3)
cuadro1_1.config(justify='center')
labelcuadro1_1=Label(miFrame,text='gr: ',padx = 10,pady=15)
labelcuadro1_1.grid(row=1,column=2)

#Ingrediente 2
cuadro2=Entry(miFrame)
cuadro2.grid(row=2,column=1)
cuadro2.config(justify='center')
labelcuadro2=Label(miFrame,text='Ingrediente 2: ',padx = 10,pady=15)
labelcuadro2.grid(row=2,column=0)
#Gramos ingrediente 2
cuadro2_1=Entry(miFrame)
cuadro2_1.grid(row=2,column=3)
cuadro2_1.config(justify='center')
labelcuadro2_1=Label(miFrame,text='gr: ',padx = 10,pady=15)
labelcuadro2_1.grid(row=2,column=2)

#Ingrediente 3
cuadro3=Entry(miFrame)
cuadro3.grid(row=3,column=1)
cuadro3.config(justify='center')
labelcuadro3=Label(miFrame,text='Ingrediente 3: ',padx = 10,pady=15)
labelcuadro3.grid(row=3,column=0)
#Gramos ingrediente 3
cuadro2_1=Entry(miFrame)
cuadro2_1.grid(row=3,column=3)
cuadro2_1.config(justify='center')
labelcuadro2_1=Label(miFrame,text='gr: ',padx = 10,pady=15)
labelcuadro2_1.grid(row=3,column=2)

#Boton
def codigoBoton():
    print('Hola')


botonCalculo = Button(raiz, text='Calcular',pady=5,command=codigoBoton)
botonCalculo.pack()



if __name__ == '__main__':
    raiz.mainloop()