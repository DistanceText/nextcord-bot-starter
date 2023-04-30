import nextcord
from nextcord.ext import commands
from nextcord import member
from nextcord import Interaction
from colorama import Fore, Style
from nextcord.ext.commands import has_permissions, MissingPermissions
from typing import List

class ExampleCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(description="adds two numbers together")
    async def add(self, interaction: Interaction, num1: int, num2: int):
        embed = nextcord.Embed(title="Addition", description=f"{num1} + {num2} = {num1 + num2}", color=nextcord.Color.blue())
        await interaction.response.send_message(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        print(f"{message.author} has sent a message: {message.content}")

def setup(client):
    client.add_cog(ExampleCog(client))
    print("Loaded Example Cog")