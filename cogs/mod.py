#!/usr/bin/env python3.6
from discord.ext import commands
import discord

from cogs.checks import is_mod, is_server_owner

class Mod(commands.Cog):
    def __init__(self):
        pass

    async def create_mute_role(self, ctx):
        if 'raymond mute' in list(map(lambda r: r.name, ctx.guild.roles)):
            return next((r for r in ctx.guild.roles if r.name == 'raymond mute'), None)
        
        role = await ctx.guild.create_role(name='raymond mute', color=discord.Color(value = 0x522c04))

        for channel in ctx.guild.channels:
            overwrite = discord.PermissionOverwrite(send_messages=False)

            await channel.set_permissions(role, overwrite=overwrite)

        return role

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
    
    @is_mod()
    @commands.command(name='mute')
    async def _mute(self, ctx, *, target:discord.Member):
        """Mutes a user."""
        mr = await self.create_mute_role(ctx)

        await target.add_roles(mr)

        await ctx.send(':white_check_mark:')

    @is_mod()
    @commands.command(name='unmute')
    async def _unmute(self, ctx, *, target:discord.Member):
        '''Unmutes a user.'''
        mr = next((r for r in ctx.guild.roles if r.name == 'raymond mute'), None)

        await target.remove_roles(mr)
        await ctx.send(':ballot_box_with_check:')

def setup(bot):
    bot.add_cog(Mod())