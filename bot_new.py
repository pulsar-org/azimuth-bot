import discord
import os # default module
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.command(description="Sends the bot's latency.") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {bot.latency}ms")

# create Slash Command group with bot.create_group
greetings = bot.create_group("greetings", "Greet people")

@greetings.command()
async def hello(ctx):
  await ctx.respond(f"Hello, {ctx.author}!")

@greetings.command()
async def bye(ctx):
  await ctx.respond(f"Bye, {ctx.author}!")

bot.run(os.getenv('TOKEN')) # run the bot with the token