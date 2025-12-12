import turtle
import time
import random

delay = 0.1

#puntaje
puntaje = 0
puntajeAlto = 0

#Estos codigos son para la pantalla del juego
pantalla = turtle.Screen()
pantalla.title("Juego de la serpiente")
pantalla.bgcolor("grey")
pantalla.setup(width=700, height=600)
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

cuerpo = []

#este sera el texto que indique la puntuacion
texto = turtle.Turtle()
texto.speed(0)
texto.shape("square")
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Puntaje: 0  Puntaje mas alto: 0", align="center", font=("Courier", 24, "normal"))

#movimientos de la serpiente
def go_up():
        if cabeza.direction != "down":
            cabeza.direction = "up"

def go_down():
        if cabeza.direction != "up":
            cabeza.direction = "down"

def go_left():
        if cabeza.direction != "right":
            cabeza.direction = "left"
        
def go_right():
        if cabeza.direction != "left":
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

#pausar el juego
pausa = False
def toggle_pause():
    global pausa
    pausa = not pausa 

pantalla.onkeypress(toggle_pause, "p")

#reiniciar el juego
def restart_game():
    global puntaje, delay

    time.sleep(1)
    cabeza.goto(0,0)
    cabeza.direction = "stop"

    #al colisionar el aumento del cuerpo se muestran en la pantalla separados de la cabeza, con esto los aumentos no se veran
    for segment in cuerpo:
        segment.goto(1000,1000)
    cuerpo.clear()

    #reubica la comida en su posicion inicial
    comida.goto(0,100)

    #reinicio del puntaje
    puntaje = 0
    
    #actualiza el puntaje en la pantalla
    texto.clear()
    texto.write("Puntaje: {}  Puntaje mas alto: {}".format(puntaje, puntajeAlto), align="center", font=("Courier", 24, "normal"))

pantalla.onkeypress(restart_game, "r")


#teclas para poder mover a la serpiente
pantalla.listen()
pantalla.onkeypress(go_up, "w")
pantalla.onkeypress(go_down, "s")
pantalla.onkeypress(go_left, "a")
pantalla.onkeypress(go_right, "d")

#bucle del juego
while True:
    pantalla.update()
    
    #el juego no se detiene hasta que pongan pausa
    if not pausa:
        #Saber cuando hay una colision con los bordes
        if cabeza.xcor()>320 or cabeza.xcor()<-320 or cabeza.ycor()>290 or cabeza.ycor()<-290:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            
            #al colisionar el aumento del cuerpo se muestran en la pantalla separados de la cabeza, con esto los aumentos no se veran
            for segment in cuerpo:
                segment.goto(1000, 1000)
            
            
            #quita el aumento del cuerpo a la cabeza
            cuerpo.clear()

            #reinicio del puntaje
            puntaje = 0
            
            #actualiza el puntaje en la pantalla
            texto.clear()    
            texto.write("Puntaje: {}  Puntaje mas alto: {}". format(puntaje, puntajeAlto), align="center", font=("Courier", 24, "normal"))    
            
        #estos codigos seran para que la serpiente coma
        #generara la comida en una ubicacion aleatoria
        if cabeza.distance(comida) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            comida.goto(x,y)
            
            #aumento del cuerpo al comer
            aumento_cuerpo = turtle.Turtle()
            aumento_cuerpo.speed(0)
            aumento_cuerpo.shape("square")
            aumento_cuerpo.color("teal")
            aumento_cuerpo.penup()
            cuerpo.append(aumento_cuerpo)
            
            #aumento del puntaje
            puntaje += 10
            
            if puntaje > puntajeAlto:
                puntajeAlto = puntaje
            
            #actualiza el puntaje en la pantalla
            texto.clear()    
            texto.write("Puntaje: {}  Puntaje mas alto: {}". format(puntaje, puntajeAlto), align="center", font=("Courier", 24, "normal"))    
            
        #permitira que los segmentos del cuerpo se coloquen primero en orden inverso
        for index in range(len(cuerpo)-1, 0, -1):  
            x = cuerpo[index-1].xcor()
            y = cuerpo[index-1].ycor()
            cuerpo[index].goto(x,y)
            
        #permitira que el segmento 0 del cuerpo se coloque donde antes estaba la cabeza  
        if len(cuerpo) > 0:
            x = cabeza.xcor()
            y = cabeza.ycor()
            cuerpo[0].goto(x,y)
        
        move()
        
        #Saber cuando hay una colision con el propio cuerpo de la serpiente
        for segment in cuerpo:
            if segment.distance(cabeza) < 20:
                time.sleep(1)
                cabeza.goto(0,0)
                cabeza.direction = "stop"
        
            
                #al colisionar el aumento del cuerpo se muestran en la pantalla separados de la cabeza, con esto los aumentos no se veran
                for segment in cuerpo:
                    segment.goto(1000, 1000)
            
            
                #quita el aumento del cuerpo a la cabeza
                cuerpo.clear()
        
                #reinicio del puntaje
                puntaje = 0
            
                #actualiza el puntaje en la pantalla
                texto.clear()    
                texto.write("Puntaje: {}  Puntaje mas alto: {}". format(puntaje, puntajeAlto), align="center", font=("Courier", 24, "normal"))    
            
    time.sleep(delay)
    

pantalla.mainloop()
