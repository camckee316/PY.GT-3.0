from pickle import TRUE
import discord
from discord.ext import commands


class Help(commands.Cog):


    def __intit__(self, bot):


        self.bot = bot


    @discord.slash_command(description="List of commands")
    async def help(self, ctx):
        embed = discord.Embed(
            title = "Commands for bot.",
            #description= "Information on Gold Pokemon.",
            color=discord.Colour.random(),
        )
        embed.add_field(name="Escape", value="Usage:`/escape`\nProvides a list of pokemon that can escape during a battle.", inline=True)
        embed.add_field(name="Follow", value="Usage:`/follow`\nProvides a list of pokemon that can follow you in game.", inline=True)
        embed.add_field(name="Drop", value="Usage:`/drop`\nGives a list of pokemon the may occasionally drop items.", inline=True)
        embed.add_field(name="Gold", value="Usage:`/gold`\nInformation on gold pokemon.", inline=True )
        embed.add_field(name="History", value="Usage:`/history`\nHistory of bot.", inline=True)
        embed.add_field(name="Legend", value="Usage:`/legend`\nProvides a list of legendary and mythical pokemon found in game.", inline=True)
        embed.add_field(name="NonMap", value="Usage:`/nonmap`\nProvides a list of non-map pokemon in game.", inline=True)
        embed.add_field(name="Map", value="Usage:`/map`\nProvides maps of serveral regions of the game.", inline=True)
        embed.add_field(name="NoBreed", value="Usage:`/nobreed`\nPokemon that can not breed in game. Also known as Type S Pokemon.", inline=True)
        embed.add_field(name="Shiny", value="Usage:`/shiny`\nProvides information on shiny pokemon.", inline=True)
        embed.add_field(name="Time", value="Usage:`/time`\nProvides information about the day and night cycle according server time. Type `/time` in english chat of game server.", inline=True)
        embed.add_field(name="Nature", value="Usage:`/nature`\nShow a nature chart.", inline=True)
        #commands not added yet need to read from file. also all commands need 1 arg
        embed.add_field(name="Pokeinfo", value="Usage: `/pokeinfo pokemonName` \n Provides national pokedex number, pokemon name, evolutions, what map/event they are found on, ev yield, possible abilities, basestats, growth rate and pokemon type.", inline=True)
        embed.add_field(name="Ability", value="Usage:`/ability abilityName` \nProvides information about a pokemon ability.", inline=True)
        embed.add_field(name="Area", value="Usage:`/area mapName` \nProvides information on what map pokemon are found, and there ev yield", inline=True)
        embed.add_field(name="Breed", value="Usage:`/breed pokemonName`\nGives a list of pokemon breeding partners, for egg moves.", inline=True)
        embed.add_field(name="Cover", value="Usage:`/cover pokemonType` \n Usage:`/cover pokemonType1, pokemonType2`\nProvides the coverage type or type combination.", inline=True)
        embed.add_field(name="Evtrain", value="Usage:`/evtrain stat` \n Example `/evtrain hp`\nProvides information on which pokemon to faint to collect that ev yield.", inline=True)
        embed.add_field(name="Item", value="Usage:`/item nameOfItem`\n Provides information of item.", inline=True)
        embed.add_field(name="Move", value="Usage:`/move nameOfMove`\nLists the move and gives description of power, accuracy and what caterogy it is in.", inline=True)
        embed.add_field(name="MoveTutor", value="Usage:`/movetutor moveType`\n Provides information of the move tutor and the moves taught.", inline=True)
        embed.add_field(name="Weak", value="Usage:`/weak pokemonName`\n Provides information on the pokemon weakness, resistance, and immuities.", inline=True)
        embed.add_field(name="Rebirth", value="Usage:`/rebirth pokemonName` \n Provides information on where to rebirth legendaries. Rebirthing requires having rebirth crystals.", inline=True)
        embed.add_field(name="Tournament", value="Usage:`/tournament nameOfTournament` \n Provides infomation on which pokemon can be won in that tournament.", inline=True)
        embed.add_field(name="PokeMove", value="Usage:`/pokemove nameOfPokemon` \n Provides information on the pokemon moves are learn. By level up, hm/tm, and egg moves.", inline=True)

        await ctx.respond(embed=embed, ephemeral=True)

def setup(bot):  
    bot.add_cog(Help(bot))