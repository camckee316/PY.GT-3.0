import discord
from discord.ext import commands


class Shiny(commands.Cog):


    def __intit__(self, bot):


        self.bot = bot


    @discord.slash_command(description="Informaton on Shiny Pokemon.")
    async def shiny(self, ctx):
        embed= discord.Embed(
            title="Shiny Pokemon", 
            description="Information on Shiny Pokemon.",
            color=discord.Colour.random(),
        )
        embed.add_field(
            name="Shiny Pokemon",
            value="Increase's Hit Points by 10%. Chances of finding them in the wild 1/8192 without premium account and 1/4096 with premium.",
            inline= True
        )
        await ctx.respond(embed=embed)

def setup(bot):  
    bot.add_cog(Shiny(bot))