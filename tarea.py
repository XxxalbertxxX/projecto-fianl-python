import pyttsx3
import random
import time
engine = pyttsx3.init()
engine.setProperty('rate', 125)
engine.setProperty('volume', 2.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


speak("Bienvenido a el juego de adivinar un numero")

speak("El numero esta entre 1 y 50")


intentos = 3
puntaje = 0
while intentos > 0:

    num = random.randint(1,50)
    adi = int(input("Cual crees que es el numero:"))
    if num == adi:
        speak("Has adivinado, te felicito")
        intentos += 1
        puntaje += 1

    elif num > adi:
        speak("Tu numero es mayor que el adivinado")
        intentos -= 1
    elif num < adi:
        speak("Tu numero es menor que el adivinado")
        intentos -= 1
    print(f"Te quedan {intentos} intentos")
    if intentos == 0:
        print("Te has quedado sin intentos")
        print(f"EL numero era {adi}")
        print(f"Tu puntaje es {puntaje}")
