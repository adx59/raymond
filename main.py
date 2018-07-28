#!/usr/bin/env python
import json

from discord.ext import commands
import discord

class Raymond(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="r",
            description="Adam's utility bot."
        )

        self.config = json.loads(open("config.json"))

    def run(self):
        token = self.config["token"]
        cogs = self.config["cogs"]