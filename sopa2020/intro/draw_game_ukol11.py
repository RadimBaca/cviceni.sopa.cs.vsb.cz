import keyboard
import turtle
import time

velikost_ctverce = int(input("Zadejte velikost hrací plochy: "))

malir = turtle.Turtle()
for i in range(0, 4):
    malir.forward(velikost_ctverce)
    malir.left(90)
	
malir.up()
malir.goto(100, 100)

posun = 1;
while True:
    malir.forward(posun)
    time.sleep(0.01)
    malir.forward(posun)
    time.sleep(0.01)
    if keyboard.is_pressed('q'):
        print('Konec hry.')
        break 
    if keyboard.is_pressed('a'):
        malir.left(90)
    if keyboard.is_pressed('d'):
        malir.right(90)
    if keyboard.is_pressed('s'):
        if (posun == 1):
            posun = 0
        else:
            posun = 1
    if malir.xcor() < 0 or malir.xcor() > velikost_ctverce or malir.ycor() < 0 or malir.ycor() > velikost_ctverce:
        print('Dostal jsi se mimo hrací pole. Konec hry.')
        break;