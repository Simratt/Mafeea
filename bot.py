import discord
import random
from discord.ext import commands
import config, objects

bot = commands.Bot(config.prefix)

@bot.event
async def on_ready():
    print('bot is ready')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')


@bot.command()
async def bang(ctx):
    await ctx.send("See you Space Cowboy...")

bot.run(config.token)
