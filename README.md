# Logica-de-programacion
Alumno: Luis Guillermo Betancourt Poma

Fecha: 11/12/2025

Materia: Logica de programacion

Objetivo

El objetivo del programa es simular el juego de la serpiente, donde el usuario debe controlar la serpiente y hacer que esta crezca y acumule puntos al comer las frutas, mientras lo hace debera evitar colisionar con los bordes y con sigo misma para no perder. El proposito final sera alcanzar la mayor puntuacion antes de colisionar.

Explicacion de las principales funcionalidades del codigo

-Interfaz gráfica con Turtle

El juego utiliza la librería turtle para crear la pantalla principal del juego,a la serpiente,a la comida y tambien el marcador de puntaje

-Movimiento de la serpiente

La serpiente puede moverse en cuatro direcciones:

•	W → arriba

•	S → abajo

•	A → izquierda

•	D → derecha

El movimiento se realiza en pasos de 20 píxeles para mantener una cuadrícula uniforme.

-Generación aleatoria de comida

Cada vez que la serpiente come, la comida aparece en una nueva posición generada aleatoriamente dentro de la pantalla.

-Crecimiento del cuerpo

Cuando la serpiente come se agrega un nuevo segmento al cuerpo y el segmento generado sigue la trayectoria de la cabeza de forma ordenada

-Sistema de puntaje

El juego incluye el puntaje actual y el puntaje más alto alcanzado en el juego. Cada comida suma 10 puntos. El puntaje se visualiza en la parte superior de la pantalla.

-Detección de colisiones

El juego finaliza cuando la serpiente choca contra los bordes de la pantalla o choca contra su propio cuerpo. Cuando la colison ocurra la serpiente vuelve al centro y su cuerpo se elimina, mientras que el puntaje se reinicia y se guarda siempre y cuando supere el puntaje más alto

-Bucle principal del juego

El programa utiliza un bucle while True lo cual actualiza la pantalla, permite que la serpiente se mueva, revisa si hubo colisiones y controla el tiempo mediante time.sleep(). Lo cual mantiene el juego funcionando de forma continua.

Ademas se encuentran dos teclas que alteran el bucle:

•	P → pausa/reanudar

•	r → reinicio
