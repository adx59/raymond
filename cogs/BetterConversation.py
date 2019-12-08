#!/usr/bin/env python
import os
import sys
import subprocess
import traceback
import urllib.parse

from discord.ext import commands
import discord

class BetterConvo (object):
    def __init__(self, bot):
        self.bot = bot

    def filter(self, content):
        arr_content = content.lower().split()

        if len(arr_content) == 1 and ('what' in content.lower()):
            return (1, f'> {content}\ntry saying something productive')
        
        elif len(arr_content) > 1 and ('what’s' in arr_content[0].lower() or 'what\'s' in arr_content[0].lower()):
            urlparams = {'q': ' '.join(arr_content[1:])}
            encoded = urllib.parse.urlencode(urlparams)

            return (0, f'> {content}\nhttps://lmgtfy.com/?{encoded}')

        return (0, False)

    async def handle_incoming(self, message: discord.Message):
        if message.author.id == self.bot.config['bcTarget']:
            result = self.filter(message.content)

            if not result[1]:
                return

            if result[0]:
                await message.delete()

            await message.channel.send(result[1])
            

def setup(bot):
    bot.BChandler = BetterConvo(bot)