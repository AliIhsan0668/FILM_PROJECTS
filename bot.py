import discord
from discord.ext import commands
import sqlite3
import random
import os
from config import TOKEN 

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="*", intents=intents)

def rastgelefilm():
    conn = sqlite3.connect("IMDb_Data_final.db")
    cur = conn.cursor()
    cur.execute("SELECT title, imdb_score FROM imdb_data WHERE Title LIKE '%Movie%' ORDER BY RANDOM() LIMIT 1;")
    result = cur.fetchone()
    conn.close()
    return result

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı!')

@bot.command(name="rastgelefilmke")
async def rastgelefilmke(ctx):
    film = rastgelefilm()
    if film:
        title, score = film
        await ctx.send(f"Film Önerisi: {title}\nIMDb Puanı: {score}")
    else:
        await ctx.send("Şu anda film öneremiyorum, veritabanı yok kaybolmuşşşş.")

@bot.command(name="info")
async def info(ctx):
    await ctx.send("Merhaba! `*rastgelefilmke` komutunu kullanarak rastgele bir film önerisi alabilirsin")

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"Bir hata oluştu: {str(error)}")

if __name__ == "__main__":
    bot.run(TOKEN)
