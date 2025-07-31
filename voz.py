import pyttsx3

# Inicializar el motor

engine = pyttsx3.init()

# Configurar parámetros

engine.setProperty('rate', 180)  # Tasa de habla

engine.setProperty('volume', 0.9)  # Volumen

# Selecciona una voz

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 - hombre, 1

# Texto a vocalizar

text = "Hola como estas?"


# Vocalizar el texto

engine.say(text)

# Ejecutar la síntesis

engine.runAndWait()
