import keyboard
import turtle
import time

malir = turtle.Turtle()
for i in range(0, 4):
    malir.forward(200)
    malir.left(90)
malir.up()
malir.goto(100, 100)
while True:
    malir.forward(1)
    time.sleep(0.01)
    malir.forward(1)
    time.sleep(0.01)
    if keyboard.is_pressed('q'):
        print('Konec hry.')
        break 
    if keyboard.is_pressed('a'):
        malir.left(90)
    if keyboard.is_pressed('d'):
        malir.right(90)
    if malir.xcor() < 0 or malir.xcor() > 200 or malir.ycor() < 0 or malir.ycor() > 200:
        print('Dostal jsi se mimo hrací pole. Konec hry.')
        break;