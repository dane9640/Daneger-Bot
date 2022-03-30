import os
import discord
import random

REPO_LINK = "https://github.com/dane9640/Daneger-Bot"

client = discord.Client()

@client.event
async def onReady():
  print("We have logged in as {0.user}".format(client))

@client.event

async def on_message(message):
  username = str(message.author).split('#'[0])
  userMessage = str(message.content)
  
  if message.author == client.user:
    return 

  elif(userMessage.lower() == "!rand"):
    await message.channel.send(f"Your random number is: {random.randrange(100)}")

  elif(userMessage.lower() == "!intro"):
    await message.channel.send(f"Hello! I am a discord bot that Dane is making to get better at python/API's more features are incoming.")
    await message.channel.send(f"You can find the source code at: {REPO_LINK}")

  elif(userMessage.lower() == "!commands"):
    await message.channel.send(f"Current commands (More will be added)\n !rand: gives random number\n !intro: I introduce myself\n !commands: You should know what this does")
  
client.run(os.environ['discordToken'])