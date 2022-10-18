import discord
from discord.ext import commands
from discord.commands import slash_command
import os  # default module
from dotenv import load_dotenv
import array


load_dotenv()  # load all the variables from the env file
# guild ids in which commands will appear useful for testing.
bot = discord.Bot(debug_guilds=[1024149439029452931])


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

cogs_list = [
    'gold',
    'shiny',
    'legend',
    'escape',
    'follow',
    'time',
    'map',
    'history',
    'nonmap',
    'nobreed',
    'drop',
    'help',
    'nature',
    'invite'
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

#bot.load_extension('cogs.gold')
#bot.load_extension('cogs.shiny')

bot.run(os.getenv('token'))  # run the bot with the token
