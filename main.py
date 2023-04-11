import discord
from discord.ext import commands

TOKEN = "MTA5NDM2NDc5MjEyNDM1MDU5Ng.GCLUgW.Yj1_l1xNJRh57jW5UqrusJINGYG2LgB4Nbi71I" # replace with your own token

client = commands.Bot(command_prefix="/")

@client.command()
async def ping(ctx):
    await ctx.send("Bing Chilling")

client.run(TOKEN)
