import mysql.connector  #pip install mysql-connector-python

class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='crepas', 
                                            user = 'root',
                                            password ='Nanda')



    def inserta_producto(self,crepa,costo, unidades, precio, utilidad, fecha):
        cur = self.conexion.cursor()
        sql='''INSERT INTO ventas (Crepa, Costo, Unidades, Precio, Utilidad, Fecha) 
        VALUES('{}', '{}','{}', '{}','{}','{}')'''.format(crepa, costo, unidades, precio, utilidad, fecha)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()


    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM ventas " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def mostrar_productos_hoy(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM crepas.ventas WHERE Fecha =  curdate();" 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def mostrar_precios(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM crepas.crepas " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_producto(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM ventas WHERE Crepa = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 

    def elimina_productos(self,nombre):
        cur = self.conexion.cursor()
        sql="DELETE FROM crepas.ventas WHERE Crepa = {}".format(nombre)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()
    
    def actualiza_productos(self,Id, crepa,costo, unidades, precio, utilidad, fecha):
        cur = self.conexion.cursor()
        sql ='''UPDATE ventas SET  Crepa ='{}', Costo = '{}' , Unidades = '{}', Precio = '{}', Utilidad = '{}', Fecha = '{}'
        WHERE Id = '{}' '''.format(crepa,costo, unidades, precio, utilidad, fecha, Id)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return a  
