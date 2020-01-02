#!/usr/bin/env python3.6
import json
import logging
import traceback

from discord.ext import commands
import discord

class Raymond(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="",
            description="Adam's utility bot."
        )

        logging.basicConfig(
            level=logging.INFO,
            format="[%(name)s %(levelname)s] %(message)s"
        )
        self.logger = logging.getLogger("bot")
        
        self.config = json.loads(open("config.json").read())
        self.BChandler = None

    async def get_prefix(self, msg):
        return self.config["prefix"]

    async def on_ready(self):
        self.logger.info("Bot is ready!")
        await self.change_presence(activity=discord.Game(name="with linter errors"))

    async def on_message(self, msg):
        await self.BChandler.handle_incoming(msg)

        await self.process_commands(msg)

    async def on_command_error(self, ctx, err):
        if isinstance(err, commands.errors.CommandNotFound):
            return

        if isinstance(err, commands.CommandInvokeError):
            fmt = traceback.format_exception(type(err.original), err.original,
                                             err.original.__traceback__, chain=False)
            fmt = '\n'.join(fmt)
        else:
            fmt = traceback.format_exception(type(err), err,
                                             err.__traceback__, chain=False)
            fmt = '\n'.join(fmt)

        await ctx.send(f":warning: **Error:**```{fmt}```")
        self.logger.exception(fmt)

    def run(self):
        token = self.config["token"]
        cogs = self.config["cogs"]

        for cog in cogs:
            self.logger.info(f"Loaded cog {cog}")
            try:
                self.load_extension(cog)
            except Exception as e:
                self.logger.exception(f"Error occured while loading {cog}", e)

        super().run(token)

bot = Raymond()
bot.run()
