import mysql.connector  #pip install mysql-connector-python
 
class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost', database ='crepas', user = 'root', password ='Nanda')



    def inserta_producto(self,Id, Costo, Unidades, Precio, Utilidad, Fecha):
        cur = self.conexion.cursor()
        sql='''INSERT INTO ventas (Id, Costo, Unidades, Precio, Utilidad, Fecha) 
        VALUES('{}', '{}','{}', '{}','{}')'''.format(Id, Costo, Unidades, Precio, Utilidad, Fecha)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()


    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM crepas " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_producto(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM crepas WHERE NOMBRE = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 

    def elimina_productos(self,nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM crepas WHERE NOMBRE = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()
  