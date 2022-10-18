import discord
from discord.ext import commands


class Invite(commands.Cog):


    def __intit__(self, bot):


        self.bot = bot


    @discord.slash_command(description="Invites bot to your server.")
    async def invite(self, ctx):
        embed = discord.Embed(
            title = "Click the link below to invite me to your server.",
            description= "https://discord.com/api/oauth2/authorize?client_id=1030975625802043486&permissions=8&scope=bot%20applications.commands",
            color=discord.Colour.random(),
        )

        await ctx.respond(embed=embed)

def setup(bot):  
    bot.add_cog(Invite(bot))