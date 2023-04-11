import discord
from discord.ext import commands

TOKEN = "MTA5NDM2NDc5MjEyNDM1MDU5Ng.GPVJ6g.Ex-8WUpgRiPYr17EVpaqBCEg0LTCaU2geZb7bs"

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.command()
async def ping(ctx):
    await ctx.send("Bing Chilling")

client.run(TOKEN)
