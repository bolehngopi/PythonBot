import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'h!')

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('Idk'))
  print('Bot is now online')

@client.event
async def on_message_error(ctx, error):
  pass

@client.command()
async def delete(ctx, amount : int):
  await ctx.channel.purge(limit=amount)
  
async def ping(ctx):
    if round(client.latency * 1000) <= 50:
        embed=discord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! The ping is **{round(client.latency *1000)}** milliseconds!", color=0x44ff44)
    elif round(client.latency * 1000) <= 100:
        embed=discord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! The ping is **{round(client.latency *1000)}** milliseconds!", color=0xffd000)
    elif round(client.latency * 1000) <= 200:
        embed=discord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! The ping is **{round(client.latency *1000)}** milliseconds!", color=0xff6600)
    else:
        embed=discord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! The ping is **{round(client.latency *1000)}** milliseconds!", color=0x990000)
    await ctx.send(embed=embed)

@delete.error
async def delete_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Please specify a amount of messsage to delete')


client.run('Your Token')
