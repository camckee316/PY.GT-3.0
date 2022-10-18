from re import T
from tkinter.tix import Tree
import discord
from discord.ext import commands


class Follow(commands.Cog):


    def __intit__(self, bot):


        self.bot = bot


    @discord.slash_command(description="Pokemon that can follow you in game.")
    async def follow(self, ctx):
        embed = discord.Embed(
            title = "Follower Pokemon",
            #description= "Pokemon that can follow you in game.",
            color=discord.Colour.random(),
        )
        embed.add_field(
            name="Kanto Region Followers:", 
            value="Bulbasaur  Ivysaur  Venusaur  Charmander  Charmeleon  Charizard  Squirtle  Wartotle  Blastosie  Caterpie  Pikachu  Raichu  Krabby  Magikarp", 
            inline=True)
        embed.add_field(
            name="Johto Region Followers:",
            value="Chikotira  Bayleef  Meganium  Cyndaquil  Quilava  Typhlosion  Totodile  Croconaw  Feraligatr  Sentret",
            inline=True
        )
        embed.add_field(
            name="Hoenn Followers:", 
            value= "Treecko  Grovyle  Sceptile  Torchic  Combusken  Blaziken  Mudkip  Marshtomp  Swampert  Wurmple  Spinda",
            inline=True
        )
        embed.add_field(
            name="Shinnoh Followers:",
            value="Turtwig  Grotle  Torterra  Chimchar  Monferno  Infernape  Piplup  Prinplup  Empoleon  Bidoof",
            inline=True
        )
        embed.add_field(
            name= "Unova Followers:",
        value= "Victini  Snivy  Servine  Serperior  Tepig  Pignite  Emboar  Oshawott  Dewott  Samurott  Patrat  Munna  Musharna  Cottonee  Petilil  Krokorok  Zorua  Minccino  Cobalion  Terrakion  Virizion  Keldeo",
        inline=True
        )
        embed.add_field(
        name= "Kalos Followers:",
        value= "Chespin  Quilladin  Chesnaught  Fennekin  Braixen  Delphox  Froakie  Frogadier  Greninja",
        inline= True
        )
        await ctx.respond(embed=embed)

def setup(bot):  
    bot.add_cog(Follow(bot))