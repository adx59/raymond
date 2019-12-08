#!/usr/bin/env python
from discord.ext import commands
import discord

class Idfk(commands.Cog):
    @commands.command(name="communism", hidden=True)
    async def _communism(self, ctx):
        """Communism lol"""
        await ctx.send("is garbage xd")

    @commands.command(name="ocket_racoon_is_so_fucking_hot", hidden=True)
    async def _rocket(self, ctx):
        """rocket racoon lol"""
        await ctx.send("dude i totally agree, gotta hit that rule34 for all the good stuff")

    
def setup(bot):
    bot.add_cog(Idfk())