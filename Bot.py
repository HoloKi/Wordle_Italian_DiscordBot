import discord
import asyncio
import time
from discord.ext import commands
from discord import TextChannel
from googlesearch import search 

random = __import__("random")
client = commands.Bot(command_prefix = '.')
client.remove_command('help')

#COMANDO PER LO STATUS DEL BOT+ ID BOT + NOME BOT
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Sto facendo i cassi miei'))
    print('Il bot è pronto e funzionante.')
    print(client.user.name)
    print(client.user.id)
    print('------')

#comando per la ricerca in web
@client.command()
async def cerca(ctx, *,arg):
    for url in search(arg, stop=1):
        await ctx.send(url)

#COMANDO PING
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

#COMANDO PER FIRE
@client.command()
async def fire(ctx):
    responses = ['https://i.kym-cdn.com/photos/images/newsfeed/001/505/718/136.jpg', #gattoschifomado
                 'https://res.cloudinary.com/lmn/image/upload/c_limit,h_360,w_640/e_sharpen:100/f_auto,fl_lossy,q_auto/v1/gameskinnyc/b/i/t/bit-heroes-skeleton-key-0dd37.png', #bit heroes
                 'https://imgur.com/a/zNHwlcp', #imgur bhchiesa crossover 
                 'https://imgur.com/a/J9iUd5L', #notre chiesa bh
                 'https://cdn02.nintendo-europe.com/media/images/10_share_images/games_15/nintendo_switch_download_software_1/H2x1_NSwitchDS_Warframe_image1600w.jpg'] #warframe
    await ctx.send(random.choice(responses))

#COMANDO PER ROSE
@client.command()
async def rose(ctx):
    responses = ['https://i.kym-cdn.com/photos/images/original/000/862/912/fdf.gif', #anime ass
                 'https://media.giphy.com/media/6CBGoJnEBbEWs/giphy.gif', #red taiga
                 'https://media.giphy.com/media/jTU09JLRaYCt2/giphy.gif', #taiga sfrontata
                 'https://media.giphy.com/media/wUf0jPd2ksY92/giphy.gif', #jojo balls
                 'https://media.giphy.com/media/gDciyiNcDhYXu/giphy.gif', #ohmygod joo reference
                 'https://i.kym-cdn.com/photos/images/newsfeed/000/869/852/a28.gif', #n'altro culo
                 'https://i.pinimg.com/originals/d5/8b/5b/d58b5be495a07dfda4672aaf7aa2e35b.gif', #donnasenzabocce
                 'https://media.giphy.com/media/SpzdWtMmREEaA/giphy.gif'] #taiga felice
    await ctx.send(random.choice(responses))

#COMANDO PER CAPPU
@client.command()
async def cappu(ctx):
    responses = ['https://tenor.com/y8kZ.gif', #ragazzo cool
                'https://tenor.com/rpCn.gif'] #sguardo sexy
    await ctx.send(random.choice(responses))

#COMANDO PER ARTY
@client.command()
async def arty(ctx):
    responses = ['Lasciami stare',
                 'Vuoi un ban?',
                 'https://media.giphy.com/media/uC9e2ojJn1ZXW/giphy.gif',
                 'https://media.giphy.com/media/qPD4yGsrc0pdm/giphy.gif',
                 'Te la sei cercata',
                 'Continua cosi e ti banno',
                 'Sono pigro daiiii']
    await ctx.send(random.choice(responses))


#COMANDO PER LE FRASI FILOSOFICHE DI PETTI
@client.command()
async def petty(ctx):
    embed = discord.Embed(
        color = discord.Colour.red()  
    )
    
    embed.set_author(name='Saggio Petti')
    responses = ['Quando il dito indica la luna lo stolto guarda il dito',
                 'Cadi sette volte, rialzati otto',
                 'Quando piove lo stolto impreca contro gli dei, il saggio si procura un ombrello',
                 'Una coscienza pulita è il cuscino migliore',
                 'Il momento migliore per piantare un albero era 20 anni fa. Il secondo miglior momento è ora',
                 'Il nostro primo insegnante è il nostro cuore',
                 'La donna è detta creatura debole, ma un suo pelo tira più di una coppia di elefanti.',
                 'In un buon libro il meglio è tra le righe',
                 'Anche con una sella dorata un asino non diventa un cavallo',
                 'Una buona risata allunga la vita',
                 'Amare ed essere saggi è impossibile']
    embed.add_field(name = 'dile:', value = (random.choice(responses)), inline=False)
    await ctx.send(embed=embed)

#COMANDO PER NIC
@client.command()
async def nic(ctx):
    await ctx.send('https://media.giphy.com/media/3h40Gfu1mwk5xFAfcN/giphy.gif') #hanzo

#COMANDO PER YODA
@client.command()
async def yoda(ctx):
    responses = ['https://media0.giphy.com/media/26vIeEarfjFwKCEow/giphy.gif', #rainbow6
                 'https://thumbs.gfycat.com/HotElatedIbizanhound-max-1mb.gif'] #rainbowmemes
    await ctx.send(random.choice(responses))



#COMANDO PER EVAN
@client.command()
async def eva(ctx):
    await ctx.send('Sei bello Rose!')

#COMANDO PER LA GIF DI CANNELLA
@client.command()
async def canny(ctx):
    await ctx.send('https://media0.giphy.com/media/1jadHTB4xIMBgNT0xd/giphy.gif')

#COMANDO PER SAPERE CHI SCRIVE E VISUALIZZARLO SULLA BOARD DI PYTHON
@client.event
async def on_message(message):
    author = message.author
    content = message.content
    channel = message.channel
    print(author, channel, content)
    await client.process_commands(message)

# COMANDO HELP PER VEDERE QUALI COMANDI DEL BOT CI SONO

@client.command(pass_context = True)    
async def help(ctx):
    embed = discord.Embed(
        color = discord.Colour.orange()  
    )
    
    embed.set_author(name='Help')
    embed.add_field(name = '.cerca', value = 'Invia il primo risultato della ricerca', inline=False)
    embed.add_field(name = '.rose', value = 'Le migliori gif di Rose', inline=False)
    embed.add_field(name = '.arty', value = 'Il meglio di Arty', inline=False)
    embed.add_field(name = '.cappu', value = 'Le migliori gif di Cappu', inline=False)
    embed.add_field(name = '.fire', value = 'Le migliori gif di Firemage', inline=False)
    embed.add_field(name = '.petty', value = 'I migliori proverbi dal mondo', inline=False)
    embed.add_field(name = '.eva', value = 'La frase meno iconica di Evan', inline=False)
    embed.add_field(name = '.nic', value = 'La miglior gif di Nic', inline=False)
    embed.add_field(name = '.clear', value = 'Permette di default di cancellare 5 messaggi precedenti, Admin only', inline=False)
    embed.add_field(name = '.yoda', value = 'Alcune gif divertenti su r6', inline=False)
    embed.add_field(name = '.canny', value = 'Le sue gif preferite', inline=False)
    embed.add_field(name = '.ping', value = 'Controlla quanto lagga Arty', inline=False)
    embed.add_field(name = 'Il bot è semplice e sviluppato col culo, abbiate pazienza.', value = 'Imparerò a programmare, lo giuro', inline=False)
    
    await ctx.send(embed=embed)

#COMANDO PER PURGARE I MESSAGGI
@client.command()
@commands.has_permissions(manage_messages= True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

client.run('token')
