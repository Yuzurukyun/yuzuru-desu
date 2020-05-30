# import standard python libraries
import os
import logging
from dotenv import load_dotenv

# import custom classes

# import third party libraries
import discord
from discord.ext import commands
from discord import utils

# The .gitignore file will not upload the .env file, keeping the discord token
# safe. Create the .env file as follows:
'''
File path:
yuzuru-desu/.env

Inside .env file:
DISCORD_TOKEN=<your token>

e.g.
DISCORD_TOKEN_YUZURU=<your token>
'''

load_dotenv() # export environment variables in .env file

# get discord token environment variable
# TOKEN = os.getenv('DISCORD_TOKEN_IJOMAA')
TOKEN = os.getenv('DISCORD_TOKEN_YUZURU')

# Dictionary for the list of User IDs.
# ids are required since a user may change their name
USER_IDS = {
    '[Yuzuru]'    :   332456386946531328,
    '[Servant]'   :   173404147901661184,
    '[Negative]'  :   624214764226084884,
    '[Mobel]'     :   309650909741318154,
    '[Noire]'     :   263253261094486016,
    '[Shaw]'      :   243311861183807488,
    '[Jay]'       :   210143294972231681,

    '[Jovial]'    :   268074911619219456,

    '[Perkorn]'   :   217276956469755904,
    '[Jeremy]'    :   293473817932726272,
    '[Twice]'     :   194385555125960705,
    '[Nookuon]'   :   218372116893007872,
    '[Lillie]'    :   692429269321777222,
    '[Arko]'      :   135769169600839681,
    '[Coffee]'    :   331783104236617728,
    '[Cam]'       :   325379295549587467,
    '[Zocobo]'    :   366255501035569154,
    '[Clopel]'    :   327506772422164480,
    '[Riam]'      :   363795030365700097,
    '[Skrubby]'   :   212241751383998477,
    '[DC]'        :   492590612969816095,
    '[Lyn]'       :   276101884555821057,
    '[Megumin]'   :   177100361729966082,

    '[_F]'        :   420284927205048321
}

# Dictionary for the list of Discord Channels.
# <channel character> : <channel name>
DISCORD_CHANNELS = {
    '[a]' : 'section-a',
    '[b]' : 'section-b',
    '[c]' : 'section-c',
    '[d]' : 'section-d',
    '[e]' : 'section-e',
    '[i]' : 'all-intersections'
}
RETARD_CHANNEL = 'retard-messages'

# GM IDs who GMs the roleplay.
GM_IDs = [332456386946531328, 173404147901661184, 624214764226084884,
          309650909741318154, 263253261094486016, 243311861183807488]

# Participant IDs who participated in the roleplay.
Participant_IDs = [217276956469755904, 293473817932726272, 194385555125960705, 218372116893007872, 692429269321777222,
                   331783104236617728, 325379295549587467, 366255501035569154, 327506772422164480, 363795030365700097,
                   212241751383998477, 492590612969816095, 276101884555821057, 177100361729966082]

# Prints out logs as discord.log.
def logs():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

# The command bot command.
client = commands.Bot(command_prefix=commands.when_mentioned_or('yu!', 'y!', 'yuzuru!', 'yus!'), case_insensitive=True)


# Class for the Characters. My peeve for this is that I don't know how to take a single element and use it outside of the __str__.
# I just couldn't due to my incompetence and tackling tougher subjects without learning the basics.
class Characters:
    def __init__(self, name, reside, moneys, doc):
        self.name = name
        self.doc = doc
        self.moneys = moneys
        self.reside = reside

    def __str__(self):
        return '`Name:` **{self.name}** \n`Reside in:` **{self.reside}** `\n`Money:` You have **{self.moneys}¥**' \
               ' \n`Document:` {self.doc}'.format(self=self)


