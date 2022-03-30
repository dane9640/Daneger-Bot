import os
import discord
import random
import string

# Basically the controller
client = discord.Client()

# Just a link to this bots source code
REPO_LINK = "https://github.com/dane9640/Daneger-Bot"

# Let's you know the bot is active
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

# function triggers when a message has been sent.
# message is the message that triggered function.
@client.event
async def on_message(message):
  # Just some stringifying of important components
  # of the message.
  username = str(message.author.name)
  userMessage = str(message.content)

  # Checks if the message was sent by the bot
  # to prevent infinite loop
  if message.author == client.user:
    return

  # check if the bot was mentioned
  elif(client.user.mentioned_in(message)):
    # if the message is saying hello, say hi back
    if "hello" in userMessage.lower():
      await message.channel.send(f"Hello! {username}")
    # message otherwise.
    else:
      await message.channel.send(f"The fuck did you just say to me, {username}?!")
      
##################### COMMANDS ################
      
  # Random number command
  elif(userMessage.lower() == "!rand"):
    await message.channel.send(f"Your random number is: {random.randrange(100)}")

  # Intro command
  elif(userMessage.lower() == "!intro"):
    await message.channel.send(f"Hello! I am a discord bot that Dane is making to get better at python/API's more features are incoming.")
    await message.channel.send(f"You can find the source code at: {REPO_LINK}")

  # Random Image Command
  elif(userMessage.lower() == "!randimg"):
    await message.channel.send(f"Here is a random screenshot I got from \'hacking\': {randomImgURL()}")
    
  # Command List
  elif(userMessage.lower() == "!commands"):
    await message.channel.send(f"Current commands (More will be added)\n !rand: gives random number\n !intro: I introduce myself\n !randimg: produces a link to a random screenshot !commands: You should know what this does\n")

################# Functions ######################

# Function that builds the url to a random
# image.
def randomImgURL():
  letters = string.ascii_letters
  chars = ""
  i=0
  while i < 2:
    chars += random.choice(letters).lower()
    i += 1
  
  nums = ""
  i = 0
  while i < 4:
    nums += str(random.randint(0, 9))
    i += 1

  url = "https://prnt.sc/" + chars + nums
  return url

# Runs the bot
client.run(os.environ['discordToken'])