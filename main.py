############ Daneger Bot ############################
##### Written by: Danger Dane                       #
##### Liscense: Completly Open Source, feel free to #
#####           take and use code however you want  #
#####################################################

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

  #complimenting the bot
  elif("good bot" in userMessage.lower()):
    await message.channel.send(f"**Blush**")

  #Shaming the bot
  elif("bad bot" in userMessage.lower()):
    await message.channel.send(f"**Cries**")
    
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

  # Rock Paper Scissors Command
  elif("!rps" in userMessage):
    pick = userMessage.split(" ")[1].lower()
    result = rps(pick)
    if "win" in result[1]:
      await message.channel.send(f"{result[0].capitalize()} \n You Win, Congratz!")
    else:
      await message.channel.send(f"{result[0].capitalize()}\n You lost, why not try again?\n I\'m probably not cheating...")
    
  # Command List
  elif(userMessage.lower() == "!commands"):
    await message.channel.send(f"Current commands (More will be added)\n\n !rand: gives random number\n\n !intro: I introduce myself\n\n !randimg: produces a link to a random screenshot\n\n !rps #yourChoice: Play a game of Rock Paper Scissors  !commands: You should know what this does")

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


# Rock paper scissors but with silly logic
def rps(userPick):
  pickChoices = "rock", "paper", "scissors"
  botPick = ""
  result = "lose"
  if random.randint(1,2) == 1:
    result = "win"
    if userPick in pickChoices[0]:
      botPick = pickChoices[2]
    elif userPick in pickChoices[1]:
      botPick = pickChoices[0]
    else:
      botPick = pickChoices[1]
  else: 
    if userPick in pickChoices[0]:
      botPick = pickChoices[1]
    elif userPick in pickChoices[1]:
      botPick = pickChoices[2]
    else:
      botPick = pickChoices[0]    
  return botPick, result

# Runs the bot
client.run(os.environ['discordToken'])
