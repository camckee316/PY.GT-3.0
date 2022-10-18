import discord
from discord.ext import commands


class Escape(commands.Cog):


    def __intit__(self, bot):


        self.bot = bot


    @discord.slash_command(description="Information on Pokemon that can escape in battle.")
    async def escape(self, ctx):
        embed = discord.Embed(
            title = "Escapable Pokemon",
            #description= "Information on Gold Pokemon.",
            color=discord.Colour.random(),
        )
        embed.add_field(
            name="Pokemon that can escape in battle.", 
            value="Articuno, Cubone, Delibird, Dragonair, Dratini, Eevee, Grimer, Heracross, Magnemite, Moltress, Mr.Mime, Phanpy, Porygon, Quagsire, Snubbull, Tangela, Teddiursa, Togetic, Umbreon, Unown, Zapdos", 
            inline=True)
        await ctx.respond(embed=embed)

def setup(bot):  
    bot.add_cog(Escape(bot))