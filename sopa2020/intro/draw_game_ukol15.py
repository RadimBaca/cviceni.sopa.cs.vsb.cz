import keyboard
import turtle
import time
import random


file = open('data_hlasek.txt', encoding ="utf-8")
hlasky = {}
for line in file:
    klic, hlaska = line.split('#')
    hlasky[klic] = hlaska
	
velikost_ctverce = int(input(hlasky['plocha']))

pole_zelv = []
for i in range(0,4):
    zelva = turtle.Turtle();
    zelva.shape("turtle")
    zelva.up()
    zelva.goto(random.random() * velikost_ctverce, random.random() * velikost_ctverce)
    pole_zelv.append(zelva)

malir = turtle.Turtle()
for i in range(0, 4):
    malir.forward(velikost_ctverce)
    malir.left(90)	
malir.up()
malir.goto(100, 100)

napisy = turtle.Turtle()
napisy.up()
napisy.hideturtle()
napisy.goto(0, -30)
napisy.write(hlasky['uvod1'])
napisy.goto(0, -50)
napisy.write(hlasky['uvod2'])
napisy.goto(0, -70)
napisy.write(hlasky['uvod3'])

sebrano = 0
posun = 1;
while True:
    malir.forward(posun)
    time.sleep(0.01)
    malir.forward(posun)
    time.sleep(0.01)
    if keyboard.is_pressed('q'):
        print(hlasky['konec_q'])
        break 
    if sebrano == len(pole_zelv):
        print(hlasky['konec_win'])
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
        print(hlasky['konec_out'])
        break;
    for i in range(0, 4):		
        if malir.distance(pole_zelv[i].pos()) < 4:
            sebrano = sebrano + 1
            pole_zelv[i].goto(velikost_ctverce + 40, 40 * sebrano)
            print('sebrano ' + str(sebrano))
        