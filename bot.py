from nextcord.ext import commands
from botty import setup, reply
from typing import List
from dotenv import dotenv_values
from utils import Confirm

setup("botty")
config = dotenv_values(".env")
bot = commands.Bot("$")

@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send("ping")

@bot.command('.')
async def reply_user(ctx: commands.Context, *, message: str):
    res = ''
    async with ctx.typing():
        res = reply(message, discord=True)
    if "links:-" in res and "https://" in res and not await Confirm("I didnt understand what you said\nShould I search?").prompt(ctx):
        await ctx.send("sorry I didnt understand what you said.")
    elif type(res)==tuple:
        res = res[0].split('\n')
        res[0] = "***"+res[0][1:]+"***"
        await ctx.send('\n'.join(res))
    else:
        await ctx.send(res.replace('###', ''))

bot.run(config["TOKEN"])
