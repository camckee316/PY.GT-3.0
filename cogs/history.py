import discord
from discord.ext import commands


class History(commands.Cog):


    def __intit__(self, bot):


        self.bot = bot


    @discord.slash_command(description="The history.")
    async def history(self, ctx):
        embed = discord.Embed(
            title = "History of GyaradosThief",
            #description= "",
            color=discord.Colour.random(),
        )
        embed.add_field(
            name="KarpThief", 
            value="Was made for irc. It was in c++ or mIRC. Made after we lost the original bot that was in irc. Made and hosted by camckee, with coding help from Nexus and PrincessPhoienx.", 
            inline=True
        )

        embed.add_field(
            name="GyaradosThief", 
            value="An upgrade of karpThief. As irc was not as popular. KT was recoded using discord.js v12, for the use in discord. Made by camckee. Hosted by repl.it. Coding help from Nexus and PrincessPhoienx", 
            inline=True
        )

        embed.add_field(
            name="GyaradosThief 2.0", 
            value="Upgrade of GT. Included new commands and embed messages. Coded in discord.js v13, as v12 was not supported anymore. Recoded by .Eklavya11 and camckee. Hosted by wurpus.host.", 
            inline=True
        )

        embed.add_field(
            name="GyaradosThief 3.0", 
            value="Upgrade of GT 2.0. Coded in py-cord 2.2.0. Coded in py-cord. Is actually just a duplicate of GT 2.0 just in a different programing language and uses only slash commands. Coding help from Devon(DustinFoes) and Slim Beatbox", 
            inline=True
        )
        
        embed.set_footer(text="GT 3.0 is in production as of 10/15/2022. Release date unknow at this time.")

        await ctx.respond(embed=embed)

def setup(bot):  
    bot.add_cog(History(bot))