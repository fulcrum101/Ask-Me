import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from OpenAI_FC import F_C
from OpenAI_QA import Q_A
from OpenAI_R import R
from OpenAI_SM import S_M
from OpenAI_ST import S_T

load_dotenv()
TOKEN = os.environ['TOKEN']

intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print('Logged in as {0}!'.format(client.user))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name="Wikipedia comments"))


@client.command(aliases=['Q'])
async def QA(ctx, *text):
    answer = Q_A(" ".join(text))
    await ctx.send(f'A:{answer}')


@client.command(aliases=['F'])
async def FC(ctx, *text):
    answer = F_C(" ".join(text))
    await ctx.send(f'{answer}')


@client.command(aliases=['S'])
async def SM(ctx, *text):
    answer = S_M(" ".join(text))
    await ctx.send(f'{answer}')


@client.command(aliases=['R'])
async def Re(ctx, *text):
    meal = text[0]
    ing = '\n'.join(text[1:])
    await ctx.send(f'{R((meal, ing))}')


@client.command(aliases=['T'])
async def ST(ctx, *text):
    answer = S_T(" ".join(text))
    await ctx.send(f'{answer}')


@client.command(aliases=['I'])
async def Info(ctx):
    with open('COMMANDS_INFO.txt') as ci:
        INFO = ci.read()
    await ctx.send(f'{INFO}')


client.run(TOKEN)
