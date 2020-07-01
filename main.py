# import standard python libraries
import os
import logging
import json
from dotenv import load_dotenv
from datetime import datetime

# import custom classes

# import third party libraries
from pytz import timezone
import discord
from discord import utils
from discord import File
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

load_dotenv()  # export environment variables in .env file

# get discord token environment variable
# TOKEN = os.getenv('DISCORD_TOKEN_IJOMAA')
TOKEN = os.getenv('DISCORD_TOKEN_YUZURU')


# Dictionary for the list of Discord Channels.
# <channel character> : <channel name>
DISCORD_CHANNELS = {
    '[a]': 'section-a',
    '[b]': 'section-b',
    '[c]': 'section-c',
    '[d]': 'section-d',
    '[e]': 'section-e',
    '[i]': 'all-intersections'
}
RETARD_CHANNEL = 'retard-messages'

# GM IDs who GMs the roleplay.
GM_IDS = {
    '[Yuzuru]': 332456386946531328,
    '[Servant]': 173404147901661184,
    '[Negative]': 624214764226084884,
    '[Mobel]': 309650909741318154,
    '[Noire]': 263253261094486016,
    '[Shaw]': 243311861183807488,

    '[_F]': 420284927205048321,  # need to give them high access to debug bot commands
}

# Participant IDs who participated in the roleplay.
PARTICIPANT_IDS = {
    '[Perkorn]': 217276956469755904,
    '[Mana]': 373781173203369987,
    '[Twice]': 194385555125960705,
    '[Nookuon]': 218372116893007872,
    '[Lillie]': 692429269321777222,
    '[Arko]': 135769169600839681,
    '[Coffee]': 331783104236617728,
    '[Cam]': 325379295549587467,
    '[Zocobo]': 366255501035569154,
    '[Clopel]': 327506772422164480,
    '[Riam]': 363795030365700097,
    '[DC]': 492590612969816095,
    '[Lyn]': 276101884555821057,
    '[Megumin]': 177100361729966082,
    '[Shady]': 721496867627860080,

    # dropped participants
    '[Jeremy]': 293473817932726272,
    '[Skrubby]': 212241751383998477,
}

# other people to add to use the bot
OTHER_IDS = {
    '[Jay]': 210143294972231681,
    '[Jovial]': 268074911619219456,
    '[Salanto]': 200278357235990528,
    '[Munz]': 339542438081331203,
}

# Dictionary for the list of all User IDs in the roleplay. IDs are required since a user may change their name.
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


"""
When testing the bot locally while no bot is running on the server.
This is the default command syntax.
"""
# The command bot command
client = commands.Bot(command_prefix=commands.when_mentioned_or('yu!', 'y!', 'yuzuru!', 'yus!', 'yuyu!'),
                      case_insensitive=True)

"""
When testing the bot locally while the bot is running on the server.
"""
# # The command bot command
# client = commands.Bot(command_prefix=commands.when_mentioned_or('dev!'),
#                       case_insensitive=True)


class Character:  # class name should be singular
    """
        Class for the Characters. My peeve for this is that I don't know how to take a single element and use it
        outside of the __str__. I just couldn't due to my incompetence and tackling tougher subjects without
        learning the basics.
    """

    def __init__(self, name, reside, money, doc):
        self.name = name
        self.reside = reside
        self.money = money
        self.doc = doc

    def __str__(self):
        return '`Name:` **{self.name}** \n`Resides in:` **{self.reside}** \n`Money:` You have **{self.money}¥**' \
               ' \n`Document:` {self.doc}'.format(self=self)

# A really hacky fix to save data. Only works for the money. The work required to do it properly will take a long time.
# Only do this very bad technique because saving money is important.

CHARACTER_MONEY = None


with open('character_money.json', 'r') as file:
    CHARACTER_MONEY = json.load(file)
    file.close()

