import discord
from discord.ext import commands


class NonMap(commands.Cog):


    def __intit__(self, bot):


        self.bot = bot


    @discord.slash_command(description="A list of pokemon not found on maps.")
    async def nonmap(self, ctx):
        embed = discord.Embed(
            title = "NonMap's",
            description= "Pokemon that are not found on the normal map.",
            color=discord.Colour.random(),
        )
        embed.add_field(
            name="Nonmap Pokemon:", 
            value="Alomomola, Amaura, Audino, Axew, Basculin, Bergmite, Binacle, Carbink, Chingling, Clauncher, Cottonee, Cranidos, Croagunk, Cryogonal, Cubchoo, Darumaka, Dedenne, Deino, Drifloon, Drilbur, Druddigon, Durant, Emolga, Espurr, Frillish, Glaceon, Glameow, Golett, Goomy-Shiny Goomy, Gothita, Hawlucha, Helioptile, Happiny, Honedge, Inkay, Karrablast, Klink, Lillipup, Litwick, Mantyke, Mienfoo, Mimejr, Minccino, Mothim, Munna, Noibat, Pachirisu, Pancham, Pawniard,Phantum, Pumpkaboo, Riolu, Roggenrola, Rotom, Sandile, Scraggy, Shieldon, Sigilyph, Skorupi, Skrelp, Snover, Solosis, Spiritomb, Spritzee, Stunfisk, Swirlix, Timburr, Tirtouga, Trubbish, Tympole, Tynamo, Tyrunt, Vanillite, Vullaby, Woobat, Wormadam, Yamask", 
            inline=True
        )
        embed.set_footer(text="These pokemon are usually found in events.")
        await ctx.respond(embed=embed)

def setup(bot):  
    bot.add_cog(NonMap(bot))