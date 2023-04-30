import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import os
import datetime
from typing import List

clientprefix = '^'
intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix=clientprefix, intents=intents,status=nextcord.Status.do_not_disturb)

@client.event
async def on_ready():
    print('Bot working as {0.user}'.format(client))
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name="/ commands"),status=nextcord.Status.do_not_disturb)
    print('rpc set! at ', str(datetime.datetime.now()))
    print('Bot is now working! started at: ', str(datetime.datetime.now()))
    print('--------------------------------------------------------------')

@client.slash_command(name="load", description="Loads a cog")
@commands.is_owner()
async def load(interaction: Interaction, extension: str):
    client.load_extension(f'cogs.{extension}')
    embed = nextcord.Embed(title="Cog loaded", description=f"**Loaded {extension}**", color=0x00ff00)
    await interaction.response.send_message(embed=embed)

@client.slash_command(name="unload", description="Unloads a cog")
@commands.is_owner()
async def unload(interaction: Interaction, extension: str):
    client.unload_extension(f'cogs.{extension}')
    embed = nextcord.Embed(title="Cog unloaded", description=f"**Unloaded {extension}**", color=0x00ff00)
    await interaction.response.send_message(embed=embed)

@client.slash_command(name="reload", description="Reloads a cog")
@commands.is_owner()
async def reload(interaction: Interaction, extension: str):
    client.reload_extension(f'cogs.{extension}')
    embed = nextcord.Embed(title="Cog reloaded", description=f"**Reloaded {extension}**", color=0x00ff00)
    await interaction.response.send_message(embed=embed)

extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        extensions.append('cogs.' + filename[:-3])

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.')
            print(e)


client.run('YOUR TOKEN HERE')