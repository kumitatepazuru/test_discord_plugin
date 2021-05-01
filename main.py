import logging

import discord
from discord.ext import commands


class message(commands.Cog):

    THIS_BOT = 705705685543026699

    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)

    @commands.Cog.listener(name='on_message')
    async def msg(self, message: discord.Message):
        # sender is bot, or me
        if message.author.bot or message.author.id == self.THIS_BOT:
            return

        # mention
        if ('<@!' + str(self.THIS_BOT) + '>') in message.content:
            await message.channel.send('なにー？')


def setup(bot):
    bot.add_cog(message(bot))
