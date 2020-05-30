# import standard python libraries
import os
import logging
from dotenv import load_dotenv

# import custom classes

# import third party libraries
import discord
from discord.ext import commands

# The .gitignore file will not upload the .env file, keeping the discord token
# safe. Create the .env file as follows:
'''
File path:
yuzuru-desu/.env

Inside .env file:
DISCORD_TOKEN=<your token>
'''

load_dotenv() # export environment variables in .env file
TOKEN = os.getenv('DISCORD_TOKEN') # Discord Token; self-explanatory

# Dictionary for the list of User IDs.
User_IDs = {
    'Yuzuru'    :   332456386946531328,
    'Servant'   :   173404147901661184,
    'Negative'  :   624214764226084884,
    'Mobel'     :   309650909741318154,
    'Noire'     :   263253261094486016,
    'Shaw'      :   243311861183807488,
    'Jay'       :   210143294972231681,

    'Jovial'    :   268074911619219456,

    'Perkorn'   :   217276956469755904,
    'Jeremy'    :   293473817932726272,
    'Twice'     :   194385555125960705,
    'Nookuon'   :   218372116893007872,
    'Lillie'    :   692429269321777222,
    'Arko'      :   135769169600839681,
    'Coffee'    :   331783104236617728,
    'Cam'       :   325379295549587467,
    'Zocobo'    :   366255501035569154,
    'Clopel'    :   327506772422164480,
    'Riam'      :   363795030365700097,
    'Skrubby'   :   212241751383998477,
    'DC'        :   492590612969816095,
    'Lyn'       :   276101884555821057,
    'Megumin'   :   177100361729966082
}

# Dictionary for the list of Discord Channels.
Discord_Channels = {
    'Section_A'       :   715914092203737128,
    'Section_B'       :   715914337012940804,
    'Section_C'       :   715914353273995365,
    'Section_D'       :   715914366847025283,
    'Section_E'       :   715914378771431454,
    'Intersections'   :   715914424673763369,
    'Cringe'          :   715951589566971974
}

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

    # I don't even know what this does.
    if message.author == client.user:
        return

    # This receives the messages from the Bot's DMs and send them directly to the Discord Channel.
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
    if message.author == client.get_user(User_IDs[Yuzuru]):
        await message.channel.send(str(Yuzuru))


# This one took a bit to write, but overall need optimization and factoring. There has to be a way to make this less
# cancer like. The idea is that people will DM the bot and the information will be sent to the Discord Channels where
# every GM can see and access the players inquiries. Though, the code works, it's just ugly. This uses the Dictionary.
@client.command(aliases=['s', 'searc', 'sear', 'ask'])
async def search(ctx):

    if '[a]' in ctx.message.content.lower():
        msg = '**{0.author}**: {0.message.content}'.format(ctx)
        channel = client.get_channel(Section_A)
        await ctx.send(":warning: **Your message has been sent to the GMs! :warning: \n> Please wait for a moment...**")
        await channel.send(msg)

    elif '[b]' in ctx.message.content.lower():
        msg = '**{0.author}**: {0.message.content}'.format(ctx)
        channel = client.get_channel(Section_B)
        await ctx.send(":warning: **Your message has been sent to the GMs! :warning: \n> Please wait for a moment...**")
        await channel.send(msg)

    elif '[c]' in ctx.message.content.lower():
        msg = '**{0.author}**: {0.message.content}'.format(ctx)
        channel = client.get_channel(Section_C)
        await ctx.send(":warning: **Your message has been sent to the GMs! :warning: \n> Please wait for a moment...**")
        await channel.send(msg)

    elif '[d]' in ctx.message.content.lower():
        msg = '**{0.author}**: {0.message.content}'.format(ctx)
        channel = client.get_channel(Section_D)
        await ctx.send(":warning: **Your message has been sent to the GMs! :warning: \n> Please wait for a moment...**")
        await channel.send(msg)

    elif '[e]' in ctx.message.content.lower():
        msg = '**{0.author}**: {0.message.content}'.format(ctx)
        channel = client.get_channel(Section_E)
        await ctx.send(":warning: **Your message has been sent to the GMs! :warning: \n> Please wait for a moment...**")
        await channel.send(msg)

    elif '[i]' in ctx.message.content.lower():
        msg = '**{0.author}**: {0.message.content}'.format(ctx)
        channel = client.get_channel(Intersections)
        await ctx.send(":warning: **Your message has been sent to the GMs! :warning: \n> Please wait for a moment...**")
        await channel.send(msg)

    else:
        msg = '{0.author}: {0.message.content}'.format(ctx)
        channel = client.get_channel(Cringe)
        await ctx.send(":warning: **Your message has been sent to the GMs! :warning: \n> Please wait for a moment... \nAlso, you have not stated an area, so please do so.**")
        await channel.send(msg)


# This is unfinished, as you may have guessed. This code has the same issue as the above and I have no idea how to
# fix it. The idea is that the GMs will be able to send messages to players on the spot. This uses the dictionary.
# Also, this poses an issue as, if I were to do 'y!r [Jay] {Message}', the 'y!r [Jay]' is included and it's ugly.
@client.command(aliases=['r', 'rpy', 'rep'])
async def reply(ctx):

    if '[jay]' in ctx.message.content.lower():
        msg = '**{0.author}**: {0.message.content}'.format(ctx)
        pid = client.get_user(User_IDs['Jay'])
        await ctx.send(":warning: **Message was sent!** :warning:")
        await pid.send(msg)

    elif '[cringe]' in ctx.message.content.lower():
        msg = '**{0.author}**: {0.message.content}'.format(ctx)
        pid = client.get_channel(Discord_Channels['Cringe'])
        await ctx.send(":warning: **Message was sent!** :warning:")
        await pid.send(msg)


# Runs the log program.
logs()

# This runs the client.
client.run(TOKEN)
