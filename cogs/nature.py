import discord
from discord.ext import commands


class Nature(commands.Cog):


    def __intit__(self, bot):


        self.bot = bot


    @discord.slash_command(description="Shows nature chart.")
    async def nature(self, ctx):
        embed = discord.Embed(
            title = "Pokemon Natures",
            #description= "Information on Gold Pokemon.",
            color=discord.Colour.random(),
        )
        embed.set_image(url="https://i.imgur.com/M6bmGq9.jpg")
        
        await ctx.respond(embed=embed)

def setup(bot):  
    bot.add_cog(Nature(bot))