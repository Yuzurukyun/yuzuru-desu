import discord
from discord.ext import commands
import logging


TOKEN = 'lol no'


def logs():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)


client = commands.Bot(command_prefix='yu!', case_insensitive=True)


@client.event
async def on_ready():
    print('logged on as {0}!'.format(client.user))
    return await client.change_presence(activity=discord.Activity(type=1, name='"yu!help" for commands', url='https://twitch.tv/twitch'))


@client.event
async def on_message(message):
    print('Message from {0.author}: {0.content}'.format(message))
    if message.author == client.user:
        return

    if message.content.lower().startswith(f'hello'):
        await message.channel.send('Hello!')

    if message.content.lower().startswith(f'greater good'):
        await message.channel.send('The higher order shall reign.')

    if message.content.lower().startswith(f'e'):
        await message.channel.send('e')

    if message.content.lower().startswith(f'h'):
        await message.channel.send('h')

    await client.process_commands(message)


@client.command()
async def shaw(ctx):
    await ctx.send('Shaw is gay lol!!!')


@client.command()
async def servant(ctx):
    await ctx.send('Servant is a good servant to me.')


@client.command()
async def gay(ctx, member: discord.Member):
    await ctx.send(f"{member.mention} is gay lol!!!")


@client.command()
async def mf(message):
    #id = 332456386946531328
    id = 263253261094486016
    if message.author == client.get_user(id):
        await message.channel.send(f'You are mom')


#For some reason, "ctx" is needed for the code to function.

@client.command()
async def test(ctx, *, question):
    host_lounge = [channel id]
    ans = question
    channel = client.get_channel(host_lounge)
    await channel.send(ans)


logs()

client.run(TOKEN)
