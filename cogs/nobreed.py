import discord
from discord.ext import commands


class NoBreed(commands.Cog):


    def __intit__(self, bot):


        self.bot = bot


    @discord.slash_command(description="Pokemon that can't breed in game.")
    async def nobreed(self, ctx):
        embed = discord.Embed(
            title = "Type S Pokemon/ S Grade Pokemon",
            description= "These pokemon can not breed in game. ",
            color=discord.Colour.random(),
        )
        embed.add_field(
            name="Pokemon:", 
            value="Ditto, Dratini, Dragonair, Dragonite, Larvitar, Pupitar, Tyranitar, Bagon, Shelgon, Salamence, Beldum, Metang, Metagross, Gible, Gabite, Garchomp, Deino, Zweilous, Hydreigon, Goomy, Sliggoo, Goodra", 
            inline=True)
        await ctx.respond(embed=embed)

def setup(bot):  
    bot.add_cog(NoBreed(bot))