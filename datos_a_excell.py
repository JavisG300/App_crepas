import mysql.connector
import openpyxl

conexion = mysql.connector.connect( host='localhost', database ='crepas', user = 'root',password ='Nanda')
# Create a cursor
cursor = conexion.cursor()

# Execute a query
query = 'SELECT crepa, COUNT(crepa) AS frecuencia, AVG(costo) AS costo_promedio, AVG(precio) AS precio_promedio FROM ventas GROUP BY crepa ORDER BY crepa'
cursor.execute(query)

# Fetch the data
data = cursor.fetchall()

workbook = openpyxl.Workbook()

# Add a sheet to the workbook
worksheet = workbook.active

# Write the data to the sheet
for row in data:
    worksheet.append(row)

# Save the workbook
workbook.save('datos_2.xlsx')