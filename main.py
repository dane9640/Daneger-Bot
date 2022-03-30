import os
import discord
import random

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
    await message.channel.send(f"Hello! I am a discord bot that Dane is making to get better at python/API's more features are incoming")

client.run(os.environ['discordToken'])