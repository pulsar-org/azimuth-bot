import discord

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "test", description = "Latest testing command")
async def hello(ctx):
    embed = discord.Embed(
        title="My Amazing Embed",
        description="Embeds are super easy, barely an inconvenience.",
        color=discord.Colour.blurple(),  # Pycord provides a class with default colors you can choose from
    )
    embed.add_field(name="A Normal Field",
                    value="A really nice field with some information. **The description as well as the fields support markdown!**")

    embed.add_field(name="Inline Field 1", value="Inline Field 1", inline=True)
    embed.add_field(name="Inline Field 2", value="Inline Field 2", inline=True)
    embed.add_field(name="Inline Field 3", value="Inline Field 3", inline=True)

    embed.set_footer(text="Footer! No markdown here.")  # footers can have icons too
    embed.set_author(name="Pycord Team", icon_url="https://example.com/link-to-my-image.png")
    embed.set_thumbnail(url="https://example.com/link-to-my-thumbnail.png")
    embed.set_image(url="https://example.com/link-to-my-banner.png")

    await ctx.respond("Hello! Here's a cool embed.", embed=embed)  # Send the embed with some text

@bot.command(description="Sends the bot's latency.") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {bot.latency}ms")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")


bot.run("MTA5ODgwODE0MDQzNjM1NzIzMg.GRMUha.t1YMF2IC1_N-bWuAkfLkEqHXjEnHTpV4VB4DsY")