<?php
// Comentario de una línea

/*
Comentario de varias líneas
Este archivo muestra un ejemplo genérico de PHP.
*/

// Definición de variables
$nombre = "Juan";
$edad = 25;

// Función para obtener el saludo
function obtenerSaludo($nombre) {
    $saludo = "¡Hola, " . $nombre . "!";
    return $saludo;
}

// Función para verificar si una persona es mayor de edad
function esMayorDeEdad($edad) {
    if ($edad >= 18) {
        return true;
    } else {
        return false;
    }
}

// Sentencia lógica
if (esMayorDeEdad($edad)) {
    echo obtenerSaludo($nombre) . " Eres mayor de edad.";
} else {
    echo obtenerSaludo($nombre) . " Eres menor de edad.";
}

// Variables de entorno
$nombre_usuario = $_ENV["USERNAME"];
$ruta_actual = $_SERVER["REQUEST_URI"];

// Mostrar información del usuario
echo "Nombre de usuario: " . $nombre_usuario;
echo "Ruta actual: " . $ruta_actual;

// Ejemplo de bucle
for ($i = 1; $i <= 5; $i++) {
    echo "Número: " . $i;
}

// Ejemplo de array
$numeros = array(1, 2, 3, 4, 5);
foreach ($numeros as $numero) {
    echo "Número: " . $numero;
}

?>
