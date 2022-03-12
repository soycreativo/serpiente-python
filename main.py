from turtle import Turtle, Screen
import time

from snake import Snake
from food import Food

from scoreboard import ScoreBoard

#Creación del tablero del juego
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Programate snake game")

screen.tracer(0)

#Serpiente
snake = Snake()

food = Food()

#Creamos el objeto y tablero
scoreboard = ScoreBoard()

#Método de escucha
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detectar colisión de comida
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

#Detector de colisiones
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor () < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detector de segmentos de la serpiente
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            

screen.exitonclick()