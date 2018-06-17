from discord.ext import commands
import logging
from BlueClass import BlueBot


bot = BlueBot(command_prefix="[")
logging.basicConfig(filename='example.log', level=logging.INFO, format=bot.cfg["logging"]["format"], datefmt=bot.cfg["logging"]["datefmt"])

logging.info("loading starting extensions")
for cog in bot.cfg["starting_commands"]:
	try:
		bot.load_extension(cog)
		logging.info("successfully loaded extension {}".format(cog))

	except ImportError as e:
		logging.error("Failed to load extension {}".format(cog))

bot.run(bot.cfg["Tokens"]["NewBlue"])

