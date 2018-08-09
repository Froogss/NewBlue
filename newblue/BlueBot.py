from discord.ext import commands
import json


class BlueBot(commands.Bot):

    def __init__(self, command_prefix=None):
        super().__init__(command_prefix=command_prefix)
        self.load_config()


    async def on_ready(self):
        print("ready")
        for com in self.commands:
            print(com.name)
            print(com.cog_name)

    def load_config(self):
        with open("config.json", "r") as file:
            self.cfg = json.loads(file.read())



