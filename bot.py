import discord
from discord.ext import commands
import requests
# Inicializar el bot
intents = discord.Intents.default()
intents.message_content = True  # Para leer mensajes
bot = commands.Bot(command_prefix="!", intents=intents)
 
# Manejador de comando !start
@bot.command()
async def start(ctx):
    await ctx.send("¡Hola! Soy un bot que anuncia el pronóstico del tiempo.")
 
 
def get_weather(city : str) -> str:
 
    url = f"""https://wttr.in/{city}?format= Clima : %C+ Temperatura : %t
    + Humedad:%h+ Viento:%w + Radiacion UV: %u + Presion : %P
    """  # Formato: descripción + temperatura
    response = requests.get(url)
 
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "No te puedes conectar"
 
 
@bot.command()
async def weather(ctx, *, city: str):
    info_clima = get_weather(city)
    await ctx.send(f"El clima en: {city} es {info_clima}")

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

def get_fact() -> str:
        url = "https://uselessfacts.jsph.pl/random.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get("text")
        else:
            return "No puedes ver esa informacion"
    
@bot.command()
async def fact(ctx):
    dato_aleatorio = get_fact()
    await ctx.send(f"Aqui tienes un dato aleatorio: {dato_aleatorio}")

import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 125)
engine.setProperty('volume', 2.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

@bot.command()
async def saludo(ctx, mensaje:str):
    await ctx.send(speak(mensaje))


bot.run("MTM5MDQyNzk2NDEzODcxNzE4NA.G_HX2L.G-xI8dvwgMMYPzgB2NRsNwQjngVfw16eaH-Zb0")