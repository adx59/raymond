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

        elif len(arr_content) < 3 and ('sorry' in content.lower()):
            return (0, f'> {content}\nbro. NEVER APOLOGIZE. (to anyone in this server, at least). '+\
                'STAND UP FOR YOURSELF BRO. If someone\'s being a dick to you, DON\'T APOLOGIZE.'+\
                    ' If it is genuinely your problem, then be better. Don\'t be sorry.')

        elif 'bloody stream' in content.lower():
            return (
                0,
'https://www.youtube.com/watch?v=ndRVcGbJP7Y\n\n \
\
Shijima no soko kara mezameru sono hashiratachi toki wo koe\n \
Shinku no chishio ga tachiagaru yuuki wo hikiawaseru\n\n \
\
Uketsugu ai wo sadame to yobu nara\n \
Hohoemu me de tsugi no te wo\n\n \
\
Yami wo azamuite setsuna wo kawashite\n \
Yaiba surinuke yatsura no suki wo tsuke\n \
Tsuranuita omoi ga mirai wo hiraku\n \
Like a bloody storm, atsuku like a bloody stone\n \
Ketsumyaku ni kizamareta innen ni\n \
Ukiagaru kienai hokori no kizuna nigirishimete\n \
')

        # lmgtfy

        lmgtfy_search_phrases = ['what\'s', 'what’s', 'what is', 'whats']
        
        for phrase in lmgtfy_search_phrases:
            if phrase in content:
                search = content.replace(phrase, '')
                urlparams = {'q': search}
                encoded = urllib.parse.urlencode(urlparams)

                return (0, f'> {content}\nhttps://lmgtfy.com/?{encoded}')

        return (0, False)

    async def handle_incoming(self, message: discord.Message):
        if message.author.id in self.bot.config['bcTarget']:
            result = self.filter(message.content)

            if not result[1]:
                return

            if result[0]:
                await message.delete()

            await message.channel.send(result[1])
            

def setup(bot):
    bot.BChandler = BetterConvo(bot)