#!/usr/bin/env python3.6
from discord.ext import commands

def is_dev():
    def predicate(ctx):
        return ctx.author.id in ctx.bot.config['owners']
    return commands.check(predicate)

def is_mod():
    def predicate(ctx):
        return ctx.author.id in ctx.bot.config['owners'] \
            or ctx.author.guild_permissions.administrator
    return commands.check(predicate)