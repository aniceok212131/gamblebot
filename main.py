import random
import discord
from discord import app_commands
from discord.ext import commands
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash commands.")
    except Exception as e:
        print(f"Sync failed: {e}")

@bot.tree.command(name="gamble", description="gamble")
async def gamble(interaction: discord.Interaction):
    number = random.randint(1, 100)
    if number >= 50:
        await interaction.response.send_message(f"{number}% you won 2 cents", ephemeral=False)
    else:
        await interaction.response.send_message(f"{number}% you suck and owe everyone 2 yearly subscriptions of discord nitro", ephemeral=False)

client.run(os.getenv("MTM2NzYyNjUyMTA3MzgxMTQ1Ng.GWqhZB.el5gNSt-7JNewRpf86bMDw5g3aeOm24CReL-70"))
