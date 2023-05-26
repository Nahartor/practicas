# ELIMINAR/CAMBIAR CONTRASEÑA DESCONOCIDA W10 

En la siguiente guía explicaremos paso a paso como eliminar o cambiar la contraseña de un usuario de Windows 10 en caso de que no sepamos cual es y no tengamos acceso a la cuenta de administrador.  

## Materiales necesarios

* Memoria USB de (al menos) 8GB de capacidad. (¡Todos los datos que haya dentro seran borrados!)
* Herramienta de creación de medios de Windows.  
Si no la tienes ya puedes descargarla en el siguiente enlace:  
https://go.microsoft.com/fwlink/?LinkId=691209  

## Procedimiento

* En un ordenador con Windows 10 descargaremos y abriremos (como administrador) la herramienta de creación de medios de Windows y seguiremos los siguientes pasos. (El proceso puede durar entre 30 y 60 minutos dependiendo del equipo y la velocidad del USB).  
  * Aceptamos los terminos y avisos aplicables.
  * Seleccionamos "Crear medios de instalación para otro PC".
  * Seleccionamos el idioma (español), edicion del SO (Windows 10) y arquitectura (64 bits) para nuestro equipo. (En este paso si nuestro ordenador tiene las mismas características que el equipo que estamos recuperando podemos marcar la opción "Usa las opciones recomendadas para este equipo").
  * Seleccionamos "Unidad flash USB".
  * Seleccionamos la unidad. (Si no se encuentra podemos pulsar "Actualizar la lista de unidades").
  * A partir de aqui solo debemos dejar trabajar al programa y darle a aceptar a todo lo que nos salga.  
  **AVISO:** el programa formateará la unidad por si solo. Si en algún momento nos avisa de que debemos formatear pulsaremos aceptar. Se nos abrira la ventana de formateo. **DEBES IGNORARLA**. De lo contrario el proceso se detendrá y tendrás que volver a empezar.  
* En el equipo que deseamos recuperar inicaremos el sistema y accederemos a la BIOS y cambiaremos el orden de arranque para que cargue nuestro USB en primer lugar o bien accederemos al modo FlashBoot para cargar directamente nuestro USB.  
  * Para accedeer a la BIOS debemos iniciar el ordenador y pulsar repetidamente alguna de las siguientes teclas (varía en función del fabricante): F2, F10, Supr.
  * Para acceder al mood de arranque rápido (FlashBoot) debemos iniciar el ordenador y pulsar una de las siguientes teclas (varía en función del fabricante): F9, F10, F12.
* Una vez que cargue el instalador de Windows pulsaremos en siguiente. (Las opciones de la primera pagina nos dan igual, generalmente autodetectarña "español").
* En la ventana donde aparece el boton de "Instalar ahora" buscaremos la opción "Reparar el equipo".
* Pulsamos "Solucionador problemas".
* Pulsamos "Simbolo del sistema". Esto nos abrirá una terminal sobre la que lanzaremos los siguientes comandos: 
  * ```C:``` --> Esto nos situará en la raiz del directorio C:\
  * ```dir``` --> Nos muestra el contenido de C:\ ,esto resulta util para comprobar que es el disco en el que esta instalado el SO, de lo contrario deberemos probar con otras unidades como D: o F: en el punto antrior y repetir el comando "dir" hasta dar con la carpeta "Windows". 
  * ```cd Windows\System32```
  * ```ren Utilman.exe Utilman.bak``` --> Si pulsamos TAB a mitad de escribir el nombre del archivo nos lo autocompletará y asi nos aseguraremos de que lo estamos escribiendo bien.
  * ```copy cmd.exe Utilman.exe```
* Salir del simbolo del sistema.
* Apagar el equipo.
* Retirar el medio USB.
* Iniciar el equipo.
* Doble click en "Accesibilidad" --> Abrirá un simbolo de sistema.
* En la consola que se nos acaba de abrir escribiremos ```control userpasswords2``` y pulsaremos "Enter" --> Abrirá el gestor de usuarios con permisos de administrador.
* Buscar el usuario en cuestión.
* Pulsar en "Restablecer contraseña". En este paso puedes establecer una nueva contrseña o dejarla en blanco.
* Aceptar-Aceptar
* ¡LISTO!

Una vez realizados todos los pasos solo debes pulsar sobre tu usuario, introducir la nueva contraseña (o dejar el campo en blanco si no especificaste ninguna) y pulsar la flecha para ingresar en la cuenta del usuario.  

Una vez que tengas acceso podras cambiar la contraseña desde dentro en caso de querer hacerlo en un futuro.  

Espero que esta guía te haya sido de utilidad. 