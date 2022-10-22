import discord
from discord import Attachment, app_commands, TextChannel
from discord.ext import commands

from modals.setup import SetupModal
import config as cfg

""" Setup basic bot parameter """
bot = commands.Bot(intents=cfg.intents, command_prefix=None)
tree = bot.tree
speedmapping_group = app_commands.Group(name="speedmapping", description="Commands relating to the speedmapping cup",
                                        guild_ids=[cfg.guild.id])
basemap_group = app_commands.Group(name="basemap", description="Commands relating to the speedmapping cup's base map",
                                   parent=speedmapping_group, guild_ids=[cfg.guild.id])

""" Event definitions """


@bot.event
async def on_ready():
    await bot.wait_until_ready()
    synced = await tree.sync(guild=cfg.guild)
    print("Ready!")
    print(f"Synced {len(synced)} commands")


""" Commands definitions """


@tree.command(name="ping", description="Pong", guild=cfg.guild)
async def ping(interaction: discord.Interaction) -> None:
    await interaction.response.send_message(f"Pong! {int(bot.latency * 1000)}ms")
    return


@speedmapping_group.command(name="setup")
@app_commands.describe(channel="The channel where the speed mapping rules and discussions will be in.")
async def setup(interaction: discord.Interaction, channel: TextChannel) -> None:
    modal = SetupModal()
    await interaction.response.send_modal(modal)


@basemap_group.command(name="add")
async def add_base_map(interaction: discord.Interaction, attachment: Attachment) -> None:
    await interaction.response.send_message(f"Url: {attachment.url}")
    channel = interaction.channel
    await channel.send(file=await attachment.to_file())
    with open(f"../resources/{attachment.filename}", "wb") as f:
        b = await attachment.read()
        f.write(b)



tree.add_command(speedmapping_group)
""" Start Bot """
bot.run(cfg.config['token'])
