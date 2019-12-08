#!/usr/bin/env python
import os
import sys
import subprocess
import traceback

from discord.ext import commands
import discord

class Dev(commands.Cog):
    @commands.command(name="reload", aliases=["r"])
    async def _reload(self, ctx, *, cog: str):
        """Reloads a cog.
        
        Communism sucks."""
        try:
            ctx.bot.unload_extension(cog)
            ctx.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f":warning: **Failed to reload cog.**```{e}```")
        else:
            await ctx.send(f":ok_hand: Reloaded cog `{cog}`.")

    @commands.command(name="pull", aliases=["pu"])
    async def _pull(self, ctx):
        """Pulls from git.
        
        Hey Google."""
        cmd_process = subprocess.run(
            "git pull origin master",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )
        out = str(cmd_process.stdout)[2:-1].replace("\\n", "\n") 
        err = str(cmd_process.stderr)[2:-1].replace("\\n", "\n")

        await ctx.send((
            f":thumbsup: Executed pull command, results:\n\n"
            f"**Stdout:**```{out}```"
            f"\n**Stderr:**```{err}```"
        ))

    @commands.command(name="bash", aliases=["cmd"])
    async def _bash(self, ctx, *, command: str):
        """Executes a command."""
        cmd_process = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )
        out = str(cmd_process.stdout)[2:-1].replace("\\n", "\n")
        err = str(cmd_process.stderr)[2:-1].replace("\\n", "\n")
        if out == '':
            out = "None"
        if err == '':
            err = "None"

        await ctx.send((
            f":white_check_mark: Executed.\n\n**Stdout:**```{out}```\n**Stderr:**```{err}```"
        ))

    @commands.command(name="restart", aliases=["reboot"])
    async def _restart(self, ctx):
        """Restarts the bot."""
        await ctx.send(":arrows_counterclockwise: Rebooting...")
        os.execl(sys.executable, sys.executable, * sys.argv)

    @commands.command(name="eval", aliases=["debug"])
    async def _eval(self, ctx, *, code: str):
        """Evaluates code."""
        env = {
            "ctx": ctx,
            "bot": ctx.bot
        }
        to_run = "async def func():\n"
        for line in code.splitlines():
            to_run += f"  {line}\n"
        
        try:
            exec(to_run, env)

            func = env["func"]
            res = await func()
        except Exception as e:
            await ctx.send(f":warning: **Error:** ```{e}```")
        else:
            if res is None:
                await ctx.message.add_reaction("✅")
            else:
                await ctx.send(f":white_check_mark: Evaluated. Result:```{res}```")

    @commands.command(name="repl", aliases=["idle"])
    async def _repl(self, ctx):
        """Starts an REPL."""
        class Repl(object):
            def __init__(self):
                self.repl = ">>> "

            def truncate_2000(self):
                self.repl = self.repl[2000:]
                self.repl = self.repl[self.repl.find("\n"):]

            def write_new_cmd(self, cmd: str):
                self.repl += cmd

            def write_no_strip(self, to_write):
                self.repl += f"\n{to_write}"

            def write(self, to_write: str):
                self.repl += f"\n{to_write.strip()}"


        env = {
            "ctx": ctx,
            "bot": ctx.bot
        }
        repl = Repl()
        repl_msg = await ctx.send(f"```python\n{repl.repl}\n```")

        while True:
            if len(repl.repl) >= 2000:
                repl.truncate_2000()
                repl_msg = await ctx.send(f"```python\n{repl.repl}\n```")
            await repl_msg.edit(content=f"```python\n{repl.repl}\n```")

            def check(msg):
                return msg.author == ctx.message.author and msg.channel == ctx.message.channel

            next_command = await ctx.bot.wait_for("message", check=check)
            cmd = next_command.content
            await next_command.delete()

            if cmd == "exitrepl":
                del repl  # cleanup
                del env
                break

            repl.write_new_cmd(cmd)

            sys.stdout = repl
            try:
                exec(cmd, env)
            except Exception as e:
                repl.write(''.join(traceback.format_exception(type(e), e, e.__traceback__)))
            sys.stdout = sys.__stdout__
            repl.write_no_strip(">>> ")

def setup(bot):
    bot.add_cog(Dev())
