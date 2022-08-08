import discord
import asyncpraw
from discord.ext import commands




class Reddit(commands.Cog):


    # Initialization that allows us to access the bot within the cog
    def __init__(self, bot):
        self.bot = bot # essential for bot to work


    @commands.command(aliases = ['rdt', 'r'],
                      help = 'Shows the five hottest posts in the specified subreddit')
    async def reddit(self, ctx, sub = 'csmajors', num = 5):

        reddit = asyncpraw.Reddit('PythonBot', config_interpolation = 'basic')

       

        reddit.read_only = True

        subreddit = await reddit.subreddit(sub)

        posts = []

        hot = subreddit.hot(limit = num)

        async for submission in hot:
            posts.append(submission)
        
        for post in posts:
            title = post.title
            permalink = post.permalink
            upvotes = post.score
            ratio = post.upvote_ratio * 100
            comments = post.num_comments

            url = post.url
            embed = discord.Embed(title = title,
                                  description = f'https://www.reddit.com{permalink}',
                                  timestamp = ctx.message.created_at,
                                  url = url,
                                  color = discord.Color.red())
            embed.set_image(url = url)
            embed.add_field(name = 'Upvotes 👍🏻', value = upvotes, inline = True)
            embed.add_field(name = 'Upvote Ratio ⬆️ ⬇️', value = f'{float(ratio):g}%')
            embed.add_field(name = 'Comments 💬', value = comments, inline = True)
            embed.set_footer(text = ctx.author.display_name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)

        await reddit.close()




def setup(bot):
    bot.add_cog(Reddit(bot))