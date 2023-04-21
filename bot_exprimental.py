from dotenv import load_dotenv
import os  # default module
import discord

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "test", description = "Latest testing command")
async def hello(ctx):
    embed = discord.Embed(
        title="Azimuth",
        description="Embeds are super easy, barely an inconvenience.",
        color=discord.Colour.dark_gold(),  # Pycord provides a class with default colors you can choose from
    )
    embed.add_field(name="A Normal Field",
                    value="A really nice field with some information. **The description as well as the fields support markdown!**")

    embed.add_field(name="Inline Field 1", value="Inline Field 1", inline=True)
    embed.add_field(name="Inline Field 2", value="Inline Field 2", inline=True)
    embed.add_field(name="Inline Field 3", value="Inline Field 3", inline=True)

    embed.set_footer(text="Made by the Azimuth Team")  # footers can have icons too
    embed.set_author(name="Azimuth", icon_url="http://nextcloud.swifts.wiki/s/iJCXFjMkCWnHT4s/download/pulsar.png")
    embed.set_thumbnail(url="http://nextcloud.swifts.wiki/s/WCs5gZ4HAj3ASQE/download/question-mark-circle-svgrepo-com.png")
    embed.set_image(url="http://nextcloud.swifts.wiki/s/DEBQjRSwnXP6jrk/download/Bliss.png")

    await ctx.respond("Hello! Here's a cool embed.", embed=embed)  # Send the embed with some text

bot.run(os.getenv('TOKEN'))  # run the bot with the token