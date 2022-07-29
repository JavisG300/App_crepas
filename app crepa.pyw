from tkinter import *
from tokenize import String

#Raíz
raiz = Tk()
raiz.title('La vuelta al mundo en 80 crepas')
raiz.resizable(0,0) #Para no dimensionar a mano
raiz.iconbitmap('happy_icon-icons.com_67810.ico')
raiz.geometry('580x300')
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
cuadro3_1=Entry(miFrame)
cuadro3_1.grid(row=3,column=3)
cuadro3_1.config(justify='center')
labelcuadro3_1=Label(miFrame,text='gr: ',padx = 10,pady=15)
labelcuadro3_1.grid(row=3,column=2)

#Crepa creada
CostoPantalla = StringVar()
pantalla = Entry(miFrame, textvariable=CostoPantalla)
pantalla.grid(row=4,column=1, padx=10,pady=10,columnspan=3)
pantalla.config(justify="center")
label_pantalla = Label(miFrame,text='Costo total ',padx = 10,pady=15)
label_pantalla.grid(row=4,column=1)


#Boton
def codigoBoton():
    dic={'jamon':0.16,'quesocrema':0.12, 'quesomozarella':0.14}
    primer_ingrediente=cuadro1.get().strip().lower()
    gramo1 = cuadro1_1.get()
    segundo_ingrediente=cuadro2.get().strip().lower()
    gramo2 = cuadro2_1.get()
    tercer_ingrediente=cuadro3.get().strip().lower()
    gramo3 = cuadro3_1.get()
    costo = 2.76 + dic[primer_ingrediente]*float(gramo1) + dic[segundo_ingrediente]*float(gramo2) +  dic[tercer_ingrediente]*float(gramo3)
    costo = str(round(costo,2))
    CostoPantalla.set(costo)

botonCalculo = Button(raiz, text='Calcular',pady=5,command=codigoBoton)
botonCalculo.pack()



if __name__ == '__main__':
    raiz.mainloop()