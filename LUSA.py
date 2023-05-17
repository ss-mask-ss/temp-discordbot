import discord

import os


client = discord.Client()



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(discord.__version__)
    print('------')
    #sarver数
    # activity = discord.Activity(name=f"LUSA丨{len(client.guilds)}sever", type=discord.ActivityType.watching)
    # client = discord.Client(activity=activity)
    await client.change_presence(activity=discord.Game(name=f"LUSAtest丨ver1.0.0丨{len(client.guilds)}sever"))



@client.event
async def on_message(message):
  msg_txt = message.content
  msg_author = message.author

  if msg_author.bot:
    return

  if msg_txt == '/test':
    await message.channel.send(f'{msg_author.mention}さん、こんにちは')







print('bottoken.txt')
file = open('bottoken.txt','r',encoding='UTF-8')
TOKEN=file.read()
file.close()

print(TOKEN)

client.run(TOKEN)