import discord
from discord.ext import commands


class Legend(commands.Cog):


    def __intit__(self, bot):


        self.bot = bot


    @discord.slash_command(description='List of Legendary and Mythical Pokemon in game.')
    async def legend(self, ctx):
        embed=discord.Embed(
            title="Legendary and Mythical Pokemon.",
            #description="This pokemon are obtainable in game.",
            color=discord.Colour.random(),
        )
        embed.add_field(
            name= "Legendary Pokemon",
            value= "Articuno, Giratina, Cresselia, Heatran, Latios, Latias, Mewtwo, Moltres, Regice, Regirock, Registeel, Zapdos",
            inline=True
        )
        embed.add_field(
            name="Mythical Pokemon",
            value= "Manaphy, Mew, Phione, Shaymin",
            inline=True
        )

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Legend(bot))