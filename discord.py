import discord

# Create an instance of the Discord client
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
client = discord.Client(intents=intents)

# Define an event for when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

# Define an event for when a message is received
@client.event
async def on_message(message):
    # Ignore messages from the bot itself to prevent a loop
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

# Run the bot with your token
client.run('YOUR_BOT_TOKEN_HERE')
