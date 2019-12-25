#!/usr/bin/env python3
from discord.ext import commands

def is_dev():
        def predicate(ctx):
            return ctx.author.id in ctx.bot.config['owners']
        return commands.check(predicate)
