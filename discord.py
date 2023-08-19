import discord
import requests
from bs4 import BeautifulSoup

# Create an instance of the Discord client
intents = discord.Intents.default()
intents.members = True  # Enable the member intent to track member events
client = discord.Client(intents=intents)

# Define the website URL you want to monitor
website_url = 'https://example.com'
# Initialize the content of the website
previous_content = ''

# Define the welcome message
welcome_message = "Welcome to the server! We're glad you're here."

# Define an event for when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

# Define an event for when a new member joins the server
@client.event
async def on_member_join(member):
    # Get the channel where you want to send the welcome message
    # Replace 'your-channel-id' with the actual channel ID
    channel = member.guild.get_channel(your_channel_id)

    # Send the welcome message
    await channel.send(f"{member.mention}, {welcome_message}")

# Function to check for website updates
async def check_website_updates():
    global previous_content

    while True:
        try:
            # Fetch the website content
            response = requests.get(website_url)
            response.raise_for_status()

            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            current_content = soup.get_text()

            # Compare the current content to the previous content
            if current_content != previous_content:
                # Send a notification to the specified Discord channel
                channel = client.get_channel(your_channel_id)
                await channel.send(f'Website updated: {website_url}')

            # Update the previous content
            previous_content = current_content

        except Exception as e:
            print(f'Error checking for updates: {str(e)}')

        # Wait for some time before checking again (e.g., every 1 hour)
        await asyncio.sleep(3600)

# Define an event for when a message is received
@client.event
async def on_message(message):
    # Ignore messages from the bot itself to prevent a loop
    if message.author == client.user:
        return

    if message.content.startswith('ping'):
        # Reply with "pong"
        await message.channel.send('pong')

# Run the bot with your token
client.run('YOUR_BOT_TOKEN_HERE')
