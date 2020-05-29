import discord
from discord.ext import commands
import logging

# ijomaa's token 
TOKEN = 'NTg2MjIyOTkwMTkxMDk5OTA1.XtBAKg.NOONtRmuhlWusANN5wWGYX9wflc'


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
async def on_message(messagefff):
    print('Message from {0.author}: {0.content}'.format(messagefff))
    if messagefff.author == client.user:
        return

    if messagefff.content.lower().startswith(f'hello'):
        await messagefff.channel.send('Hello!')

    if messagefff.content.lower().startswith(f'greater good'):
        await messagefff.channel.send('The higher order shall reign.')

    if messagefff.content.lower().startswith(f'e'):
        await messagefff.channel.send('e')

    if messagefff.content.lower().startswith(f'h'):
        await messagefff.channel.send('h')

    await client.process_commands(messagefff)


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
    id = 420284927205048321
    if message.author == client.get_user(id):
        await message.channel.send(f'You are mom')


#For some reason, "ctx" is needed for the code to function.

@client.command()
async def test(ctx, *, question):
    channel_id = 715723956455342141 # bot-test1 channel

    host_lounge = channel_id
    ans = question
    channel = client.get_channel(host_lounge)
    await channel.send(ans)


@client.command()
async def test2(ctx):
# host_lounge = 654362714638123040
    channel_id = 715723956455342141 # bot-test1 channel

    host_lounge = channel_id
    ans = question
    channel = client.get_channel(host_lounge)

    channel = ctx.channel
    await channel.send(ans)

# @client.command()
# async def search(message):
#   print('h from {@.author}: {@.content}'.format(message))
#   msg = '{@.author}: {@.content}'.format(message)
#   hostlounge = 654362714638123040
#   channel = client.get_channel(hostlounge)
#   await channel.send(msg)

@client.command()
async def search(ctx):
  print('h from {0.author}: {0.message.content}'.format(ctx))
  msg = '{0.author}: {0.message.content}'.format(ctx)
  hostlounge = 715723956455342141
  channel = client.get_channel(hostlounge)
  await channel.send(msg)


logs()

client.run(TOKEN)
