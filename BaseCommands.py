from discord.ext import commands


class BaseCommands:
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def reload_extensions(self):
		for name in self.extenions:
			self.unload_extension(name)
			try:
				self.bot.load_extension(name)

			except ImportError as e:
				await self.bot.say("Failed to reload extension {}")

	@commands.command()
	async def load_extension(self, ctx, name):
		try:
			self.bot.load_extension(name)

		except ImportError as e:
			await self.bot.say("Extension {} could not be loaded")




def setup(bot):
	bot.add_cog(BaseCommands(bot))
