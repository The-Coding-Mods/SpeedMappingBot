""" Load Config """
import discord
import yaml

config = yaml.safe_load(open("../resources/token.yaml"))

guild = discord.Object(id=config['server']['debug'])

intents = discord.Intents.default()
intents.message_content = True
