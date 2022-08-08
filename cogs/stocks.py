import discord
import pandas_datareader as web
# import pandas
# import matplotlib.pyplot as plt
from discord.ext import commands


source = 'yahoo'


# Gets the closing stock price for today
def get_today_stock_price(ticker):
    data = web.DataReader(name = ticker, data_source = source)
    return data['Close'].iloc[-1]


# Gets the stock information from the last five years
def get_stock_information(ticker):
    return web.DataReader(name = ticker, data_source = source)


def get_stock_history(ticker, start_date, end_date):
    return web.DataReader(name = ticker, data_source = source,
                          start = start_date, end = end_date)






class Stocks(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases = ['spt'],
                      help = 'Shows the closing price of the stock for the today')
    async def stockpricetoday(self, ctx, *, tickers):
        stocks = tickers.split(' ')
        prices = ''

        for stock in stocks:
            stock_name = f'{stock.upper():8}'
            prices += stock_name
            try:
                price = get_today_stock_price(stock)
                prices += f'{price:8}' + '\n'
            except:
                prices += 'This stock does not exist\n'

        embed = discord.Embed(title = 'Today\'s Closing Stock Prices', description = prices, color = discord.Color.red())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f'Requested by {ctx.author.display_name}')
        await ctx.send(embed = embed)




# Setup that allows us to connect the cog to the bot
def setup(bot):
    bot.add_cog(Stocks(bot))