import discord
from bot_logic import gen_pass
from discord.ext import commands
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix = "$",intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send ('Hi')

@bot.command()
async def bye(ctx):
    await ctx.send ('😥chao')

@bot.command()
async def como_estas(ctx):
    await ctx.send ('bien y tu?(bien o mal)')

@bot.command()
async def mal(ctx):
    await ctx.send ('oh siempre hay un dia malo')

@bot.command()
async def bien(ctx):
    await ctx.send ('oh que bien sigue feliz')

@bot.command()
async def password(ctx):
    await ctx.send (gen_pass(10))

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
   
bot.run("MTI3ODE1ODMwMTYzNjQ2MDYwNA.Gz_Jzh.zzTcuKQiLYlk78g9VupcS1vBhPThoNxiaxYEv8")