# Character Data (name, doc, money)
Yuzuru = Characters('We are no strangers to love', 'You know the rules, so do I.',
                    'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 1000)


# The On_Ready event.
@client.event
async def on_ready():
    print('logged on as {0}!'.format(client.user))
    return await client.change_presence(activity=discord.Activity(type=1, name='"yu!help" for commands', url='https://twitch.tv/twitch'))


# The Error Catcher event.
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('**This command does not exist or it may be a typo. '
                       '\nI suggest** ***literal suicide*** **or** `yu!help`.')

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('**Please input a valid argument.** `e.g. yu!search [argument]`')


# These events occur whenever you type a message.
@client.event
async def on_message(message):
    # This prints all logs to the console for security reasons.
    print('Message from {0.author}: {0.content}'.format(message))
    channel = client.get_channel(715992199329742948)

    # Don't do anything if the bot sent the message. Prevents recursive loops.
    if message.author == client.user:
        return

    # This receives the messages from the Bot's DMs and send them directly to
    # the Discord Channel. We also make sure that the bot didn't send the
    # message, to prevent recursive loops.
    if message.guild is None and message.author != client.user:
        msg = '**{0.author}**: {0.content}'.format(message)
        await channel.send(msg)

    # Meme
    if 'hello there' in message.content.lower():
        await message.channel.send('General Kenobi!')

    # Meme
    if 'greater good' in message.content.lower():
        await message.channel.send('The higher order shall reign.')

    # e
    if message.content.lower().startswith(f'e'):
        await message.channel.send('e')

    # h
    if message.content.lower().startswith(f'h'):
        await message.channel.send('h')

    # Prevents it from clashing with commands.
    await client.process_commands(message)


# Shaw is gay lol!
@client.command()
async def shaw(ctx):
    await ctx.send('Shaw is gay lol!!!')


# Servant.
@client.command()
async def servant(ctx):
    await ctx.send('Servant is a good servant to me.')


# Gay double ping time.
@client.command()
async def gay(ctx, member: discord.Member):
    await ctx.send(f"{member.mention} is gay lol!!!")


# This is a test command for a bigger command later on -- profiles. Look below for it.
@client.command()
async def mf(message):
    # id = 332456386946531328
    id = 263253261094486016
    if message.author == client.get_user(id):
        await message.channel.send(f'You are mom')


# The idea is that, if they were to do 'y!profile', the user will receive their information and their information alone.
@client.command(aliases=['pf', 'profiles', 'p'])
async def profile(message):
    if message.author == client.get_user(USER_IDS[Yuzuru]):
        await message.channel.send(str(Yuzuru))

@client.command(aliases=['s', 'searc', 'sear', 'ask'])
async def search(ctx):
    """
       This one took a bit to write, but overall need optimization and factoring. There has to be a way to make this less
       cancer like. The idea is that people will DM the bot and the information will be sent to the Discord Channels where
       every GM can see and access the players inquiries. Though, the code works, it's just ugly. This uses the Dictionary.
    """

    # log message
    msg = '**{0.author}**: {0.message.content}'.format(ctx)

    is_channel_char_found = False

    # send user's message to correct channel based on the channel character
    for channel_char in DISCORD_CHANNELS.keys():
        if ((channel_char.lower() in ctx.message.content.lower())
                and (not is_channel_char_found)):

            # get channel id based on channel name, using the channel character
            channel = utils.get(client.get_all_channels(), name=DISCORD_CHANNELS[channel_char])

            await ctx.send(":warning: **Your message has been sent to the GMs! :warning: \n> Please wait for a moment...**")
            await channel.send(msg)

            # only process the first channel character found
            is_channel_char_found = True

    # send message to retard-messages channel
    if (not is_channel_char_found):
        channel = utils.get(client.get_all_channels(), name=RETARD_CHANNEL)
        await ctx.send(":warning: **Your message has been sent to the GMs! :warning: \n> Please wait for a moment...**")
        await channel.send(msg)

@client.command(aliases=['r', 'rpy', 'rep'])
async def reply(ctx):
    """
    This is unfinished, as you may have guessed. This code has the same issue as the above and I have no idea how to
    fix it. The idea is that the GMs will be able to send messages to players on the spot. This uses the dictionary.
    Also, this poses an issue as, if I were to do 'y!r [Jay] {Message}', the 'y!r [Jay]' is included and it's ugly.
    """

    # log message
    msg = '**{0.author}**: {0.message.content}'.format(ctx)

    is_username_found = False

    # send a message to the user matching the username
    for username in USER_IDS.keys():
        if ((username.lower() in ctx.message.content.lower())
                and (not is_username_found)):

            # get user id based on username
            pid = client.get_user(USER_IDS[username])

            await ctx.send(":warning: **Message was sent!** :warning:")
            await pid.send(msg)

            # only process the first username found
            is_username_found = True

@client.command()
async def test2(ctx):
    pid = discord.utils.get(client.get_all_members(), name='_F')
    pid = client.get_user(USER_IDS['[_F]'])
    username = list(USER_IDS.keys())[0]
    print(username.lower() in ctx.message.content.lower())
    await pid.send("Hi this works!")
    
# Runs the log program.
logs()

# This runs the client.
client.run(TOKEN)
