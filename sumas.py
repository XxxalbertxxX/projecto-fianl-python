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


speak("Hola")
speak("Bienvenido al juego de adivinar la suma.")
time.sleep(0.2)
speak("""Te voy a dar dos números del uno al diez.
    Tu misión es adivinar la suma.""")

score = 0
jugar = True
while jugar:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_sum = num1 + num2
    speak(f"¿Cuál es la suma de {num1} más {num2}?")
    user_input = int(input(f"¿Cuál es la suma de {num1} + {num2}? "))
    if user_input == correct_sum:
        score += 1
        speak("¡Has adivinado! Te has ganado un punto. ¡Te felicito!")
        print("Correcto 🎉")
    else:
        speak(f"Lo siento, la respuesta correcta era {correct_sum}.")
        print("Incorrecto ❌")
    seguir = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if seguir != 's':
        jugar = False
speak(f"Gracias por jugar. Tu puntuación final es {score} puntos.")
print(f"Puntuación final: {score}")
