# Creación de un demonio (daemon) en Debian 11

En la siguiente guía voy a explicar paso a paso como crear un servicio en Debian 11.  
Un servicio es un tipo muy particular de proceso. En los sistemas operativos basados en **Unix**, como Debian 11 recibe el nombre de **demonio**.  
Un demonio es un proceso que se ejecuta en segundo plano sin necesidad alguna de interacción con el usuario.
***
Para crear un demonio primero debemos escribir su código en un archivo con extensión .sh que ubicaremos en el directorio **/usr/local/bin**  
A continuación podrás ver un ejemplo:
```sh
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
```
En el ejemplo anterior se pretende crear un demonio que compruebe en un bucle infinito la presencia de un archivo concreto en el directorio **/tmp** y en caso de encontrarlo cree otro archivo y borre el anterior. 

Esto es util para diversas funcionalidades y facilmente adaptable a las necesidades que tengamos en cada momento.  
***
Una vez que hemos creado el archivo .sh debemos hacer que sea ejecutable con el siguiente comando  
```
sudo chmod +x /usr/local/bin/nombre_archivo.sh
```  
***
Una vez hemos creado el archivo que ejecutará el demonio (es decir, lo que el demonio debe hacer mientras esté activo) deberemos crear el demonio en sí.  
Para ello debemos generar un archivo con el nombre del demonio en la carpeta **/etc/init.d** con el nombre del demonio  
A contnuación podras ver un ejemplo del código:  
```sh
#!/bin/bash
# chkconfig: 345 99 10
# description: Script to check and reload file

case "$1" in
 start)
        echo "Iniciando check_reload_file.sh"
        /usr/local/bin/check_reload_file.sh &
        ;;
 stop)
        echo "Deteniendo check_reload_file.sh"
        pkill -f "/usr/local/bin/check_reload_file.sh"
        ;;
 restart)
        $0 stop
        $0 start
        ;;
 *)
        echo "Uso: $0 {start|stop|restart}"
        exit 1
        ;;
esac

exit 0
```  
Una vez creado el archivo deberemos convertirlo en ejecutable. El comando es el mismo que el descrito en el apartado anterior.  
***
A continuación debemos añadir el recien creado demonio al registro del sistema para que este se inicie al encender la máquina.  
```
sudo update-rc.d check_reload_file defaults
```  
***
Lo siguiente que debemos hacer es comprobar que el servicio ha sido creado e inicarlo.
```
systemctl status check_reload_file.service
systemctl start check_reload_file.service
```  
***
En nuestro ejemplo hemos comprobado el correcto funcionamiento del demonio creando manualmente el archivo en la carpeta **/tmp** y observando con el comando **watch** que el demonio efectivamente hacá aquello para lo que se le habia programado. 
