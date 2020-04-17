import os
import requests

import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
         'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']

days = ['today', 'tomorrow', 'yesterday']


def handle_command(command):
    sign = signs[0]
    day = days[0]
    if len(command) > 0:
        words = command.split(" ")
        print(words)
        if len(words) > 1 and words[1] in signs:
            sign = words[1]
        if len(words) > 2 and words[2] in days:
            day = words[2]

    params = (('sign', sign), ('day', day))
    r = requests.post('https://aztro.sameerkumar.website/', params=params)
    data = r.json()
    description = data['description']
    return description


def help_message():
    possible_signs = ', '.join(signs)
    possible_days = ', '.join(days)
    return """Roscobot - Get your daily Horoscope:

Example:
!zodiac
!zodiac leo
!zodiac leo today

possible signs: {signs}
possible dates: {days}
""".format(signs=possible_signs, days=possible_days)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    zodiac_cmd = "!zodiac"
    c = message.content
    if c.startswith(zodiac_cmd):
        start = len(zodiac_cmd)
        response = handle_command(c[start:])
        await message.channel.send(response)
    elif c == "!help":
        response = help_message()
        await message.channel.send(response)

client.run(TOKEN)
