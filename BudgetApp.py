import turtle

# Настройки для сердца
heart_color = "red"
heart_fill_color = "pink"
heart_thickness = 2

# Настройки для надписи
text_color = "purple"
text_font = ("Arial", 16, "bold")

# Создаем окно для рисования
window = turtle.Screen()
window.bgcolor("white")

# Создаем черепашку и настраиваем ее
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Рисуем сердце
t.pensize(heart_thickness)
t.color(heart_color, heart_fill_color)
t.begin_fill()
t.left(45)
t.forward(150)
t.circle(60, 180)
t.right(90)
t.circle(60, 180)
t.forward(150)
t.end_fill()

# Перемещаем черепашку для начала рисования текста
t.penup()
t.goto(0, 50)
t.color(text_color)
t.write("Я ЛЮБЛЮ ТАНЮ", align="center", font=text_font)

# Оставляем окно открытым до закрытия пользователем
turtle.done()
asd
asd
asd
asd
asd
