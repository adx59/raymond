#!/usr/bin/env python3
from discord.ext import commands

def is_dev():
        def predicate(ctx):
            await ctx.send(f'{ctx.author.id} {ctx.bot.config.owners}')
            return ctx.author.id in ctx.bot.config.owners
        return commands.check(predicate)
