#Напишите функцию, которая рисует квадрат с помощью библиотеки turtle
import turtle

# Список координат точек для квадрата
square_coordinates = [
    (100, 100),  # Верхний правый угол
    (100, -100),  # Нижний правый угол
    (-100, -100),  # Нижний левый угол
    (-100, 100)  # Верхний левый угол
]


def draw_figure(coordinates):
    turtle.penup()
    turtle.setpos(coordinates[0])
    turtle.pendown()

    for coord in coordinates[1:]:
        turtle.setpos(coord)

    turtle.setpos(coordinates[0])


wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Рисование квадрата")

figure_turtle = turtle.Turtle()
figure_turtle.speed(1)

# Рисование квадрата по координатам
draw_figure(square_coordinates)

wn.exitonclick()