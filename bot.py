# 2/16/2024. I've got no clue how to code in python icl.
# 2/17/2024. I've still got no clue what the fuck I'm doing but I have learned that I need to be using bot instead of client.

import discord
import logging
import os

from discord.ext import commands
from shit import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix= '!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.change_presence(activity=discord.Game(name="toys :)"))

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")


@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def ms(ctx):
    await ctx.send(f'{bot.latency}')

@bot.hybrid_command(name='hi')
async def hi(ctx):
    await ctx.send(":D It workige!!!")

@bot.command()
async def sync(ctx):
    if ctx.message.author.id == (OwnerID):
        await bot.tree.sync()
        await ctx.send('Synced Successfully')
    else:
        await ctx.send("You're not an owner :'(")

@bot.hybrid_command()
async def echo(ctx: commands.Context, message: str):
    await ctx.send(message)

@bot.hybrid_command()
async def multiply(ctx, a:int,b:int):
    await ctx.send(f"{a} * {b} = {a*b}")

@bot.command()
async def test(ctx):
    await ctx.send(OwnerID)

@bot.command
async def profilepic(ctx):
    if ctx.message.author.id == (OwnerID):
        await edit ()

bot.run(Token, log_level=logging.WARN)
