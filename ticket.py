import discord #burasi full modül yeri
from discord.ext import commands
from discord.utils import get
from discord import Embed, Color
import DiscordUtils
import os
from discord.ext.commands import has_permissions, MissingPermissions
import json



#burasi komuta özel prefix isterseniz belirlersiniz isterseniz silersiniz
intents = discord.Intents.default()

intents.members = True
client = commands.Bot(command_prefix = "prefix gir", intents = intents)
client.remove_command("yardım")
#


#buralarda ticket sistemi yeri
@client.command(pass_context=True)
async def ticket(ctx):
    guild = ctx.guild
    embed = discord.Embed(
        title = 'Ticket Sistem',
        description = '📩 Tıklayarak Ticket Açabilirsin.',
        color = 0
    )

    embed.set_footer(text="Ticket Sistemi")

    msg = await ctx.send(embed=embed)
    await msg.add_reaction("📩")
    reaction = await msg.fetch_message(msg.id)


    await client.wait_for("reaction_add, check=check")

    if reaction == '📩':
        await guild.create_text_channel(name=f'Ticket - {reaction.author.name}')
