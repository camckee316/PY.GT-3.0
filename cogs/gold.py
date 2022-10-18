import discord
from discord.ext import commands


class Gold(commands.Cog):


    def __intit__(self, bot):


        self.bot = bot


    @discord.slash_command(description="Information on Gold Pokemon.")
    async def gold(self, ctx):
        embed = discord.Embed(
            title = "Gold Pokemon",
            description= "Information on Gold Pokemon.",
            color=discord.Colour.random(),
        )
        embed.add_field(
            name="Gold Pokemon", 
            value="Increase Speed by 10%! Can only be purchased with tokens. Tokens are obtained by donating or FD (Friend Donation)", 
            inline=True)
        await ctx.respond(embed=embed)

def setup(bot):  
    bot.add_cog(Gold(bot))