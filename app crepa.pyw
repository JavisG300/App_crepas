from tkinter import *
from tokenize import String

#Raíz
raiz = Tk()
raiz.title('La vuelta al mundo en 80 crepas')
raiz.resizable(1,1) #Para no dimensionar a mano
raiz.iconbitmap('happy_icon-icons.com_67810.ico')
raiz.geometry('910x390')
raiz.config(bg='#CFECFF')

#Frame
miFrame = Frame() #Debemos meterlo dentro de la raíz
miFrame.pack()
#miFrame.config(width = '550', height='550')


#Label
miLabel = Label(miFrame, text='Costo/Beneficio por crepa')
miLabel.grid(row=0,column=1)
milabel2 = Label(miFrame,text ='jamon, quesocrema, mozarella, kitkat, nutella, mermelada, lechera, chocoretas, duraznos, oreo , salsatomate, gouda')
milabel2.grid(row=7,column=1)
milabel3 = Label(miFrame,text = 'peperoni, chantilly, nuez, manzana, nuez, canela, cajeta, platano, fresa, arandano')
milabel3.grid(row=8,column=1)
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

#Ingrediente 4
cuadro4=Entry(miFrame)
cuadro4.grid(row=4,column=1)
cuadro4.config(justify='center')
labelcuadro4=Label(miFrame,text='Ingrediente 4: ',padx = 10,pady=15)
labelcuadro4.grid(row=4,column=0)
#Gramos ingrediente 4
cuadro4_1=Entry(miFrame)
cuadro4_1.grid(row=4,column=3)
cuadro4_1.config(justify='center')
labelcuadro4_1=Label(miFrame,text='gr: ',padx = 10,pady=15)
labelcuadro4_1.grid(row=4,column=2)

#Ingrediente 5
cuadro5=Entry(miFrame)
cuadro5.grid(row=5,column=1)
cuadro5.config(justify='center')
labelcuadro5=Label(miFrame,text='Ingrediente 5: ',padx = 10,pady=15)
labelcuadro5.grid(row=5,column=0)
#Gramos ingrediente 5
cuadro5_1=Entry(miFrame)
cuadro5_1.grid(row=5,column=3)
cuadro5_1.config(justify='center')
labelcuadro5_1=Label(miFrame,text='gr: ',padx = 10,pady=15)
labelcuadro5_1.grid(row=5,column=2)

#Crepa creada
CostoPantalla = StringVar()
pantalla = Entry(miFrame, textvariable=CostoPantalla)
pantalla.grid(row=6,column=1, padx=10,pady=10,columnspan=3)
pantalla.config(justify="center")
label_pantalla = Label(miFrame,text='Costo total ',padx = 10,pady=15)
label_pantalla.grid(row=6,column=1)

#Boton
def codigoBoton():
    dic={'jamon':0.16,'quesocrema':0.12, 'quesomozarella':0.14,'kitkat':0.24,'nutella':0.17,'mermelada':0.12,'lechera':0.06,'chocoretas':0.2,'duraznos':0.06,'oreo':0.1,'salsatomate':0.09,'gouda':0.21,'peperoni':0.58,'chantilly':0.06,'nuez':0.5,'manzana':0.04,'nuez':0.5,'canela':0.17,'cajeta':0.15,'platano':0.033,'fresa':0.13,'arandano':0.3}
    primer_ingrediente=cuadro1.get().strip().lower()
    gramo1 = cuadro1_1.get()
    segundo_ingrediente=cuadro2.get().strip().lower()
    gramo2 = cuadro2_1.get()
    tercer_ingrediente=cuadro3.get().strip().lower()
    gramo3 = cuadro3_1.get()
    costo = 2.76 + 5 + dic[primer_ingrediente]*float(gramo1) + dic[segundo_ingrediente]*float(gramo2) +  dic[tercer_ingrediente]*float(gramo3)
    costo = str(round(costo,2))
    CostoPantalla.set(costo)

botonCalculo = Button(raiz, text='Calcular',pady=5,command=codigoBoton)
botonCalculo.pack()



if __name__ == '__main__':
    raiz.mainloop()