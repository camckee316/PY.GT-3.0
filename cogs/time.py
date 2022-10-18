import discord
from discord.ext import commands


class Time(commands.Cog):


    def __intit__(self, bot):


        self.bot = bot


    @discord.slash_command(description="Day/Night cycle.")
    async def time(self, ctx):
        embed = discord.Embed(
            title = "Day/Night Cycle for pokemongods",
            description= "03:00 - 09:00 Night \n 09:00 - 15:00 Day \n 15:00 - 21:00 Night \n 21:00 - 03:00 Day",
            color=discord.Colour.random(),
        )
        embed.set_footer(text="In game's English chat, type /time to know the time.")
        await ctx.respond(embed=embed)

def setup(bot):  
    bot.add_cog(Time(bot))