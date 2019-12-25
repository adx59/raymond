#!/usr/bin/env python3.6
from discord.ext import commands
import discord

class Mod(commands.Cog):
    def __init__(self):
        pass

    async def purge(self, ctx, limit: int, *, specific_user=None):
        """Purges a channel.
        
        If you wish to target one user's messages, **mention** them."""
        def check(m):
            if not specific_user:
                return True
            
            return m.author == specific_user
        
        await ctx.channel.purge(limit=limit, check=check)


def setup(bot):
    bot.add_cog(Mod())