from tkinter import *
from tkinter import ttk

class Interfaz:

	def __init__(self,ventana):
		self.ventana = ventana
		self.productos = ("Italia-$80","Hawaii-$75","Tres Quesos-$75","Chocomenta-$65","Dopamina-$65","Cajetosa-$65","De la casa-$60","1 a 2 ingredientes-$55","2 a 4 ingredientes-$70","4 a 6 ingredientes-$85")
		self.cajaCantidad = IntVar()
		self.cajaTotal = IntVar()
		self.total = 0
		self.dibujarComponentes()

	def dibujarComponentes(self):
		self.ventana.title("Caja Registrado")
		self.ventana.geometry("650x450")
		Label(self.ventana,text="Selecciona tu producto: ").place(x=10,y=10)
		Label(self.ventana,text="Seleciona la cantidad: ").place(x=10,y=60)
		Label(self.ventana,text="El total es: ").place(x=450,y=400)
		self.combo = ttk.Combobox(self.ventana,state="readonly")
		self.combo.place(x=10,y=35)
		self.combo["values"]=self.productos
		self.combo.current(0)
		Entry(self.ventana,textvariable=self.cajaCantidad).place(x=10,y=85)
		Entry(self.ventana,textvariable=self.cajaTotal).place(x=520,y=400)
		Button(self.ventana,text="Agregar",command=self.agregarProducto).place(x=10,y=110)

		self.tabla = ttk.Treeview(self.ventana,columns=("Cantidad","Subtotal"))
		self.tabla.heading("#0",text="Producto")
		self.tabla.heading("Cantidad",text="Cantidad")
		self.tabla.heading("Subtotal",text="Subtotal")
		self.tabla.place(x=10,y=150)

	def agregarProducto(self):
		texto = self.combo.get()
		#   Galletas-$10   [0] = Galletas   [1] = 10    
		datos = texto.split("-$")
		producto = datos[0]
		precio = datos[1]
		cantidad = self.cajaCantidad.get()
		subtotal = int(precio)*int(cantidad)
		self.tabla.insert("",END,text=producto,values=(cantidad,"$"+str(subtotal)))
		self.total = self.total + subtotal
		self.cajaTotal.set("$"+str(self.total))

obj = Interfaz(Tk())
obj.ventana.mainloop()