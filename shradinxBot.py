# shradinxBot.py
# Shradinx
# November 13, 2022
# Interactions.py bot made for QuestCraft
# ------------------------------------------------------------------------------

# Import all modules needed for bot.
import interactions
from interactions import autodefer
import random

# Open the bot token file and read for the token
botToken = open("token.txt", "r")
botToken = botToken.read()

# Set server ID
serverID = 1039592132014522460

# Set the client variable along with token, intents, and presence
client = interactions.Client(intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MESSAGE_CONTENT,
                             token=botToken, presence=interactions.ClientPresence(
                                status=interactions.StatusType.ONLINE,
                                activities=[
                                    interactions.PresenceActivity(name="#announcements for 3.0 ping",
                                                                  type=interactions.PresenceActivityType.WATCHING)
                                ]
                                )
                             )

# Initiate bot and print bot activation message
@client.event()
async def on_ready():
    print('QuestCraft_Bot_Python Activated!')

# When a message is sent, if it contains "is qc fix", respond with "no"
@client.event()
async def on_message_create(message: interactions.Message):
    if "is qc fix" in message.content.lower():
        channel = await message.get_channel()
        await channel.send("no")


# Random number command: Returns a number between 1 and 100000 to the user
@client.command(
    name="random_number",
    description="Get a random number between 1 and 100000",
    scope=serverID,
)
async def random_number(ctx):
    # Set message to be printed and get random number
    output = "Here is your number: " + str(random.randint(1, 100000))
    print(ctx.author.name, "ran random_number command.")
    await ctx.send(output)

# Drugs command: Print "Drugs are bad."
@client.command(
    name="drugs",
    description="Drugs",
    scope=serverID,
)
async def drugs(ctx):
    print(ctx.author.name, "ran drugs command.")
    await ctx.send("Drugs are bad.")

# Ping command: Print "Pong!"
@client.command(
    name="ping",
    description="Ping SMH",
    scope=serverID
)
async def ping(ctx):
    print(ctx.author.name, "ran ping command.")
    await ctx.send("Pong!")

# Soon command: Print "Soon™: a moment between the next minute and the heat death of the universe."
@client.command(
    name="soon",
    description="Replies with soon:tm:",
    scope=serverID
)
async def soon(ctx):
    print(ctx.author.name, "ran soon command.")
    await ctx.send("Soon™: a moment between the next minute and the heat death of the universe.")

# Fixed command: Print "**kinda**, you will get an @ everyone when it gets done. There is a workaround though."
@client.command(
    name="fixed",
    description="Is QC Fixed?",
    scope=serverID
)
async def fixed(ctx):
    print(ctx.author.name, "ran fixed command.")
    await ctx.send("**kinda**, you will get an @ everyone when it gets done. There is a workaround though.")

# v3info command: Print "In QCXR V3.0, we are departing from using MCXR, to Vivecraft."
@client.command(
    name="v3info",
    description="Info about V3",
    scope=serverID
)
async def v3info(ctx):
    print(ctx.author.name, "ran v3info command.")
    await ctx.send("In QCXR V3.0, we are departing from using MCXR, to Vivecraft.")

# When command: Print "It will come out when Pojlib is done, which is in development, "
#                    "but may take a bit to finish. We will never have a ETA."
@client.command(
    name="when",
    description="Tells you when it comes out.",
    scope=serverID
)
async def when(ctx):
    print(ctx.author.name, "ran when command.")
    await ctx.send("It will come out when Pojlib is done, which is in development, "
                   "but may take a bit to finish. We will never have a ETA.")

# Why command: Print "Questcraft is broken due to v44 breaking the way we started OpenXR (2d --> 3d)"
@client.command(
    name="why",
    description="Tells you why QC is broken",
    scope=serverID
)
async def why(ctx):
    print(ctx.author.name, "ran why command.")
    await ctx.send("Questcraft is broken due to v44 breaking the way we started OpenXR (2d --> 3d)")

# YVR command: Print "YVR is a Chinese headset company. They have requested YVRCraft. "
#                    "We are working on both QCXR and YVRCraft."
@client.command(
    name="yvr",
    description="Tells you what YVR is.",
    scope=serverID
)
async def yvr(ctx):
    print(ctx.author.name, "ran yvr command.")
    await ctx.send("YVR is a Chinese headset company. They have requested YVRCraft. "
                   "We are working on both QCXR and YVRCraft.")

# ShradinxQCFix command: Return how many times Shradinx has said "is qc fix"
@client.command(
    name="shradinxqcfix",
    description="Provides how many times Shradinx has said \"is qc fix\" ",
    scope=serverID,
)
@autodefer(delay=1)
async def shradinxQCFix(ctx):
    # Get guild/server info
    guild = await interactions.get(client, interactions.Guild, object_id=serverID)
    # Set the initial total value
    total = 0
    # Return Shradinx's user ID and message.content containing "is qc fix"
    def check(message):
        return message.author.id == 338854290967756811 and message.content == "is qc fix"
    # For all text channels in the server, check all channel history for instances of "is qc fix" sent by Shradinx.
    for channel in await guild.get_all_channels():
        # Check channel types for only text and voice
        if channel.type in {interactions.ChannelType.GUILD_CATEGORY, interactions.ChannelType.GUILD_VOICE}:
            continue
        # For the entire length of the channel history, check for "is qc fix" sent by Shradinx
        async for message in channel.history(check=check):
            # Add 1 to the total for each message found
            total += 1
    print(ctx.author.name, "ran shradinxqcfix command.")
    await ctx.send(f"Shradinx has said \"is qc fix\" {total} times")

# Isqcfix command: Prints "no fuck you"
@client.command(
    name="isqcfix",
    description="is qc fixed :fancytroll:",
    scope=serverID,
)
async def isQCFix(ctx):
    print(ctx.author.name, "ran isqcfix command.")
    await ctx.send("no fuck you")

# Users command: Returns all roles that can use application commands, or this bot.
@client.command(
    name="users",
    description="replies with all users able to run bot commands",
    scope=serverID,
)
async def users(ctx):
    roleList = []
    # Get guild/server info
    guild = await interactions.get(client, interactions.Guild, object_id=serverID)
    # Get all roles in the server
    roles = await guild.get_all_roles()
    # For all the roles in the server, search for all that have USE_APPLICATION_COMMANDS permission.
    for i in range(len(roles)):
        if int(roles[i].permissions) & interactions.Permissions.USE_APPLICATION_COMMANDS:
            # Append the role name to roleList
            roleList.append(roles[i].name.lower())
    print(ctx.author.name, "ran users command.")
    await ctx.send(", ".join(roleList) + " are able to use this bot.")

# Jenny command: prints "soon:tm:"
@client.command(
    name="jenny",
    description="When will the jenny mod be ported to QuestCraft",
    scope=serverID,
)
async def jenny(ctx):
    print(ctx.author.name, "ran the jenny command.")
    await ctx.send("soon:tm:")

# Qctutorial command: prints "This video is not endorsed by the QC team, but made by my creator.
#                            https://www.youtube.com/watch?v=TLWR_3hEBJU"
@client.command(
    name="qctutorial",
    description="Tutorial fix.",
    scope=serverID,
)
async def qctutorial(ctx):
    print(ctx.author.name, "ran the qctutorial command.")
    await ctx.send("This video is not endorsed by the QC team, but made by my creator. "
                   "https://www.youtube.com/watch?v=TLWR_3hEBJU")

client.start()
