import discord
from discord.ext import commands


class Event(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    # The On_Ready event.
    async def on_ready(self):
        print('logged on as {0}!'.format(self.client.user))
        return await self.client.change_presence(
            activity=discord.Activity(type=1, name='"yu!help" for commands', url='https://twitch.tv/twitch'))

    # A way to see if this cog works.
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')






def setup(client):
    client.add_cog(Event(client))
