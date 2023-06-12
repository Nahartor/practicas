# ACCDB a CSV

Este proyecto emplea `Python`, junto con la librería `pyodbc` y el motor de bases de datos de `Microsoft Access Driver` para procesar un archivo de extensión .accdb y proporcionar lo siguiente:  


* Un script de importación de la base de datos (solo estructura) de extensión .sql
* Un archivo de extensión .csv para cada una de las tablas.  
Cada archivo CSV tendrá por titulo <nombre_de_la_tabla>.csv y contendrá toda la información de la misma.  
Los archivos CSV se volcarán a un directorio para su posterior utilización.

## Requisitos previos

* Windows 10 o superior.
* Motor de bases datos Microsoft Access Driver instalado.
* Pyton 3
* Librerías necesaraias:
  * pyodbc
  * os

## Estructura del proyecto

\accdb_a_csv  
   │   accdb_a_csv.py  
   │   exportar_estructura.py  
   │   index.bat  
   │   README.md  
   │  
   └───convertidas   

## Instrucciones de uso

1. Descarga este repositorio en tu equipo.
2. Asegurate de que todas las dependencias que furan en el apartado de `Requisitos previos`.
3. Ejecuta el archivo index.bat en Windows PowerShell.

Tras la ejecución del script aparecera en la carpeta `accdb_a_csv` el archivo `database_creation_script.sql` con el que podrás importar la base de datos en tu gestor de BBDD y la carpeta `convertidas` se llenará con los tantos archivos CSV como tablas tenga tu base de datos.

## Contribuciones

¡Las contribuciones a este proyecto son bienvenidas! Si desea agregar nuevas funcionalidades, corregir errores o mejorar la documentación, no dude en comunicarlo al propietario de este repositorio.

## Licencia

El grueso de este proyecto es de software libre bajo licencia tipo GNU (consulte el archivo LICENSE.md para saber más). 

Sin embargo una de sus dependencias (Microsoft Access Driver), a pesear de ser gratuito, es un software propietario de Microsoft bajo licencia Microsoft CLUF (EULA). Consulte el archivo LICENSE_MS para saber mas.

## Autoría 

Este proyecto ha sido realizado íntegramente por Nicolás Balboni Palma, Administrador de sistemas informáticos en red /DevOps.
