@echo off

REM Ejecutar accdb_a_csv.py
python accdb_a_csv.py

REM Verificar el código de salida del programa accdb_a_csv.py
set accdb_a_csv_exit_code=%errorlevel%

if %accdb_a_csv_exit_code% equ 0 (
    echo El programa accdb_a_csv.py ha finalizado correctamente.
    REM Ejecutar exportar_estructura.py
    python exportar_estructura.py
) else (
    echo El programa accdb_a_csv.py ha finalizado con errores. No se ejecutará exportar_estructura.py.
)
