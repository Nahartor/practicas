# Guia básica para cambiar la IP de una máquina Debian11

Si tenemos interfaz gráfica el proceso es senticllo, pero normalmente no la tenemos, de manera que a continación paso a explicar los pasos a seguir para realizar esta configuración de manera simple.

* Primero debemos localizar el archivo de configuración de red.  
  Este archivo se encuentra en /etc/network/interfaces
* A continuación debemos editar este archivo. Puedes usar cualquier editor de texto, yo uso nano.  
  ```  
  # This file describes the network interfaces available on your system
  # and how to activate them. For more information, see interfaces(5).

  # The loopback network interface
  auto lo
  iface lo inet loopback

  # The primary network interface
  # allow-hotplug ens18
  # iface ens18 inet dhcp

  # Static IP address
  auto ens18
  iface ens18 inet static
          address 192.168.6.211
          netmask 255.255.248.0
          network 192.168.6.0
          broadcast 192.168.6.255
          gateway 192.168.0.205
  ```  
  Nota: puedes encontrar el nombre de tu interfaz de red con el comando ```ifconfig -a```
* También es necesario indicar la dirección del servidor DNS. En esta configuración, el servidor DNS funciona en el router/modem ADSL, por lo que el parámetro para nameserver debe tener el valor 192.168.7.4, en el archivo /etc/resolv.conf  
  ```
  search avanzada7.com
  nameserver 192.168.7.4
  nameserver 8.8.8.8
  ```
  
* A continuación debemos reiniciar la interfaz de red para aplicar los cambios.  
  ```
  sudo ifdown enp0s18
  ```  
  ```sudo ifup enp0s18```  

* Puedes comprobar si la configuración se ha aplicado con los comandos:  
  ```
  ifconfig
  ``` (requiere instalación del paquete net-tools)  
  ```ip -4 addr```

Nota: modifica el nombre del puerto o el resto de los parametros a tu conveniencia.