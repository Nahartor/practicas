#!/bin/bash

# Definir la ubicación del archivo "reload"
reload_file="/tmp/reload"

# Función para realizar la tarea necesaria
check_reload_file() {
    if [ -f "$reload_file" ]; then
        touch /tmp/ejecucion
        sleep 15 # Da un margen de 15 segundos para comprobar que los archivos se estan creando correctamente
        rm "$reload_file"
    fi
}

# Bucle infinito para que el demonio se ejecute continuamente
while true; do
    check_reload_file
    sleep 1 # Esperar 1 segundo antes de volver a comprobar
done
