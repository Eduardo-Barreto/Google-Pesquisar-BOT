import discord
import asyncio
import random
from unicodedata import normalize
from time import sleep

import playlists

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

client = discord.Client()

@client.event
async def on_ready():
    print('\npai ta on\n')

@client.event
async def on_message(comando):

    filmes = 'gatinhas e gatões, clube da luta, com amor Simon, o plano imperfeito, your name, sombra lunar, tomorrowland, glass, atlantis o reino perdido, nerve, pequenosi nvasores, capitão fantástico, naruto, about time, clubs dos cinco, por lugares incríveis, o mínimo pra viver, klaus, up - altas aventuras, bee movie, tá dando onda, hotel transilvânia, a fantástica fábrica de chocolates, space jam, scoob, jovens loucos e rebeldes'

    conteudo = remover_acentos(comando.content).lower()

    if comando.content == 'marselo':
        await comando.channel.send('marselo!')

    if conteudo.startswith('!playlist'):

        playlist = conteudo[10:]
        print(playlist)

        
        if playlist == 'completa':
            await comando.channel.send(playlists.completa)

        if playlist == 'roberto carlos':
            await comando.channel.send(playlists.roberto_carlos)

        if playlist == 'jao':
            await comando.channel.send(playlists.jao)

        if playlist == 'polado':
            await comando.channel.send(playlists.polado)

        if playlist == 'fll':
            await comando.channel.send(playlists.fll)

        if playlist == 'naosemate':
            await comando.channel.send(playlists.naosemate)

        if playlist == 'beatles':
            await comando.channel.send(playlists.beatles)

    if conteudo.startswith('!comandos'):
        await comando.channel.send('```!playlist\n!moeda\n!escolha```')  
        
    if conteudo.startswith('marselo te amo') or conteudo.startswith('te amo marselo'):
        await comando.channel.send(f'Eu sou um robô, eu não tenho sentimentos {comando.author.name}, me perdoe...\nMesmo assim eu acho que eu te amaria se fosse possível')

    if conteudo.startswith('voce fala isso pra todas'):
        await comando.channel.send('Sim ué, fui programado pra isso, o que mais você esperava?')

    if conteudo.startswith('coe bot'): #Teste do bot
        await comando.channel.send('PAI TA ON 😎😎😎😎😎😎 ')
    
    if conteudo.startswith('!moeda'): #Cara ou coroa
        escolha = random.randint(1,2)
        if escolha == 1:
            await comando.add_reaction('😀')
        else:
            await comando.add_reaction('👑')

    if conteudo.startswith('!escolha'): #Escolha entre coisas

        opcoes = comando.content[9:].replace(" ou ", ", ").split(", ")

        escolha = random.randint(0, len(opcoes)-1)

        escolha = opcoes[escolha]

        await comando.channel.send(f'Já que você não consegue se decidir, eu escolho: {escolha}')

    if conteudo == 'core values' or conteudo == 'o o respeito':
        await comando.channel.send('https://media.discordapp.net/attachments/706686089267773441/716383466219896952/unknown.png')

    if conteudo == 'eu te odeio bot':
        await comando.channel.send('eu também me odeio 😎😎')

    if 'gracious professionalism' in conteudo:
        await comando.channel.send('HEY!')

    if conteudo == '!convite':
        await comando.channel.send('https://discord.com/invite/NcmFqWX')

    if conteudo == 'obg marselo' or conteudo == 'vlw marselo':
        await comando.channel.send('tmj man, qlq coisa da um toque no <@467736844621316106>')

    if conteudo == 'eu sou inevitavel':
        await comando.channel.send('e eu sou o homem de ferro 😎😎')

    if conteudo == 'bem vindo ao mundo real':
        await comando.channel.send('é uma droga, você vai amar')

    if conteudo == 'eu nao preciso disso':
         await comando.channel.send('meu marido tem dois empregos  😎😎')

    if conteudo.startswith('!azeitona'):
        await comando.channel.send('https://www.youtube.com/watch?v=1S8BpI8zqXU')

    if 'me sinto fraco' in conteudo:
        await comando.channel.send('que a força esteja com você')

    if 'mimimi' in conteudo:
        await comando.channel.send('aaah seboso https://media.tenor.com/images/fe642b387326aedca0f28b1d634522d6/tenor.gif')

    if 'conta pra ninguem' in conteudo:
        await comando.channel.send('primeira regra do clube da luta')

    if  conteudo == '!listafilmes':
        filmes = filmes.split(',')
        final = ''
        for c in range(0, len(filmes)):
            final += filmes[c] + ','

        final = final[0:-1]
        await comando.channel.send(f'essa é a sua lista de filmes: ```{final}```')

        lala = final

        opcoes = lala.replace(" ou ", ", ").split(", ")

        escolha = random.randint(0, len(opcoes)-1)

        escolha = opcoes[escolha]

        await comando.channel.send(f'Já que você não consegue se decidir, eu escolho: `{escolha}`')

    if conteudo.startswith('!rmfilme'):
        filme = conteudo[8:]

        filmes = filmes.replace(filme, '')

    if 'estao prontas criancas' in conteudo:
        await comando.channel.send('estamos capitão')

    if 'eu nao ouvi direito' in conteudo:
        await comando.channel.send('ESTAMOS CAPITÃO')

    if 'geladeira' in conteudo:
        await comando.channel.send('foi, funcionou')

    if 'roi' in conteudo:
        await comando.channel.send('Leticia né?')

    if conteudo == 'bah neh aham':
        await comando.channel.send('bah neh')

    if 'samuel' in conteudo:
        await comando.channel.send('bobo.')

    if 'bicicleta' in conteudo:
        await comando.channel.send('bailarina')

    if 'ping' in conteudo:
        await comando.channel.send('pong')

client.run('NzExNDE0NTMyODUzMDcxODgy.XsCqag.OiP6NeXCXTo7t6KjaI6XVeemp0s')