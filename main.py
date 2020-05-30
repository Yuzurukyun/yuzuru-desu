# import standard python libraries
import os
import logging
from dotenv import load_dotenv

# import custom classes

# import third party libraries
import discord
from discord import utils
from discord.ext import commands

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
GM_IDS = {
    '[Yuzuru]': 332456386946531328,
    '[Servant]'   :   173404147901661184,
    '[Negative]'  :   624214764226084884,
    '[Mobel]'     :   309650909741318154,
    '[Noire]'     :   263253261094486016,
    '[Shaw]'      :   243311861183807488,

    '[_F]'        :   420284927205048321, # need to give them high access to debug bot commands
}

# Participant IDs who participated in the roleplay.
PARTICIPANT_IDS = {
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
}

# other people to add to use the bot
OTHER_IDS = {
    '[Jay]'       :   210143294972231681,
    '[Jovial]'    :   268074911619219456,
}

# Dictionary for the list of all User IDs in the roleplay. Ids are required since a user may change their name.
USER_IDS = dict()
USER_IDS.update(GM_IDS)
USER_IDS.update(PARTICIPANT_IDS)
USER_IDS.update(OTHER_IDS)

# Prints out logs as discord.log.
def logs():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

# The command bot command.
client = commands.Bot(command_prefix=commands.when_mentioned_or('yu!', 'y!', 'yuzuru!', 'yus!'), case_insensitive=True)

class Characters:
    """
        Class for the Characters. My peeve for this is that I don't know how to take a single element and use it
        outside of the __str__. I just couldn't due to my incompetence and tackling tougher subjects without
        learning the basics.
    """
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
    return await client.change_presence(
        activity=discord.Activity(type=1, name='"yu!help" for commands', url='https://twitch.tv/twitch'))


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
    channel = utils.get(client.get_all_channels(), name='the-bot')

    # Don't do anything if the bot sent the message. Prevents recursive loops.
    if message.author == client.user:
        return

    # This receives the messages from the Bot's DMs and send them directly to
    # the Discord Channel. We also make sure that the bot didn't send the
    # message, to prevent recursive loops.
    if message.guild is None and message.author != client.user: # for debugging message that is received by bot
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
        This one took a bit to write, but overall need optimization and factoring. There has to be a way to make this
        less cancer like. The idea is that people will DM the bot and the information will be sent to the Discord
        Channels where every GM can see and access the players inquiries. Though, the code works, it's just ugly.
        This uses the Dictionary.
    """

    # log message
    msg = '**{0.author}**: {0.message.content}'.format(ctx)

    # Search query must be sent in DM's. GM's are an exception.
    # if ((ctx.guild is None)
    #         or (ctx.author.id in GM_IDS.values())):

    if ((ctx.guild is None)
            or (is_gm(ctx))):

        is_channel_char_found = False

        # send user's message to correct channel based on the channel character
        for channel_char in DISCORD_CHANNELS.keys():
            if ((channel_char.lower() in ctx.message.content.lower())
                    and (not is_channel_char_found)):

                # get channel id based on channel name, using the channel character
                channel = utils.get(client.get_all_channels(), name=DISCORD_CHANNELS[channel_char])

                await ctx.send(
                    ":warning: **Your message has been sent to the GMs! :warning: \n> Please wait for a moment...**")
                await channel.send(msg)

                # only process the first channel character found
                is_channel_char_found = True

        # send message to retard-messages channel
        if (not is_channel_char_found):
            channel = utils.get(client.get_all_channels(), name=RETARD_CHANNEL)
            await ctx.send(
                ":warning: **Your message has been sent to the GMs! :warning: \n> Please wait for a moment...**")
            await channel.send(msg)

    else:
        await ctx.send(
            ":no_entry: **You are not allowed to message your search query publicly. Send a DM instead.** :no_entry:")

# check if user is a GM for the rp
def is_gm(ctx):
    is_user_gm = ctx.author.id in GM_IDS.values()
    return is_user_gm

@client.command(aliases=['r', 'rpy', 'rep'])
@commands.check(is_gm)
async def reply(ctx, *args): # pass all arguments as a list
    """
    This is unfinished, as you may have guessed. This code has the same issue as the above and I have no idea how to
    fix it. The idea is that the GMs will be able to send messages to players on the spot. This uses the dictionary.
    Also, this poses an issue as, if I were to do 'y!r [Jay] {Message}', the 'y!r [Jay]' is included and it's ugly.
    """

    msg = '**{0.author}**: {0.message.content}'.format(ctx) # log message
    message_to_user = '**{0.author}**: {1}'.format(ctx, args[1]) # skip 1st argument (bot command) of original message

    user_target = args[0] # get username character identifier to send message to

    # send a message to the target user if they are in the rp
    for user in USER_IDS.keys():
        if (user.lower() in user_target.lower()):
            pid = client.get_user(USER_IDS[user]) # get target user's id based on username

            await ctx.send(":warning: **Message was sent!** :warning:")
            await pid.send(message_to_user)
            break # only process 1 user

@client.command()
async def test2(ctx):
    msg = '**{0.author}**: {0.message.content}'.format(ctx)
    msg2 = '**{0.author}**: {0.message.content}'.format(ctx)
    msg3 = ctx.message.content[ctx.message.content.find(' '):]
    await ctx.send(msg3)
    await ctx.send("f")
    
# Runs the log program.
logs()

# This runs the client.
client.run(TOKEN)
