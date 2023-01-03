import mysql.connector
import openpyxl

conexion = mysql.connector.connect( host='localhost', database ='crepas', user = 'root',password ='Nanda')
# Create a cursor
cursor = conexion.cursor()

# Execute a query
query = 'SELECT * FROM ventas'
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
workbook.save('prueba_extraer_datos_1.xlsx')