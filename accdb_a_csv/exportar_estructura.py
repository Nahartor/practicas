import pyodbc
import os

# Establecer la cadena de conexión a la base de datos .accdb
conn_str = r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\ruta\al\archivo.accdb"

# Conectarse a la base de datos
conn = pyodbc.connect(conn_str)

# Obtener el cursor
cursor = conn.cursor()

# Obtener los nombres de las tablas a partir de los archivos CSV
csv_directory = r"C:\ruta\al\proyecto\accdb_a_csv\convertidas"
table_names = []
for file_name in os.listdir(csv_directory):
    if file_name.endswith(".csv"):
        table_name = os.path.splitext(file_name)[0]
        table_names.append(table_name)

# Lista para almacenar las instrucciones SQL de creación
sql_statements = []

# Recorrer cada tabla
for table_name in table_names:
    # Obtener el contenido del archivo CSV
    file_path = os.path.join(csv_directory, table_name + ".csv")
    with open(file_path, "r", encoding="latin-1") as csv_file:
        csv_content = csv_file.read()

    # Obtener los campos de la tabla a partir del contenido del archivo CSV
    # Asegurarse de separar correctamente las columnas según el delimitador utilizado en los archivos CSV
    columns = csv_content.split(";")  # Reemplaza ";" por el delimitador real de tus archivos CSV

    # Crear la instrucción SQL de creación de la tabla
    create_table_sql = f"CREATE TABLE {table_name} ("

    # Recorrer los campos de la tabla
    field_definitions = []
    for column in columns:
        column_name = column.strip()  # Eliminar espacios en blanco alrededor del nombre de la columna
        data_type = "VARCHAR(255)"  # Define el tipo de datos adecuado para tus columnas

        # Definir la definición del campo en la instrucción CREATE TABLE
        field_definition = f"{column_name} {data_type}"
        field_definitions.append(field_definition)

    # Agregar las definiciones de los campos a la instrucción CREATE TABLE
    create_table_sql += ", ".join(field_definitions)
    create_table_sql += ")"

    # Agregar la instrucción CREATE TABLE a la lista de instrucciones SQL
    sql_statements.append(create_table_sql)

# Cerrar el cursor y la conexión
cursor.close()
conn.close()

# Guardar las instrucciones SQL en un archivo
with open("database_creation_script.sql", "w") as sql_file:
    sql_file.write("\n".join(sql_statements))

print("Script de creación de la base de datos generado correctamente.")
