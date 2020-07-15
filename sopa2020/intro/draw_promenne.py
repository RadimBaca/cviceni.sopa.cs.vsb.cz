import turtle

strana_ctverce = int(input("zadejte velikost ctverce: "))

malir = turtle.Turtle()
for i in range(0,50):
  malir.forward(strana_ctverce)
  malir.left(90)
  strana_ctverce = strana_ctverce + 1
