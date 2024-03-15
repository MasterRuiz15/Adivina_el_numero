from random import *
# input

print("¡Hola! Vamos a jugar un juego.")

Y = int(input("Estoy pensando en un número entre 1 y 10. Trata de adivinar cuál es: "))

# processing

X = randint(1 , 10)

if Y == X:
    print("¡Correcto! ¡Has adivinado el número")

elif Y < X:
    print("El número que estas pensando es mas bajo. El numero era " + str(X))
else:
    print("El número que estas pensando es más alto. El numero era " + str(X))