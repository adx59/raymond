#!/usr/bin/env python
from discord.ext import commands
import discord

class Idfk(object):
    @commands.command(name="communism")
    async def _communism(self, ctx):
        """Communism lol"""
        await ctx.send(":poop:")

    @commands.command(name="ocket_racoon_is_so_fucking_hot", hidden=True)
    async def _rocket(self, ctx):
        """rocket racoon lol"""
        await ctx.send("dude i totally agree, gotta hit that rule34 for all the good stuff")

    
def setup(bot):
    bot.add_cog(Idfk())