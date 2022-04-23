import discord
from discord.ext import commands

TOKEN = "TOKEN" # BOT TOKEN HERE - ENABLE ALL INTENTS

message = "PUT YOUR MESSAGE TO SEND TO USERS HERE" # PUT MSG TO SEND TO USERS HERE
role = "ROLE NAME TO MSG " # PUT ROLE NAME TO MSG TO HERE

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents, command_prefix='>')

@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name + "#" + bot.user.discriminator)
    print("Ready")


@bot.command()
@commands.has_permissions(administrator = True)
async def msg_role(ctx):
    for member in ctx.guild.members:
        for role in member.roles:
            if role.name == str(role):
                try:
                    await member.send(str(message))
                    print("messaged: " + str(member.id))
                except Exception as e:
                    print("Failed To msg! " + str(member.id))


bot.run(str(TOKEN))
