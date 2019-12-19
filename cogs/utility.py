#!/usr/bin/env python
import googletrans
import PyDictionary

from discord.ext import commands
import discord

class Utility(commands.Cog):
    def __init__(self):
        self.translator = googletrans.Translator()
        self.dictionary = PyDictionary.PyDictionary()

    @commands.command(name="translate_en", aliases=["tren"])
    async def _translate_en(self, ctx, *, text: str):
        """Translates some text to English.
        
        God has been dead for a very long time."""
        translated = self.translator.translate(text, dest="en")

        emb = discord.Embed(title=f":white_check_mark: Translated! [{translated.src} -> en]", color=0xf49e42)
        emb.add_field(name="Original", value=f"```{text}```", inline=False)
        emb.add_field(name="Translated", value=f"```{translated.text}```", inline=False)

        await ctx.send(
            embed=emb
        )

    @commands.command(name="translate", aliases=["tr"])
    async def _translate(self, ctx, dest_lang: str, *, text: str):
        """Translates some text to any language.
        
        Karl Marx is an idiot, and so are you!"""
        translated = self.translator.translate(text, dest=dest_lang)

        emb = discord.Embed(title=f":white_check_mark: Translated! [{translated.src} -> {translated.dest}]", color=0xf49e42)
        emb.add_field(name="Original", value=f"```{text}```", inline=False)
        emb.add_field(name="Translated", value=f"```{translated.text}```", inline=False)

        await ctx.send(
            embed=emb
        )

    @commands.command(name="define", aliases=["def"])
    async def _define(self, ctx, *, term: str):
        """Defines a word."""
        formatted = f"**Definition of `{term}`...**\n"

        async with ctx.typing():
            definition = self.dictionary.meaning(term)
            if definition is None:
                await ctx.send(":no_entry_sign: No definition found for that term.")
                return

        for t in definition:
            formatted += f"{t}:\n```css\n"
            if not definition[t]:
                formatted += f"No definition found for this part of speech." 
            for subdef in definition[t]:
                formatted += f"- ...{subdef}\n"
            formatted += "\n```\n"  

        print(formatted)

        await ctx.send(formatted)
    
def setup(bot):
    bot.add_cog(Utility())