'''
Not inside of a cog.
'''

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.command()
@has_permissions(administrator=True)
async def kicknorole(ctx):
    members = ctx.guild.members
        
    for member in members:
        if len(member.roles) == 1:
            await member.kick()
            print(member.name) # Just for debug reasons to make sure the command is working.
    await ctx.send('Done!')

bot.run('TOKEN')

'''
Inside of a cog. Make sure to setup your cogs folder in the main file. 
'''

class KickNoRole(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(administrator=True)
    async def kicknorole(self, ctx):
        members = ctx.guild.members
                
        for member in members:
            if len(member.roles) == 1:
                await member.kick()
                print(member.name) # Just for debug reasons to make sure the command is working.
        await ctx.send('Done!')

def setup(bot):
    bot.add_cog(KickNoRole(bot))