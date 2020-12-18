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
  
@client.command()
async def ping(ctx):
    await ctx.send('Pong! Your ping latency is {0}!'.format(round(client.latency * 1000)))

@delete.error
async def delete_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Please specify a amount of messsage to delete')


client.run('Your Token')
