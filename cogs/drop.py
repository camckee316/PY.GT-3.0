import discord
from discord.ext import commands


class Drop(commands.Cog):


    def __intit__(self, bot):


        self.bot = bot


    @discord.slash_command(description="Pokemon that drop items.")
    async def drop(self, ctx):
        embed = discord.Embed(
            title = "List of Pokemon that may drop an item.",
            #description= "",
            color=discord.Colour.random(),
        )
        embed.add_field(
            name="Pokemon drops are not always 100%.", 
            value="Caterpie(Pokeball), Sentret(Pokeball), Pidgey(Ev Reducer,), Weedle(Ev Reducer), Lotad(Ev Reducer), Spinarak(Ev Reducer), Wingull(Diner Coupon), Zubat(Rock Present), Misdreavus(Hypnotic Orb), Paras(Tiny Mushroom), Miltank(MooMoo Milk), Geodude(Geode), Larvesta(Solar Drop)", 
            inline=True)
        await ctx.respond(embed=embed)

def setup(bot):  
    bot.add_cog(Drop(bot))