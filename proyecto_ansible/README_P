# Proyecto de Administración y Configuración de un service1 con Ansible contra una maquina

Este proyecto tiene como objetivo realizar diversas tareas de administración y configuración en un entorno de sistemas utilizando Ansible. Proporciona un conjunto de playbooks y roles para automatizar diferentes acciones en los sistemas.

## Glosario de términos

- Nodo administrador --> Es la máquina en la que se ejecuta el proyecto (servidor de Ansible)
- Nodos administrados --> Son las máquinas sobre las que se ejecutan las tareas presentes en los playbooks

## Requisitos previos

- Ansible 2.9 o superior instalado en la máquina desde la cual se ejecutarán las tareas (servidor de Ansible).
- Acceso y permisos de administración en los sistemas objetivo.
    Puede consultar los requisitos previos para la instalación de Ansible, así como el proceso de instalación y los pasos a seguir para ponerlo en funcionamiento en el siguiente enlace: https://github.com/Nahartor/practicas/blob/main/Documentación/Ansible.md
- Una máquina virtual sobre la que se instalara el service1 y otra máquina que debe tener instalado el software de maquina
- Conectividad SSH entre todos los nodos que intervengan en la ejecución del proyecto, tanto los nodos administrados como el nodo administrador.

## Estructura del proyecto

El proyecto está organizado de la siguiente manera:

    service1/
    ├───ficheros
    │       archivo_generico(1).php
    │       archivo_generico(2).php
    │       archivo_generico(3).php
    │       iptables
    │       script_iptables.sh
    │
    └───playbooks
        │   maestro.yml
        │   variables_entorno.yml
        │
        ├───playbooks_maquina
        │       apertura_puertos_maquina.yml
        │       crear_usuarios_de_acceso.yml
        │       instalacion_de_dependencias_maquina.yml
        │       service1tomaquinatiptables.yml
        │
        └───playbooks_service1
                cabiar_puertos.yml
                db_service1.yml
                instalacion_service1.yml
                instalar_dependencias.yml
                integracion_service1_maquina.yml
                securizar_service1.yml

- El directorio `ficheros/` contiene los archivos relacionados con los sistemas service1 y maquina, como funciones personalizadas, configuraciones de IPTABLES y scripts adicionales.
    - En el archivo `script_iptables.sh` se debe modificar el valor de la variable IP_MAQUINA con la IP de la máquina donde está instalada la maquina
- El directorio `playbooks/` se divide en `playbooks_service1/` y `playbooks_maquina/`, que contienen los playbooks específicos para cada sistema.
- El archivo `maestro.yml` es el playbook principal que orquesta la ejecución de los diferentes playbooks y roles.
- El archivo `variables_entorno.yml` contiene las variables de entorno necesarias para la configuración y personalización de los playbooks.
    Este archivo contiene las siguientes variables, las cuales se deben modificar con los valores necesarios para cada caso, a saber:
    -ANSIBLE_COLLECTIONS_PATH --> NO TOCAR
    - IP_MAQUINA --> Contiene la IP de la máquina donde tenemos instalada la maquina 
    - IP_service1 --> Contiene la IP de la máquina donde vamos a instalar service1
    - DBUSER --> Contiene el nombre de usuario de la base de datos de la máquina service1
    - DBPASS --> Contiene la contraseña asociada al usuario especificado en DBUSER

## Uso

1. Copiar la carpeta `service1` y todo su contenido a la carpeta que se desee dentro de la máquina que vaya a ejercer como nodo administrador (servidor de Ansible)
2. Navegar hasta la carpeta `service1/playbooks` con `cd [directorio_raiz]/service1/playbooks`
3. Configurar las variables de entorno en el archivo `variables_entorno.yml` y `script_iptables.sh`
4. Ejecutar el orquestador `maestro.yml`. Para ello ejecutamos `ansible-playbook maestro.yml`

## Contribuciones
¡Las contribuciones a este proyecto son bienvenidas! Si desea agregar nuevas funcionalidades, corregir errores o mejorar la documentación, no dude en comunicarlo.

## Licencia
Este proyecto es propiedad de EpresaGenerica SL.

## Autoría
Este proyecto ha sido realizado íntegramente por Don Nicolás Balboni Palma durante la realización de su periodo de prácticas en la empresa.
