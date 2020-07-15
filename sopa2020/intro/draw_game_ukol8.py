import keyboard
import turtle

malir = turtle.Turtle()
while True:
    malir.forward(1)
    if keyboard.is_pressed('q'):
        print('Konec hry.')
        break 
    if keyboard.is_pressed('a'):
        malir.left(90)
    if keyboard.is_pressed('d'):
        malir.right(90)		