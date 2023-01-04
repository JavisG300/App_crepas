from distutils.command.config import config
from msilib.schema import File
from tkinter import  END, Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import  StringVar,Scrollbar,Frame, IntVar
from conexion import*
import time
class Ventana(Frame):
	def __init__(self, master, *args):
		super().__init__( master,*args)

		self.menu = True
		self.color = True
		self.codigo = StringVar()
		self.nombre = StringVar()
		self.modelo = StringVar()
		self.precio = StringVar()
		self.cantidad = StringVar()
		self.fecha = StringVar()
		self.productos = ("Italia","Hawaii","Tres Quesos","Chocomenta","Dopamina","Cajetosa","De la casa","1 a 2 ingredientes","2 a 4 ingredientes","4 a 6 ingredientes")
		self.cajaCantidad = IntVar()
		self.cajaTotal = IntVar()
		self.total = 0
		self.CostoPantalla = StringVar()
		self.cuadro1 = StringVar()
		self.cuadro2 = StringVar()
		self.cuadro3 = StringVar()
		self.cuadro4 = StringVar()
		self.cuadro5 = StringVar()
		self.cuadro6 = StringVar()
		self.cuadro1_1 = StringVar()
		self.cuadro2_1= StringVar()
		self.cuadro3_1= StringVar()
		self.cuadro4_1= StringVar()
		self.cuadro5_1= StringVar()
		self.cuadro6_1= StringVar()


		self.buscar = StringVar()
		self.buscar_actualiza =  StringVar()
		self.id = StringVar()
		self.base_datos = Registro_datos()

		self.frame_inicio = Frame(self.master, bg='#FEF5E7', width=50, height=45)
		self.frame_inicio.grid_propagate(0)
		self.frame_inicio.grid(column=0, row = 0, sticky='nsew')
		self.frame_menu = Frame(self.master, bg='#FEF5E7', width = 50)
		self.frame_menu.grid_propagate(0)
		self.frame_menu.grid(column=0, row = 1, sticky='nsew')
		self.frame_top = Frame(self.master, bg='#FEF5E7', height = 50)
		self.frame_top.grid(column = 1, row = 0, sticky='nsew')
		self.frame_principal = Frame(self.master, bg='#FEF5E7')
		self.frame_principal.grid(column=1, row=1, sticky='nsew')
		self.master.columnconfigure(1, weight=1)
		self.master.rowconfigure(1, weight=1)
		self.frame_principal.columnconfigure(0, weight=1)
		self.frame_principal.rowconfigure(0, weight=1)
		self.widgets()		

	def pantalla_inicial(self):
		self.paginas.select([self.frame_uno])
		
	def pantalla_datos(self):
		self.paginas.select([self.frame_dos])
		self.frame_dos.columnconfigure(0, weight=1)
		self.frame_dos.columnconfigure(1, weight=1)
		self.frame_dos.rowconfigure(2, weight=1)
		self.frame_tabla_uno.columnconfigure(0, weight=1)
		self.frame_tabla_uno.rowconfigure(0, weight=1)

	def pantalla_escribir(self):
		self.paginas.select([self.frame_tres])
		self.frame_tres.columnconfigure(0, weight=1)
		self.frame_tres.columnconfigure(1, weight=1)

	def pantalla_actualizar(self):
		self.paginas.select([self.frame_cuatro])	
		self.frame_cuatro.columnconfigure(0, weight=1)
		self.frame_cuatro.columnconfigure(1, weight=1)

	def pantalla_buscar(self):
		self.paginas.select([self.frame_cinco])
		self.frame_cinco.columnconfigure(0, weight=1)
		self.frame_cinco.columnconfigure(1, weight=1)
		self.frame_cinco.columnconfigure(2, weight=1)
		self.frame_cinco.columnconfigure(3, weight=1)
		self.frame_cinco.rowconfigure(7, weight=1)

	def pantalla_ajustes(self):
		self.paginas.select([self.frame_seis])

	def pantalla_precios(self):
		self.paginas.select([self.frame_siete])

	def menu_lateral(self):
		if self.menu is True:
			for i in range(50,170,10):				
				self.frame_menu.config(width= i)
				self.frame_inicio.config(width= i)
				self.frame_menu.update()
				clik_inicio = self.bt_cerrar.grid_forget()
				if clik_inicio is None:		
					self.bt_inicio.grid(column=0, row=0, padx =10, pady=10)
					self.bt_inicio.grid_propagate(0)
					self.bt_inicio.config(width=i)
					self.pantalla_inicial()
			self.menu = False
		else:
			for i in range(170,50,-10):
				self.frame_menu.config(width=  i)
				self.frame_inicio.config(width= i)
				self.frame_menu.update()
				clik_inicio = self.bt_inicio.grid_forget()
				if clik_inicio is   None:
					self.frame_menu.grid_propagate(0)		
					self.bt_cerrar.grid(column=0, row=0, padx =10, pady=10)
					self.bt_cerrar.grid_propagate(0)
					self.bt_cerrar.config(width=i)
					self.pantalla_inicial()
			self.menu = True

	
	def widgets(self):
		self.imagen_inicio = PhotoImage(file ='inicio.png')
		self.imagen_menu = PhotoImage(file ='menu.png')
		self.imagen_datos = PhotoImage(file ='datos.png')
		self.imagen_registrar = PhotoImage(file ='escribir.png')
		self.imagen_actualizar = PhotoImage(file ='actualizar.png')
		self.imagen_buscar = PhotoImage(file ='buscar.png')
		self.imagen_ajustes = PhotoImage(file ='configuracion.png')
		self.imagen_precios = PhotoImage(file ='costos.png')

		self.logo = PhotoImage(file = 'logo.png')
		self.imagen_uno = PhotoImage(file ='imagen_uno.png')
		self.imagen_dos= PhotoImage(file ='imagen_dos.png')
		self.bt_inicio = Button(self.frame_inicio, image= self.imagen_inicio, bg='#FEF5E7',activebackground='#FEF5E7', bd=0, command = self.menu_lateral)
		self.bt_inicio.grid(column=0, row=0, padx=5, pady=10)
		self.bt_cerrar = Button(self.frame_inicio, image= self.imagen_menu, bg='#FEF5E7',activebackground='#FEF5E7', bd=0, command = self.menu_lateral)
		self.bt_cerrar.grid(column=0, row=0, padx=5, pady=10)	
		#BOTONES Y ETIQUETAS DEL MENU LATERAL 
		Button(self.frame_menu, image= self.imagen_datos, bg='#FEF5E7', activebackground='#FEF5E7', bd=0, command = self.pantalla_datos).grid(column=0, row=1, pady=20,padx=10)
		Button(self.frame_menu, image= self.imagen_registrar, bg='#FEF5E7',activebackground='#FEF5E7', bd=0, command =self.pantalla_escribir ).grid(column=0, row=2, pady=20,padx=10)
		Button(self.frame_menu, image= self.imagen_actualizar, bg= '#FEF5E7',activebackground='#FEF5E7', bd=0, command = self.pantalla_actualizar).grid(column=0, row=3, pady=20,padx=10)
		Button(self.frame_menu, image= self.imagen_buscar, bg= '#FEF5E7',activebackground='#FEF5E7', bd=0, command = self.pantalla_buscar).grid(column=0, row=4, pady=20,padx=10)		
		Button(self.frame_menu, image= self.imagen_ajustes, bg= '#FEF5E7',activebackground='#FEF5E7', bd=0, command = self.pantalla_ajustes).grid(column=0, row=5, pady=20,padx=10)
		Button(self.frame_menu, image= self.imagen_precios, bg= '#FEF5E7',activebackground='#FEF5E7', bd=0, command = self.pantalla_precios).grid(column=0, row=6, pady=20,padx=10)
		
		Label(self.frame_menu, text= 'Ventas', bg= '#FEF5E7', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=1, pady=20, padx=2)
		Label(self.frame_menu, text= 'Registrar', bg= '#FEF5E7', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=2, pady=20, padx=2)
		Label(self.frame_menu, text= ' Actualizar', bg= '#FEF5E7', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=3, pady=20, padx=2)
		Label(self.frame_menu, text= 'Costos', bg= '#FEF5E7', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=4, pady=20, padx=2)	
		Label(self.frame_menu, text= 'Caja', bg= '#FEF5E7', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=5, pady=20, padx=2)
		Label(self.frame_menu, text= 'Precios', bg= '#FEF5E7', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=6, pady=20, padx=2)

        	#############################  CREAR  PAGINAS  ##############################
		estilo_paginas = ttk.Style()
		estilo_paginas.configure("TNotebook", background='#FEF5E7', foreground='black', padding=0, borderwidth=0)
		estilo_paginas.theme_use('default')
		estilo_paginas.configure("TNotebook", background='#FEF5E7', borderwidth=0)
		estilo_paginas.configure("TNotebook.Tab", background="#FEF5E7", borderwidth=0)
		estilo_paginas.map("TNotebook", background=[("selected", '#FEF5E7')])
		estilo_paginas.map("TNotebook.Tab", background=[("selected", '#FEF5E7')], foreground=[("selected", 'black')]);

		#CREACCION DE LAS PAGINAS 
		self.paginas = ttk.Notebook(self.frame_principal , style= 'TNotebook') #, style = 'TNotebook'
		self.paginas.grid(column=0,row=0, sticky='nsew')
		self.frame_uno = Frame(self.paginas, bg='#FEF5E7')
		self.frame_dos = Frame(self.paginas, bg='white')
		self.frame_tres = Frame(self.paginas, bg='white')
		self.frame_cuatro = Frame(self.paginas, bg='white')
		self.frame_cinco = Frame(self.paginas, bg='white')
		self.frame_seis = Frame(self.paginas, bg='white')
		self.frame_siete = Frame(self.paginas,bg='white')
		self.paginas.add(self.frame_uno)
		self.paginas.add(self.frame_dos)
		self.paginas.add(self.frame_tres)
		self.paginas.add(self.frame_cuatro)
		self.paginas.add(self.frame_cinco)
		self.paginas.add(self.frame_seis)
		self.paginas.add(self.frame_siete)
		##############################         PAGINAS       #############################################

		######################## FRAME TITULO #################
		self.titulo = Label(self.frame_top,text= 'La vuelta al mundo en 80 crepas', bg='#FEF5E7', fg= '#A569BD', font= ('Imprint MT Shadow', 15, 'bold'))
		self.titulo.pack(expand=1)
		######################## VENTANA PRINCIPAL #################
		Label(self.frame_uno, text= 'Bienvenid@ a la vuelta al mundo en 80 crepas', bg='#FEF5E7', fg= '#A569BD', font= ('Freehand521 BT', 20, 'bold')).pack(expand=1)
		Label(self.frame_uno ,image= self.logo, bg='#FEF5E7').pack(expand=1)

		######################## MOSTRAR TODOS LOS PRODUCTOS DE LA BASE DE DATOS MYSQL #################
		Label(self.frame_dos, text= 'Datos de MySQL', bg='#FEF5E7', fg= '#A569BD', font= ('Comic Sans MS', 12, 'bold')).grid(column =0, row=0)
		Button(self.frame_dos, text='VER DATOS',fg='black' ,font = ('Arial', 11,'bold'), command= self.datos_totales, bg = '#A569BD', bd = 2, borderwidth=2).grid(column=1, row=0, pady=5)
		Button(self.frame_dos, text='HOY',fg='black' ,font = ('Arial', 11,'bold'), command= self.datos_hoy, bg = '#A569BD', bd = 2, borderwidth=2).grid(column=2, row=0, pady=5)
		#ESTILO DE LAS TABLAS DE DATOS TREEVIEW
		estilo_tabla = ttk.Style()
		estilo_tabla.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='#FEF5E7')  #, fieldbackground='yellow'
		estilo_tabla.map('Treeview',background=[('selected', 'DarkOrchid1')], foreground=[('selected','black')] )		
		estilo_tabla.configure('Heading',background = 'white', foreground='navy',padding=3, font= ('Arial', 10, 'bold'))
		estilo_tabla.configure('Item',foreground = 'white', focuscolor ='DarkOrchid1')
		estilo_tabla.configure('TScrollbar', arrowcolor = 'DarkOrchid1',bordercolor  ='black', troughcolor= 'DarkOrchid1',background ='white')
		#TABLA UNO 
		self.frame_tabla_uno = Frame(self.frame_dos, bg= 'gray90')
		self.frame_tabla_uno.grid(columnspan=3, row=2, sticky='nsew')		
		self.tabla_uno = ttk.Treeview(self.frame_tabla_uno) 
		self.tabla_uno.grid(column=0, row=0, sticky='nsew')
		ladox = ttk.Scrollbar(self.frame_tabla_uno, orient = 'horizontal', command= self.tabla_uno.xview)
		ladox.grid(column=0, row = 1, sticky='ew') 
		ladoy = ttk.Scrollbar(self.frame_tabla_uno, orient ='vertical', command = self.tabla_uno.yview)
		ladoy.grid(column = 1, row = 0, sticky='ns')

		self.tabla_uno.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
		self.tabla_uno['columns'] = ('Crepa', 'Costo', 'Unidades', 'Precio','Utilidad')
		self.tabla_uno.column('#0', minwidth=100, width=120, anchor='center')
		self.tabla_uno.column('Crepa', minwidth=100, width=130 , anchor='center')
		self.tabla_uno.column('Costo', minwidth=100, width=120, anchor='center' )
		self.tabla_uno.column('Unidades', minwidth=100, width=120 , anchor='center')
		self.tabla_uno.column('Precio', minwidth=100, width=105, anchor='center')
		self.tabla_uno.column('Utilidad', minwidth=100, width=105, anchor='center')

		self.tabla_uno.heading('#0', text='Crepa', anchor ='center')
		self.tabla_uno.heading('Crepa', text='Costo', anchor ='center')
		self.tabla_uno.heading('Costo', text='Unidades', anchor ='center')
		self.tabla_uno.heading('Unidades', text='Precio', anchor ='center')
		self.tabla_uno.heading('Precio', text='Utilidad', anchor ='center')
		self.tabla_uno.heading('Utilidad', text='Fecha',anchor ='center')
		self.tabla_uno.bind("<<TreeviewSelect>>", self.obtener_fila)

		######################## REGISTRAR  NUEVOS PRODUCTOS #################
		Label(self.frame_tres, text = 'Agregar Nuevos Datos',fg='purple', bg ='white', font=('Kaufmann BT',24,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
		Label(self.frame_tres, text = 'Crepa',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15, padx=5)
		Label(self.frame_tres, text = 'Costo',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15)
		Label(self.frame_tres, text = 'Unidades',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
		Label(self.frame_tres, text = 'Precio', fg='navy',bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
		Label(self.frame_tres, text = 'Utilidad',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)
		Label(self.frame_tres, text = 'Fecha',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=6, pady=15)

		Entry(self.frame_tres, textvariable=self.codigo , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=1)
		Entry(self.frame_tres, textvariable=self.nombre , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=2)
		Entry(self.frame_tres, textvariable=self.modelo , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=3)
		Entry(self.frame_tres, textvariable=self.precio , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=4)
		Entry(self.frame_tres, textvariable=self.cantidad , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=5)
		Entry(self.frame_tres, textvariable=self.fecha , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=6)



		Button(self.frame_tres,command= self.agregar_datos, text='REGISTRAR', font=('Arial',10,'bold'), bg='magenta2').grid(column=3,row=7, pady=10, padx=4)
		Label(self.frame_tres, image= self.imagen_uno, bg= 'white').grid(column= 3, rowspan= 5, row = 0, padx= 50)
		self.aviso_guardado = Label(self.frame_tres, bg= 'white', font=('Comic Sans MS', 12), fg='black')
		self.aviso_guardado.grid(columnspan= 2 , column =0, row = 7, padx= 5)

		########################   ACTUALIZAR LOS PRODUCTOS REGISTRADOS     #################
		Label(self.frame_cuatro, text = 'Actualizar Datos',fg='#A569BD', bg ='white', font=('Kaufmann BT',24,'bold')).grid(columnspan=4, row=0)		
		Label(self.frame_cuatro, text = 'Ingrese el nombre del producto a actualizar',fg='black', bg ='white', font=('Rockwell',12)).grid(columnspan=2,row=1)
		Entry(self.frame_cuatro, textvariable= self.buscar_actualiza , font=('Comic Sans MS', 12), highlightbackground = "magenta2", width=12, highlightthickness=5).grid(column=2,row=1, padx=5)
		Button(self.frame_cuatro, command= self.actualizar_datos, text='BUSCAR', font=('Arial',12,'bold'), bg='deep sky blue').grid(column=3,row=1, pady=5, padx=15)
		self.aviso_actualizado = Label(self.frame_cuatro, fg='black', bg ='white', font=('Arial',12,'bold'))
		self.aviso_actualizado.grid(columnspan= 2, row=7, pady=10, padx=5)

		Label(self.frame_cuatro, text = 'Crepa',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15, padx=10)
		Label(self.frame_cuatro, text = 'Costo',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
		Label(self.frame_cuatro, text = 'Unidades',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
		Label(self.frame_cuatro, text = 'Precio', fg='navy',bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)
		Label(self.frame_cuatro, text = 'Utilidad',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=6, pady=15)
		Label(self.frame_cuatro, text = 'Fecha',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=7, pady=15)

		Entry(self.frame_cuatro, textvariable=self.codigo , font=('Comic Sans MS', 12), highlightbackground = "deep sky blue", highlightcolor= "green", highlightthickness=5).grid(column=1,row=2)
		Entry(self.frame_cuatro, textvariable=self.nombre , font=('Comic Sans MS', 12), highlightbackground = "deep sky blue", highlightcolor= "green", highlightthickness=5).grid(column=1,row=3)
		Entry(self.frame_cuatro, textvariable=self.modelo , font=('Comic Sans MS', 12), highlightbackground = "deep sky blue", highlightcolor= "green", highlightthickness=5).grid(column=1,row=4)
		Entry(self.frame_cuatro, textvariable=self.precio , font=('Comic Sans MS', 12), highlightbackground = "deep sky blue", highlightcolor= "green", highlightthickness=5).grid(column=1,row=5)
		Entry(self.frame_cuatro, textvariable=self.cantidad , font=('Comic Sans MS', 12), highlightbackground = "deep sky blue", highlightcolor= "green", highlightthickness=5).grid(column=1,row=6)
		Entry(self.frame_cuatro, textvariable=self.fecha , font=('Comic Sans MS', 12), highlightbackground = "deep sky blue", highlightcolor= "green", highlightthickness=5).grid(column=1,row=7)

		Button(self.frame_cuatro,command= self.actualizar_tabla, text='ACTUALIZAR', font=('Arial',12,'bold'), bg='magenta2').grid(column=2, columnspan= 2 ,row=8, pady=2)
		Label(self.frame_cuatro, image= self.imagen_dos, bg='white').grid(column= 2,columnspan= 2, rowspan= 5, row = 1, padx=2)

		######################## CALCULAR COSTOS #################
		Label(self.frame_cinco, text = 'Calcular costos',fg='#A569BD', bg ='white', font=('Kaufmann BT',24,'bold')).grid(columnspan= 4,  row=0,sticky='nsew',padx=2)
	#Ingrediente 1
		Entry(self.frame_cinco,textvariable=self.cuadro1).grid(row=1,column=1)
		Label(self.frame_cinco,text='Ingrediente 1: ',padx = 5,pady=10).grid(row=1,column=0)
	#Gramos ingrediente 1
		Entry(self.frame_cinco,textvariable=self.cuadro1_1).grid(row=1,column=3)
		Label(self.frame_cinco,text='gr: ',padx = 5,pady=10).grid(row=1,column=2)
	#Ingrediente 2
		Entry(self.frame_cinco,textvariable=self.cuadro2).grid(row=2,column=1)
		Label(self.frame_cinco,text='Ingrediente 2: ',padx = 5,pady=10).grid(row=2,column=0)
	#Gramos ingrediente 2
		Entry(self.frame_cinco,textvariable=self.cuadro2_1).grid(row=2,column=3)
		Label(self.frame_cinco,text='gr: ',padx = 5,pady=10).grid(row=2,column=2)
	#Ingrediente 3
		Entry(self.frame_cinco,textvariable=self.cuadro3).grid(row=3,column=1)
		Label(self.frame_cinco,text='Ingrediente 3: ',padx = 5,pady=10).grid(row=3,column=0)
	#Gramos ingrediente 3
		Entry(self.frame_cinco,textvariable=self.cuadro3_1).grid(row=3,column=3)
		Label(self.frame_cinco,text='gr: ',padx = 5,pady=10).grid(row=3,column=2)
	#Ingrediente 4
		Entry(self.frame_cinco,textvariable=self.cuadro4).grid(row=4,column=1)
		Label(self.frame_cinco,text='Ingrediente 4: ',padx = 5,pady=10).grid(row=4,column=0)
	#Gramos ingrediente 4
		Entry(self.frame_cinco,textvariable=self.cuadro4_1).grid(row=4,column=3)
		Label(self.frame_cinco,text='gr: ',padx = 5,pady=10).grid(row=4,column=2)
	#Ingrediente 5
		Entry(self.frame_cinco,textvariable=self.cuadro5).grid(row=5,column=1)
		Label(self.frame_cinco,text='Ingrediente 5: ',padx = 5,pady=10).grid(row=5,column=0)
	#Gramos ingrediente 5
		Entry(self.frame_cinco,textvariable=self.cuadro5_1).grid(row=5,column=3)
		Label(self.frame_cinco,text='gr: ',padx = 5,pady=10).grid(row=5,column=2)
	#Ingrediente 6
		Entry(self.frame_cinco,textvariable=self.cuadro6).grid(row=6,column=1)
		Label(self.frame_cinco,text='Ingrediente 6: ',padx = 5,pady=10).grid(row=6,column=0)
	#Gramos ingrediente 6
		Entry(self.frame_cinco,textvariable=self.cuadro6_1).grid(row=6,column=3)
		Label(self.frame_cinco,text='gr: ',padx = 5,pady=10).grid(row=6,column=2)
	#Crepa creada
		Entry(self.frame_cinco, textvariable=self.CostoPantalla).grid(row=7, column=2, padx=10,pady=10)
		Label(self.frame_cinco,text='Costo total ',padx = 10,pady=15).grid(row=7,column=1)
		Button(self.frame_cinco, text='Calcular',pady=5,command=self.codigoBoton, font=('Arial',12,'bold'), bg='#A569BD').grid(column=3, columnspan= 4 ,row=7, pady=2)
    
			
		######################## CAJA REGISTRADORA #################
		Label(self.frame_seis,text="Selecciona tu producto: ").place(x=10,y=10)
		Label(self.frame_seis,text="Seleciona la cantidad: ").place(x=10,y=60)
		Label(self.frame_seis,text="El total es: ").place(x=450,y=400)
		self.combo = ttk.Combobox(self.frame_seis,state="readonly")
		self.combo.place(x=10,y=35)
		self.combo["values"]=self.productos
		self.combo.current(0)
		Entry(self.frame_seis,textvariable=self.cajaCantidad).place(x=10,y=85)
		Entry(self.frame_seis,textvariable=self.cajaTotal).place(x=520,y=400)
		Button(self.frame_seis,text="Agregar",command=self.agregarProducto).place(x=10,y=110)
		Button(self.frame_seis,text="Limpiar",command=self.limpiarcuenta).place(x=650,y=400)
		self.tabla = ttk.Treeview(self.frame_seis,columns=("Cantidad","Subtotal"))
		self.tabla.heading("#0",text="Producto")
		self.tabla.heading("Cantidad",text="Cantidad")
		self.tabla.heading("Subtotal",text="Subtotal")
		self.tabla.place(x=10,y=150)

		######################## PRECIOS #################
		
		Label(self.frame_siete, text= 'Datos de MySQL', bg='#FEF5E7', fg= '#A569BD', font= ('Comic Sans MS', 12, 'bold')).grid(column =0, row=0)
		Button(self.frame_siete, text='VER',fg='black' ,font = ('Arial', 11,'bold'), command= self.datos_precios, bg = '#A569BD', bd = 2, borderwidth=2).grid(column=1, row=0, pady=5)
		
		estilo_tabla_1 = ttk.Style()
		estilo_tabla_1.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='#FEF5E7')  #, fieldbackground='yellow'
		estilo_tabla_1.map('Treeview',background=[('selected', 'DarkOrchid1')], foreground=[('selected','black')] )		
		estilo_tabla_1.configure('Heading',background = 'white', foreground='navy',padding=3, font= ('Arial', 10, 'bold'))
		estilo_tabla_1.configure('Item',foreground = 'white', focuscolor ='DarkOrchid1')
		estilo_tabla_1.configure('TScrollbar', arrowcolor = 'DarkOrchid1',bordercolor  ='black', troughcolor= 'DarkOrchid1',background ='white')
		
		#TABLA UNO_1
		self.frame_tabla_uno_1 = Frame(self.frame_siete, bg= 'gray90')
		self.frame_tabla_uno_1.grid(columnspan=2, row=2, sticky='nsew')		
		self.tabla_uno_1 = ttk.Treeview(self.frame_tabla_uno_1) 
		self.tabla_uno_1.grid(column=0, row=0, sticky='nsew')
		ladox = ttk.Scrollbar(self.frame_tabla_uno_1, orient = 'horizontal', command= self.tabla_uno_1.xview)
		ladox.grid(column=0, row = 1, sticky='ew') 
		ladoy = ttk.Scrollbar(self.frame_tabla_uno_1, orient ='vertical', command = self.tabla_uno_1.yview)
		ladoy.grid(column = 1, row = 0, sticky='ns')


		self.tabla_uno_1.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
		self.tabla_uno_1['columns'] = ('Crepa')
		self.tabla_uno_1.column('#0', minwidth=100, width=464, anchor='center')
		self.tabla_uno_1.column('Crepa', minwidth=100, width=464 , anchor='center')

		self.tabla_uno_1.heading('#0', text='Crepa', anchor ='center')
		self.tabla_uno_1.heading('Crepa', text='Precio', anchor ='center')
		self.tabla_uno_1.bind("<<TreeviewSelect>>", self.obtener_fila)

	def agregarProducto(self):
		texto = self.combo.get()
		producto = texto
		precios = {"Italia":80,"Hawaii":75,"Tres Quesos":75,"Chocomenta":65,"Dopamina":65,"Cajetosa":65,"De la casa":60,"1 a 2 ingredientes":55,"2 a 4 ingredientes":70,"4 a 6 ingredientes":85}
		precio = precios[producto]
		cantidad = self.cajaCantidad.get()
		subtotal = int(precio)*int(cantidad)
		self.tabla.insert("",END,text=producto,values=(cantidad,"$"+str(subtotal)))
		self.total = self.total + subtotal
		self.cajaTotal.set("$"+str(self.total))

	def limpiarcuenta(self):
		self.tabla.delete(*self.tabla.get_children())
		self.total = 0
		self.cajaTotal.set('')
		self.cajaCantidad.set('')

		

	def datos_totales(self):
		datos = self.base_datos.mostrar_productos()
		self.tabla_uno.delete(*self.tabla_uno.get_children())
		i = -1
		for dato in datos:
			i= i+1
			self.tabla_uno.insert('',i, text = datos[i][1:2], values=datos[i][2:7])
	
	def datos_hoy(self):
		datos = self.base_datos.mostrar_productos_hoy()
		self.tabla_uno.delete(*self.tabla_uno.get_children())
		i = -1
		for dato in datos:
			i= i+1
			self.tabla_uno.insert('',i, text = datos[i][1:2], values=datos[i][2:7])
	
	def datos_precios(self):
		datos = self.base_datos.mostrar_precios()
		self.tabla_uno_1.delete(*self.tabla_uno_1.get_children())
		i = -1
		for dato in datos:
			i= i+1
			self.tabla_uno_1.insert('',i, text = datos[i][0:1], values=datos[i][1:2])

	def agregar_datos(self):
		codigo = self.codigo.get()
		nombre = self.nombre.get()
		modelo = self.modelo.get()
		precio = self.precio.get()
		cantidad = self.cantidad.get()
		fecha = self.fecha.get()
		datos = (nombre, modelo, precio, cantidad, fecha)
		if codigo and nombre and modelo and precio and cantidad and fecha !='':
			self.tabla_uno.insert('',0, text = codigo, values=datos)
			self.base_datos.inserta_producto(codigo, nombre, modelo, precio, cantidad,fecha)
			self.aviso_guardado['text'] = 'Datos Guardados'
			self.limpiar_datos()
			self.aviso_guardado.update()						
			time.sleep(1) 
			self.aviso_guardado['text'] = ''						
		else:
			self.aviso_guardado['text'] = 'Ingrese todos los datos'
			self.aviso_guardado.update()
			time.sleep(1) 
			self.aviso_guardado['text'] = ''

	def actualizar_datos(self):
		dato = self.buscar_actualiza.get()
		dato = str("'" + dato + "'")
		nombre_buscado = self.base_datos.busca_producto(dato)
		if nombre_buscado == []:
			self.aviso_actualizado['text'] = 'No existe'			
			self.indica_busqueda.update()						
			time.sleep(1) 
			self.limpiar_datos()
			self.aviso_actualizado['text'] = ''
		else:
			i = -1
			for dato in nombre_buscado:
				i= i+1
				self.id.set(nombre_buscado[i][0])
				self.codigo.set(nombre_buscado[i][1])
				self.nombre.set(nombre_buscado[i][2])
				self.modelo.set(nombre_buscado[i][3])
				self.precio.set(nombre_buscado[i][4])
				self.cantidad.set(nombre_buscado[i][5])
				self.fecha.set(nombre_buscado[i][6])


	def actualizar_tabla(self):	
		Id = self.id.get() 	
		codigo = self.codigo.get()
		nombre = self.nombre.get()
		modelo = self.modelo.get()
		precio = self.precio.get()
		cantidad = self.cantidad.get()
		fecha = self.fecha.get()
		self.base_datos.actualiza_productos(Id, codigo, nombre, modelo, precio, cantidad,fecha)		
		self.aviso_actualizado['text'] = 'Datos Actualizados'			
		self.indica_busqueda.update()						
		time.sleep(1) 
		self.aviso_actualizado['text'] = ''
		self.limpiar_datos()
		self.buscar_actualiza.set('')				
	def limpiar_datos(self):
		self.codigo.set('')
		self.nombre.set('')
		self.modelo.set('')
		self.precio.set('')
		self.cantidad.set('')
		self.fecha.set('')

	def buscar_nombre(self):
		nombre_producto = self.buscar.get()
		nombre_producto = str("'" + nombre_producto + "'")
		nombre_buscado = self.base_datos.busca_producto(nombre_producto)
		if nombre_buscado == []:
			self.indica_busqueda['text'] = 'No existe'
			self.indica_busqueda.update()						
			time.sleep(1) 
			self.indica_busqueda['text'] =''
		i = -1
		for dato in nombre_buscado:
			i= i+1
			self.tabla_dos.insert('',i, text = nombre_buscado[i][1:2], values=nombre_buscado[i][2:7])
	def eliminar_fila(self):
		fila = self.tabla_dos.selection()
		if len(fila) !=0:
			self.tabla_dos.delete(fila)
			nombre = ("'"+ str(self.nombre_borrar) + "'")
			self.base_datos.elimina_productos(nombre)
			self.indica_busqueda['text'] = 'Eliminado'
			self.indica_busqueda.update()						
			self.tabla_dos.delete(*self.tabla_dos.get_children())
			time.sleep(1)
			self.indica_busqueda['text'] =''
			self.limpiar_datos()
		else:
			self.indica_busqueda['text'] = 'No se Elimino'
			self.indica_busqueda.update()
			self.tabla_dos.delete(*self.tabla_dos.get_children())						
			time.sleep(1) 
			self.indica_busqueda['text'] =''
			self.buscar.set('')
			self.limpiar_datos()

	def obtener_fila(self, event):
		current_item = self.tabla_dos.focus()
		if not current_item:
			return
		data = self.tabla_dos.item(current_item)
		self.nombre_borrar = data['values'][0]
		    
	def codigoBoton(self):
		primer_ingrediente = self.cuadro1.get().strip().lower()
		gramo1 = self.cuadro1_1.get()
		segundo_ingrediente = segundo_ingrediente = self.cuadro2.get().strip().lower()
		gramo2 = self.cuadro2_1.get()
		tercer_ingrediente = self.cuadro3.get().strip().lower()
		gramo3 = self.cuadro3_1.get()
		cuarto_ingrediente = self.cuadro4.get().strip().lower()
		gramo4 = self.cuadro4_1.get()
		quinto_ingrediente = self.cuadro5.get().strip().lower()
		gramo5 = self.cuadro5_1.get()
		sexto_ingrediente = self.cuadro6.get().strip().lower()
		gramo6 = self.cuadro6_1.get()
		dic={'jamon':0.16,'quesocrema':0.12, 'quesomozarella':0.14,
		     'kitkat':0.29,'nutella':0.17,'mermelada':0.12,
			 'lechera':0.06,'chocoretas':0.2,'durazno':0.06,
			 'oreo':0.22,'salsatomate':0.06,'quesogouda':0.21,'peperoni':0.345,
			 'chantilly':0.055,'nuez':0.5,'manzana':0.04,'nuez':0.5,
			 'canela':0.28,'cajeta':0.14,'platano':0.023,'fresa':0.13,
			 'arandano':0,'na':0,'kises menta':0.375,'quesomanchego':0.085,
			 'mermelada fresa':0.12, 'cerezas':0.11,'mermelada zarzamora':0.07,
			 'piña':0.067}
		costo = 10.15 + dic[primer_ingrediente]*float(gramo1) + dic[segundo_ingrediente]*float(gramo2) +  dic[tercer_ingrediente]*float(gramo3)+  dic[cuarto_ingrediente]*float(gramo4)+  dic[quinto_ingrediente]*float(gramo5) +  dic[sexto_ingrediente]*float(gramo6)
		costo = str(round(costo,2))
		self.CostoPantalla.set(costo)

if __name__ == "__main__":
	ventana = Tk()
	ventana.title('')
	ventana.minsize(height= 475, width=795)
	ventana.geometry('1000x500+180+80')
	ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='logo.png'))	
	app = Ventana(ventana)
	app.mainloop()