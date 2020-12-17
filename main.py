import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'h!')

@client.event
async def on_ready():
  print('Bot is now online')

@client.error
async def on_message_error(ctx, error):
  pass

@client.command()
async def purge(ctx, amount : int):
  await ctx.channel.purge(limit=amount)

@client.error
async def purge_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Please specify a amount of messsage to delete')

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

client.run('NjUzMjI3NjYzNjk1MTUxMTE0.Xez7qw.ESin0jCD9TKCBhO_29psJdMT-6M')