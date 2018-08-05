#!/usr/bin/env python
import googletrans

from discord.ext import commands
import discord

class Utility(object):
    def __init__(self):
        self.translator = googletrans.Translator()

    @commands.command(name="translate_en", aliases=["tren"])
    async def _translate_en(self, ctx, *, text: str):
        """Translates some text to English.
        
        God has been dead for a very long time."""
        translated = self.translator.translate(text, dest="en").text
        await ctx.send(
            (f"**Translated!**\n__Input Text__:\n```{text}```\n__Output Text__:\n"
            f"```{translated}```")
        )

    @commands.command(name="translate", aliases=["tr"])
    async def _translate(self, ctx, dest_lang: str, *, text: str):
        """Translates some text to any language.
        
        Karl Marx is an idiot, and so are you!"""
        translated = self.translator.translate(text, dest=dest_lang).text
        await ctx.send(
            (f"**Translated!**\n__Input Text__:\n```{text}```\n__Output Text__:\n"
            f"```{translated}```")
        )

    
def setup(bot):
    bot.add_cog(Utility())