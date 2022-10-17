import discord
from discord import app_commands
import yaml
from discord.ext import commands

""" Load Config """
config = yaml.safe_load(open("../resources/token.yaml"))
guild = discord.Object(id=config['server']['debug'])

""" Setup basic bot parameter """
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix=None)
tree = bot.tree

""" Event definitions """
@bot.event
async def on_ready():
    await bot.wait_until_ready()
    synced = await tree.sync(guild=guild)
    print("Ready!")
    print(f"Synced {len(synced)} commands")

""" Commands definitions """
@tree.command(name="ping", description="Pong", guild=guild)
async def ping(interaction: discord.Interaction) -> None:
    await interaction.response.send_message(f"Pong! {int(bot.latency*1000)}ms")
    return


@tree.command(name="setup", guild=guild)
@app_commands.describe(start_time="Time the Speedmapping starts (unix timestamp)", duration="How long do the mappers have time!")
@app_commands.choices(duration=[
    discord.app_commands.Choice(name="30 Minutes", value=0),
    discord.app_commands.Choice(name="1 Hour", value=1),
    discord.app_commands.Choice(name="1 Hour 30 Minutes", value=2)
])
async def setup(interaction: discord.Interaction, start_time: int, duration: discord.app_commands.Choice[int]) -> None:
    await interaction.response.send_message(f"Paramerters: {start_time} \t {duration.name}", ephemeral=True)
    return

""" Start Bot """
bot.run(config['token'])
