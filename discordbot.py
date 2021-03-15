import discord
import os
import json
import requests

from decouple import config

gClient = discord.Client()

def getCoffee(pInfo):
    vResponse = requests.get(config('COFFEEAPI'))
    vJSON = json.loads(vResponse.text)
    return("Coffee status: " + vJSON[pInfo])

def getJoke():
    vResponse = requests.get(config('JOKEAPI'))
    vJSON = json.loads(vResponse.text)
    return vJSON

@gClient.event
async def on_ready():
    print('Bot logged in as {0.user}'.format(gClient))

@gClient.event
async def on_message(pMessage):
    if pMessage.author == gClient.user:
        return

    if pMessage.content.startswith('!help'):
        await pMessage.channel.send('Omegabot is ready for your commands:\n\t!help - This message\n\t!coffee - Get current coffee status\n\t!joke - get a random joke from https://geek-jokes.sameerkumar.website/api')

    if pMessage.content.startswith('!coffee'):
        vStatus = getCoffee("Status")
        await pMessage.channel.send(vStatus)

    if pMessage.content.startswith('!joke'):
        vJoke = getJoke()
        await pMessage.channel.send(vJoke)

gClient.run(config('TOKEN'))
