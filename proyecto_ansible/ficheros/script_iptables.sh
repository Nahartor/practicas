#!/bin/bash

# Variables de entorno 
IP_MAQUINA="255.255.255.255" # PONER AQUÍ TU IP

# Crear el listado de IPs permitidas en ipset
ipset create permitidas hash:ip

# Añadir la dirección IP de la TreeMT a la lista de IPs permitidas en ipset
ipset add permitidas $IP_MAQUINA

# Guardar la configuración de ipset
ipset save > /etc/iptables/current.ipset

# Limpiar reglas de firewall
iptables -t filter -F INPUT
iptables -t filter -F FORWARD
iptables -t filter -F OUTPUT
iptables -t raw -F PREROUTING
iptables -t nat -F POSTROUTING

# Aceptar conexiones locales
iptables -t filter -A INPUT -i lo -j ACCEPT

# Aceptar conexiones establecidas y relacionadas
iptables -t filter -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Aceptar conexiones permitidas
iptables -t filter -A INPUT -m set --match-set permitidas src -j ACCEPT

# Aceptar conexiones permitidas en FORWARD
iptables -t filter -A FORWARD -m set --match-set permitidas src -j ACCEPT

# Aceptar conexiones al puerto 80
iptables -t filter -A INPUT -p tcp --dport 80 -j ACCEPT

# Aceptar conexiones al puerto 443
iptables -t filter -A INPUT -p tcp --dport 443 -j ACCEPT

# Aceptar conexiones al puerto 4443
iptables -t filter -A INPUT -p tcp --dport 4443 -j ACCEPT

# Aceptar conexiones al puerto 5038
iptables -t filter -A INPUT -p tcp --dport 5038 -j ACCEPT

# Aceptar conexiones al puerto 4445
iptables -t filter -A INPUT -p tcp --dport 4445 -j ACCEPT

# Configurar política predeterminada del firewall
iptables -t filter -P INPUT DROP
iptables -t filter -P FORWARD DROP
iptables -t filter -P OUTPUT ACCEPT

# Guardar la configuración del firewall
iptables-save > /etc/iptables/current.rules

# Aplicar configuración de iptables
iptables-restore < /etc/iptables/current.rules
