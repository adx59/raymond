#!/usr/bin/env python3.6
from discord.ext import commands
import discord

from cogs.checks import is_mod, is_server_owner

class Mod(commands.Cog):
    def __init__(self):
        pass

    @is_server_owner()
    @commands.command(name='purge')
    async def _purge(self, ctx, limit: int, *, specific_user:discord.Member=None):
        """Purges a channel.
        
        If you wish to target one user's messages, **mention** them."""
        def check(m):
            if not specific_user:
                return True
            
            return m.author.id == specific_user.id
        
        await ctx.channel.purge(limit=limit, check=check)


def setup(bot):
    bot.add_cog(Mod())