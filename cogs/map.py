import discord
from discord.ext import commands


class Map(commands.Cog):


    def __intit__(self, bot):


        self.bot = bot


    @discord.slash_command(description="Map Links.")
    async def map(self, ctx):
        embed = discord.Embed(
            title = "Map links for PokemonGods",
            description= "Choose a link:",
            color=discord.Colour.random(),
        )
        embed.add_field(
            name="Orden Region", 
            value="http://i.imgur.com/dYlAaGQ.jpg", 
            inline=True
            )

        embed.add_field(
            name="Blackfell Caverns",
            value="https://i.imgur.com/OsSxtei.jpeg",
            inline=True
        )
        embed.add_field(
            name="Onderblade Mines", 
            value="http://i.imgur.com/yUmYgLB.jpg", 
            inline=True
            )

        embed.add_field(
            name="Willowsteen Cabin",
            value="https://i.imgur.com/1DxwN0a.jpg",
            inline=True
        )
        embed.add_field(
            name="Trial 8 Region", 
            value="https://i.imgur.com/jOE293k.jpeg", 
            inline=True
            )

        embed.add_field(
            name="Room 2 Maze",
            value="https://i.imgur.com/7v0sKsD.jpeg",
            inline=True
        )
        embed.add_field(
            name="Trial 2 Region", 
            value="https://i.imgur.com/5AYLFLD.png`", 
            inline=True
            )

        await ctx.respond(embed=embed)

def setup(bot):  
    bot.add_cog(Map(bot))