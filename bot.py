import discord, random, config, objects
from discord.ext import commands

bot = commands.Bot(config.prefix)

@bot.event
async def on_ready():
    print('bot is ready')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')


@bot.command()
async def bang(ctx):
    await ctx.send("{}".format("じゃねスッペイズカウボーイ\t|\tSee you Space Cowboy"))


@bot.command()
async def rules(ctx):
    with open("C:\\Users\\Simrat's PC\\Documents\\My Stuff\\Mafeea\\rules.txt") as f:
        await ctx.send(f.read())

@bot.command()
async def cls(ctx, amount=50):
    await ctx.channel.purge(limit=amount)

@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, ques):
    responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful.",
            "Omaewa Mou Shinderu.",
            "Yare Yare Daze"]

    await ctx.send(f'Question: {ques}\n Answer: {random.choice(responses)}')

bot.run(config.token)

