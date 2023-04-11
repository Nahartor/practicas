# IpTables

Iptables es un firewall de red que se utiliza comúnmente en sistemas operativos Linux.
En este documento se detallan algunos de los comandos mas comunes para manejar IPTables en Debian 11.
***

- Listar las reglas de iptables actuales --> **iptables -L**
- Limpiar todas las reglas actuales --> **iptables -F**
- Bloquear todo el tráfico entrante --> **iptables -P INPUT DROP**
- Permitir todo el tráfico saliente --> **iptables -P OUTPUT ACCEPT**
- Permitir el trafico entrante en un puerto específico (por ejemlo, el puerto SSH) --> **iptables -A INPUT -p tcp --dport "NºPUERTO/NOMBRE" -j ACCEPT**
- Permitir el tráfico desde una dirección o red específica (lista blanca) --> **iptables -A INPUT -s "IP/RED" -j ACCEPT**
- Bloquear el tráfico entrante de un puerto específico --> **iptables -A INPUT -p tcp --dport "NºPUERTO/NOMBRE" -j DROP**
- Guardar las reglas actuales en un archivo --> **iptables-save > "RUTA"**
- Restaurar/importar las reglas de iptables desde un archivo --> **iptables-restore < "RUTA"**

