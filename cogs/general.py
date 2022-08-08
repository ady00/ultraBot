import discord
from discord.ext import commands




class General(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.command(help = 'Gives a general greeting or greets a specified member')
    async def greet(self, ctx, name = ''):
        if (name == ''):
            await ctx.send('Hey there!')
        else:
            await ctx.send(f'Hey {name}!')
    

    @commands.command(help = 'Adds numbers togethers')
    async def add(self, ctx, *values):
        try:
            sum = 0
            for num in values:
                sum += int(num)
            await ctx.reply(sum)
        except ValueError:
            await ctx.reply('Please enter integers only')


    



def setup(bot):
    bot.add_cog(General(bot))