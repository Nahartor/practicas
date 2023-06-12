import csv
import pyodbc

# Establecer la cadena de conexión a la base de datos .accdb
conn_str = r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\ruta\al\archivo.accdb"

# Conectarse a la base de datos
conn = pyodbc.connect(conn_str)

# Obtener el cursor
cursor = conn.cursor()

# Obtener los nombres de las tablas
table_names = cursor.tables(tableType='TABLE')

# Almacenar los nombres de las tablas en una lista
table_list = []

# Agregar los nombres de las tablas a la lista
for table in table_names:
    table_list.append(table.table_name)

# Iterar sobre cada tabla
for table in table_list:
    # Establecer la consulta SQL para obtener los datos de la tabla actual
    query = f'SELECT * FROM {table}'
    
    # Establecer el nombre del archivo CSV de salida para la tabla actual
    csv_file = f'C:\\ruta\\al\\proyecto\\accdb_a_csv\\convertidas\\{table}.csv'

    # Establecer el separador de campo y el delimitador de texto para el archivo CSV
    csv_delimiter = ','
    csv_quotechar = '"'

    # Ejecutar la consulta
    cursor.execute(query)

    # Obtener los nombres de las columnas
    column_names = [column[0] for column in cursor.description]

    # Abrir el archivo CSV y escribir los datos
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=csv_delimiter, quotechar=csv_quotechar)
        
        # Escribir los nombres de las columnas como la primera fila
        writer.writerow(column_names)
        
        # Escribir los datos en las filas siguientes
        for row in cursor:
            writer.writerow(row)

# Cerrar el cursor y la conexión
cursor.close()
conn.close()