CHARACTER_DATA = {
    '[Perkorn]': Character(
        'Kurisu Makise',
        'Hotel Room 412',
        CHARACTER_MONEY['[Perkorn]'],
        'https://docs.google.com/document/d/1MOkA6N3YUsT2_DmnY0NzRnHA0p-EbtS9Oo9ToeTqJFQ/edit'
    ),
    '[Mana]': Character(
        'Suzuha Amane',
        'Small House (Section E)',
        CHARACTER_MONEY['[Mana]'],
        'https://docs.google.com/document/d/143DsMShw7yLJgBhwejl0ASkVAC2BArUWHmRvOCXMRek/edit'
    ),
    '[Twice]': Character(
        'Battler Ushiromiya',
        'Hotel Room 420',
        CHARACTER_MONEY['[Twice]'],
        'https://docs.google.com/document/d/18aTcFr4v0-Res1Md91UqZ-oAB8_n4Elw08Cftbh8BZA/edit'
    ),
    '[Nookuon]': Character(
        'Ayaka Yukimoto',
        'Future Gadget Lab',
        CHARACTER_MONEY['[Nookuon]'],
        'https://deathwarrantbychance.imfast.io/'
    ),
    '[Lillie]': Character(
        'Rumiho Akiha (Faris Nyan-Nyan)',
        'The Condo (Except Room 1)',
        CHARACTER_MONEY['[Lillie]'],
        'https://docs.google.com/document/d/1gJ9fhd9yWeghM_NQ39DtqPNWoQ-ymZChUID4QvGniis/edit'
    ),
    '[Arko]': Character(
        'Rumiho Akiha (Faris Nyan-Nyan)',
        'The Condo (Except Room 1)',
        CHARACTER_MONEY['[Arko]'],
        'https://docs.google.com/document/d/1gJ9fhd9yWeghM_NQ39DtqPNWoQ-ymZChUID4QvGniis/edit'
    ),
    '[Coffee]': Character(
        'Moeka Kiryu',
        'Apartment Room 105',
        CHARACTER_MONEY['[Coffee]'],
        'https://docs.google.com/document/d/1BuHE-mQ2a_IE6WIqNnOJtXH1iZ43QSmwZGg28kgQIDM/edit'
    ),
    '[Cam]': Character(
        'Maho Hiyajo',
        'Hotel Room 412',
        CHARACTER_MONEY['[Cam]'],
        'https://docs.google.com/document/d/1igcjc70spmEuFWBFfNUQlrYysh4d0WujveziFsum1i4/edit'
    ),
    '[Zocobo]': Character(
        'Luka Urushibara',
        'Yanagibayashi Shrine',
        CHARACTER_MONEY['[Zocobo]'],
        'https://docs.google.com/document/d/1TlFGS81xkgvaFZ78OtAbA64xx6RCwxkYVBBbyEd7olg/edit'
    ),
    '[Clopel]': Character(
        'Rei Mekaru',
        'Hotel Room 420 (Originally Room 411)',
        CHARACTER_MONEY['[Clopel]'],
        'https://docs.google.com/document/d/1ybGmQW-T-bxS6cOoEOlrlmCiiTF8ZTCgaZTunLMl2iw/edit'
    ),
    '[Riam]': Character(
        'Lyle D. Termina',
        'Hotel Room 410',
        CHARACTER_MONEY['[Riam]'],
        'https://docs.google.com/document/d/1ZYGjAj_HNY-w7fEuXkM83sxUd5W_-tFfA74M3ysIlfc/edit'
    ),
    '[Shady]': Character(
        'Syobai Hashimoto',
        'Condo Room 1 (Shop: Shopping Complex Entrance)',
        CHARACTER_MONEY['[Shady]'],
        'https://docs.google.com/document/d/1znpFpaZmfvq0k1JNUtjOTBE8pWFQ9ylnoieUNXXYS7E/edit'
    ),
    '[DC]': Character(
        'Yuuji Diabolique',
        'Hotel Room 419',
        CHARACTER_MONEY['[DC]'],
        'https://docs.google.com/document/d/1gBOyQiFRAKhC9mIRKP9vaavIL1RkOe3LK0zib4gsrjo/edit'
    ),
    '[Lyn]': Character(
        'Rintaro Okabe',
        'Future Gadget Lab',
        CHARACTER_MONEY['[Lyn]'],
        'https://docs.google.com/document/d/1L5FOg-Yx4LLLLgSzpyr0LvxK-YG00ZutabXPMQIkTgw/edit'
    ),
    '[Megumin]': Character(
        'Mayuri Shiina',
        'Her Home lmao',
        CHARACTER_MONEY['[Megumin]'],
        'https://docs.google.com/document/d/1aFV20hOGWw_lVCo30Q7p6kCmtU-DeLJpB6g1qP2o1XI/edit'
    ),

    # need to give them high access to debug bot commands
    '[_F]': Character(
        'Itaru Hashida',
        'His Home lmao',
        CHARACTER_MONEY['[_F]'],
        'https://deathwarrantbychance.imfast.io/'
    ),
    '[Yuzuru]': Character(
        'We are no strangers to love. You know the rules, so do I.',
        "A full commitment is what I am thinking of, you won't get this from any other guy.",
        CHARACTER_MONEY['[Yuzuru]'],
        'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    )
}



def is_gm(ctx):
    is_user_gm = ctx.author.id in GM_IDS.values()
    return is_user_gm

@client.command(aliases=['gb', 'getb', 'gbank'])
@commands.check(is_gm)
async def getbank(ctx):
    """
    Get bank data of RP participants. Required before bot shutdown.

    Make sure to run this command before shutting down the bot.
    Data is not saved when the bot is shut down while running on a server.
    Data is saved if the bot is shut down while running on a local machine.
    Implement an external database connection to save the data instead (not free so forget about it).

    Restrictions: GMs only.
    Usages: y!getbank
    Aliases: gb, getb, gbank
    """

    bot_timezone = timezone('EST') # EST timezone
    time_format = '%Y-%m-%d %H:%M:%S %Z%z'
    curr_time = datetime.now(bot_timezone)

    # time when the bank data is retrieved
    msg_result = "`Last Updated`: **{0}**".format(curr_time.strftime(time_format))

    await ctx.send(msg_result, file=File("character_money.json"))

# This is a test command for a bigger command later on -- profiles. Look below for it.
@client.command(hidden=True) # hide command from y!help
async def mf(message):
    # id = 332456386946531328
    id = 263253261094486016
    if message.author == client.get_user(id):
        await message.channel.send(f'You are mom')


@client.command(hidden=True) # hide command from y!help
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command(hidden=True) # hide command from y!help
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command(aliases=['c', 'ck'])
@commands.check(is_gm)
async def check(ctx, *args): # pass all arguments as a list
    """
    Check a RP participant's character profile.

    Restrictions: GMs only.
    Users:
        Participant:
            [Perkorn]
            [Jeremy]
            [Mana]
            [Twice]
            [Nookuon]
            [Lillie]
            [Arko]
            [Coffee]
            [Cam]
            [Zocobo]
            [Clopel]
            [Riam]
            [Shady]
            [DC]
            [Lyn]
            [Megumin]
    Usages: y!check <user 1> <user 2> ... <user 5>
    Examples:
        y!check [Lyn]
        y!check [Lyn] [Twice]
        y!check [Lyn] [Twice] [Jeremy] [Perkorn] [Cam]
    Aliases: c, ck
    """

    try:
        test_target = args[0]  # check if user send any arguements
    except IndexError:
        await ctx.send(
            ":no_entry: **ERROR** :no_entry: \n> No arguments were specified.")
        return  # end the command since the user fails at doing the command correctly

    is_user_target_found = None
    user_list = args

    # show target user's profile based on each user i
    for user_target in args:
        is_user_target_found = False
        for user in USER_IDS.keys():
            if (is_user_target_found): # only process 1 user
                break

            elif ((user.lower() in user_target.lower())
                  and (not is_user_target_found)):
                await ctx.send("`User:` **{0}**\n{1}".format(user, CHARACTER_DATA[user]))
                is_user_target_found = True

        if not is_user_target_found:
            await ctx.send(
                ":no_entry: **ERROR** :no_entry: \n> __{0}__ invalid user for current RP.".format(user_target))



@client.command(aliases=['b', 'bk'])
@commands.check(is_gm)
async def bank(ctx, user_target, amount: int):
    """
        Modify bank account of an RP participant.

        Restrictions: GMs only.
        Users:
            Participant:
                [Perkorn]
                [Jeremy]
                [Mana]
                [Twice]
                [Nookuon]
                [Lillie]
                [Arko]
                [Coffee]
                [Cam]
                [Zocobo]
                [Clopel]
                [Riam]
                [Shady]
                [DC]
                [Lyn]
                [Megumin]
        Usages: y!bank <user> <amount>
        Examples:
            y!bank [Coffee] -10000
            y!bank [Perkorn] 999999
        Aliases: b, bk
    """
    is_user_target_found = False

    for user in CHARACTER_DATA.keys():
        if is_user_target_found:  # only process 1 user
            break

        elif ((user.lower() in user_target.lower())
              and (not is_user_target_found)):

            orig_amount = CHARACTER_DATA[user].money  # money in user's bank account before the transaction
            CHARACTER_DATA[user].money += amount  # update user's bank account

            # Very very very hacky solution. Only doing this for a quick solution.
            # Save the new money in the character_money.json file
            CHARACTER_MONEY[user] += amount
            with open('character_money.json', 'w') as file:
                json.dump(CHARACTER_MONEY, file, indent=2)
                file.close()

            pid = client.get_user(USER_IDS[user])  # get target user's id based on username
            # notify user of bank transaction
            await pid.send(
                ":warning: **Bank account updated from {0}¥ to {1}¥** :warning: \n> Authorized by {2.author}".format(
                    orig_amount, CHARACTER_DATA[user].money, ctx))

            # notify the GM that the bank account has been updated
            await ctx.send(
                ":warning: **Updated {0} bank account from {1}¥ to {2}¥** :warning:".format(
                    pid, orig_amount, CHARACTER_DATA[user].money))

            is_user_target_found = True

    if not is_user_target_found:
        await ctx.send(
            ":no_entry: **ERROR** :no_entry: \n> __{0}__ invalid participant user for current RP.".format(user_target))


# The idea is that, if they were to do 'y!profile', the user will receive their information and their information alone.
@client.command(aliases=['p', 'pf', 'profiles'])
async def profile(ctx):
    """
        Show your character profile in the RP.

        Use force command to show profile in public.

        Restrictions: Bot must be DM'd.
        Usages: y!profile <force>
        Examples:
            y!profile
            y!profile force
        Aliases: p, pf, profiles
    """

    force_cmd = "force"  # keyword to force displaying someone's profile when not in a DM

    # Command only works if message was a DM. Use the force keyword to bypass the restriction.
    if ((ctx.guild is None)
            or (force_cmd in ctx.message.content.lower())):

        is_user_found = False

        # show user's profile based on their user id
        for user in USER_IDS.keys():
            if ctx.author.id == USER_IDS[user]:
                await ctx.send(CHARACTER_DATA[user])
                is_user_found = True

        if not is_user_found:
            await ctx.send(
                ":no_entry: **ERROR** :no_entry: \n> __{0.author}__ invalid user for current RP.".format(ctx))

    else:
        await ctx.send(":warning: **To reveal your profile publicly, add `force` to the command.** :warning:\n"
                       + "> DM to see your profile.")

'''
# The On_Ready event.
@client.event
async def on_ready():
    print('logged on as {0}!'.format(client.user))
    return await client.change_presence(
        activity=discord.Activity(type=1, name='"yu!help" for commands', url='https://twitch.tv/twitch'))
'''

# The Error Catcher event.
"""
    So I just noticed that you did this. So, yeah, I probably should have looked into this a bit more and put
    more error checking here. You can do that though.
"""


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('**This command does not exist or it may be a typo. '
                       '\nI suggest** ***literal suicide*** **or** `yu!help`.')

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('**Please input a valid argument.** `e.g. yu!search [argument]`')

    if isinstance(error, commands.BadArgument):
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
    if message.guild is None and message.author != client.user:  # for debugging message that is received by bot
        msg = '**{0.author}**: {0.content}'.format(message)
        await channel.send(msg)

    # Meme
    if 'hello there' in message.content.lower():
        await message.channel.send('General Kenobi!')

    # Meme
    if 'greater good' in message.content.lower():
        await message.channel.send('The higher order shall reign.')

    # e
    if message.content.lower().startswith(f'e') and message.author.id != OTHER_IDS["[Munz]"]:
        await message.channel.send('e')
    elif message.content.lower().startswith(f'e') and message.author.id == OTHER_IDS["[Munz]"]:
        await message.channel.send("You are not a clown. You are the entire circus.")

    # h
    if message.content.lower().startswith(f'h') and message.author.id != OTHER_IDS["[Munz]"]:
        await message.channel.send('h')
    elif message.content.lower().startswith(f'h') and message.author.id == OTHER_IDS["[Munz]"]:
        await message.channel.send("You are not a clown. You are the entire circus.")

    # Prevents it from clashing with commands.
    await client.process_commands(message)


# Shaw is gay lol!
@client.command()
async def shaw(ctx):
    """
    Declare that Shaw is gay.

    Usages: y!shaw
    """
    await ctx.send('Shaw is gay lol!!!')

# Servant.
@client.command()
async def servant(ctx):
    """
    Remind Servant that they are a good servant.

    Usages: y!servant
    """
    await ctx.send('Servant is a good servant to me.')


# Gay double ping time.
@client.command()
async def gay(ctx, member: discord.Member):
    """
    Mention someone to declared them gay.

    Usages: y!gay <member>
    Examples: y!gay @Yuzuru Nishimiya#3327
    """
    await ctx.send(f"{member.mention} is gay lol!!!")


@client.command(aliases=['s', 'searc', 'sear', 'ask'])
async def search(ctx, *args):  # pass all arguments as a list
    """
        Send a message to the GMs based on where you are in the RP.

        Restrictions: Participants only. Bot must be DM'd.
        Usages: y!search <area> <message>
            Areas:
                [a]: Section A
                [b]: Section B
                [c]: Section C
                [d]: Section D
                [e]: Section E
                [i]: All Intersections
        Examples:
            y!search [a] Lock the door.
            y!search [b] Can I activate the time machine?
            y!search [c] Tries to take the car keys.
            y!search [d] Attacks Batter.
            y!search [e] Check underneath the dead body for items.
            y!search [i] Activate bomb.
        Aliases: s, searc, sear, ask
    """

    msg = '**{0.author}**: {0.message.content}'.format(ctx)  # log message

    """
        If the user doesn't use any arguments at all, e.g. the user just did y!s, we will get an IndexError
        exception since the list args is empty. The trick with .join returning an empty string doesn't work if the
        list args is empty. So, we create a try-except block to deal with the error.
    """
    # We do this so that the variable scope is outside the try block. Meaning that the variable can be used
    # in the rest of the code.
    channel_target = None
    try:
        channel_target = args[0]  # get channel identifier to send message to
    except IndexError:
        await ctx.send(
            ":no_entry: **ERROR** :no_entry: \n> No arguments were specified.")
        return  # end the command since the user fails at doing the command correctly

    """
        Skip bot command info in message. We're combining all the arguments in the message into a string,
        seperating them with a space. If there are no message arguments, e.g. the user just did [a], normally we'd get 
        an IndexError exception since the index [1] doesn't exist. The string .join method instead returns an
        empty string.
    """
    main_message = ' '.join(args[1:])

    # Format message with code style if message isn't empty. We can do this by passing in a string. If the string
    # is empty it will return a False value, and if it isn't it will return a True value.
    if main_message:
        main_message = '**`' + main_message + '`**'

    # full message to send to channel with standardize bot command name info
    message_to_channel = '**{0.author}**: y!search {1}'.format(ctx, main_message)

    is_channel_char_found = False

    # Command only works if message was a DM. GMs can bypass this restriction.
    if ((ctx.guild is None)
            or (is_gm(ctx))):

        # send user's message to correct channel based on the channel identifier
        for channel_char in DISCORD_CHANNELS.keys():
            if is_channel_char_found:  # only process 1 channel
                break

            elif channel_char.lower() in ctx.message.content.lower():

                # get channel id based on channel name, using the channel identifier
                channel = utils.get(client.get_all_channels(), name=DISCORD_CHANNELS[channel_char])

                await channel.send(message_to_channel)
                await ctx.send(
                    ":warning: **Your message has been sent to the GMs!** :warning: \n> Please wait for a moment...")
                is_channel_char_found = True
                break  # only process the first channel character found

        if not is_channel_char_found:
            await ctx.send(
                ":no_entry: **ERROR** :no_entry: \n> __{0}__ invalid area section for current RP.".format(
                    channel_target))

    else:
        await ctx.send(
            ":no_entry: **You are not allowed to message your search query publicly. Send a DM instead.** :no_entry:")


@client.command(aliases=['r', 'rpy', 'rep'])
@commands.check(is_gm)
async def reply(ctx, *args):  # pass all arguments as a list
    """
    Send a reply message to an RP participant.

    Restrictions: GMs only.
    Users:
        Participant:
            [Perkorn]
            [Jeremy]
            [Mana]
            [Twice]
            [Nookuon]
            [Lillie]
            [Arko]
            [Coffee]
            [Cam]
            [Zocobo]
            [Clopel]
            [Riam]
            [Shady]
            [DC]
            [Lyn]
            [Megumin]
        GM:
            [Yuzuru]
            [Servant]
            [Negative]
            [Mobel]
            [Noire]
            [Shaw]
    Usages: y!reply <user> <message>
    Examples:
        y!reply [Lyn] There is no metal upa behind the box.
    Aliases: r, rpy, rep
    """

    # Formatting the help message description is too much hassle. This is good enough.
    # And yes, this is mandatory. Otherwise people will not know how to use your bot.

    # I added a bunch of error checking here, to give you some more code examples that
    # you can read up and understand. They're not really needed for the other functions,
    # but I bet it will make other people who use your bot like it more.

    msg = '**{0.author}**: {0.message.content}'.format(ctx)  # log message

    """
        If the user doesn't use any arguments at all, e.g. the user just did y!r, we will get an IndexError
        exception since the list args is empty. The trick with .join returning an empty string doesn't work if the
        list args is empty. So, we create a try-except block to deal with the error.
    """
    # We do this so that the variable scope is outside the try block. Meaning that the variable can be used
    # in the rest of the code.
    user_target = None
    try:
        user_target = args[0]  # get user identifier to send message to
    except IndexError:
        await ctx.send(
            ":no_entry: **ERROR** :no_entry: \n> No arguments were specified.")
        return  # end the command since the user fails at doing the command correctly

    """
        Skip bot command info in message. We're combining all the arguments in the message into a string,
        seperating them with a space. If there are no message arguments, e.g. the user just did [_F], normally we'd get 
        an IndexError exception since the index [1] doesn't exist. The string .join method instead returns an
        empty string.
    """
    main_message = ' '.join(args[1:])

    # full message to send to user with no bot command info
    message_to_user = '**{0.author}**: {1}'.format(ctx, main_message)

    is_user_target_found = False

    # send a message to the target user if they are in the rp
    for user in USER_IDS.keys():
        if is_user_target_found:  # only process 1 user
            break

        elif ((user.lower() in user_target.lower())
              and (not is_user_target_found)):

            pid = client.get_user(USER_IDS[user])  # get target user's id based on username

            await pid.send(message_to_user)
            await ctx.send(":warning: **Message was sent!** :warning:")

            is_user_target_found = True

    if not is_user_target_found:
        await ctx.send(
            ":no_entry: **ERROR** :no_entry: \n> __{0}__ invalid user for current RP.".format(user_target))


@client.command(hidden=True) # hide command from y!help
async def test2(ctx):
    msg = '**{0.author}**: {0.message.content}'.format(ctx)
    msg2 = '**{0.author}**: {0.message.content}'.format(ctx)
    msg3 = ctx.message.content[ctx.message.content.find(' '):]
    await ctx.send(msg3)
    await ctx.send("f")


@client.command(hidden=True)
async def literalsuicide(ctx):
    await ctx.send("https://www.youtube.com/watch?v=2dbR2JZmlWo \nhttps://www.youtube.com/watch?v=-h5WrWncDZw")


if __name__ == "__main__": # search this up as to why this is better
    # Runs the log program.
    logs()

    # This runs the client.
    client.run(TOKEN)
