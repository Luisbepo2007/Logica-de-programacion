import turtle
import time
import random

delay = 0.1

#Estos codigos son para la pantalla del juego
pantalla = turtle.Screen()
pantalla.title("Juego de la serpiente")
pantalla.bgcolor("grey")
pantalla.setup(width=600, height=600)
pantalla.tracer(0)

#estos codigos son para hacer la cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#comida de la serpiente
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)



#movimientos de la serpiente
def go_up():
        cabeza.direction = "up"

def go_down():
        cabeza.direction = "down"

def go_left():
        cabeza.direction = "left"
        
def go_right():
        cabeza.direction = "right" 


def move():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#teclas para poder mover a la serpiente
pantalla.listen()
pantalla.onkeypress(go_up, "w")
pantalla.onkeypress(go_down, "s")
pantalla.onkeypress(go_left, "a")
pantalla.onkeypress(go_right, "d")

#bucle del juego
while True:
    pantalla.update()
    
    #generara la comida en una ubicacion aleatoria
    if cabeza.distance(comida) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        comida.goto(x,y)
        
    move()
    
    time.sleep(delay)
    
pantalla.mainloop()