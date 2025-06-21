import discord
from discord.ext import commands, tasks
from datetime import time

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)


#função que inicia o bot, mostrando no terminal que foram carregados X comandos
@bot.event
async def on_ready():
    sincs = await bot.tree.sync()
    print(f"{len(sincs)} comandos sincronizados!")
    enviar_mensagem.start()
    print("Bot inicializado com sucesso!")



#EVENTOS
@bot.event
async def on_message(msg:discord.Message):
    if msg.author.bot:
        return
    await bot.process_commands(msg)
    # await msg.reply(f"O usuário {msg.author.mention} enviou uma mensagem no canal {msg.channel.name}")

#indica que alguem entro em X canal
@bot.event
async def on_member_join(membro:discord.Member):
    #canal = bot.get_channel(CHAVE DO SEU CANAL)
    canal = bot.get_channel()
    await canal.send(f"{membro.mention} entrou no servidor!")

@bot.event
async def on_reaction_add(reacao:discord.Reaction, membro:discord.Member):
    await reacao.message.reply(f"O membro {membro.name} reagiu a mensagem com {reacao.emoji}")



#COMANDOS
@bot.command()
async def ola(ctx:commands.Context):
    nome = ctx.author.name
    await ctx.reply(f"Olá, {nome} !tudo bem?")

@bot.command()
async def enviar_embed(ctx:commands.Context):
    minha_embed = discord.Embed()
    minha_embed.title = "name"
    minha_embed.description = "Mascote oficial do bot"
    
    # definir o local da imagem e depois o nome
    imagem = discord.File("local.jpg", "nome.jpg")
    #usar o nome
    minha_embed.set_image(url="attachment://nome.jpg")
    minha_embed.set_thumbnail(url="attachment://nome.jpg")

    minha_embed.set_footer(text="Esse é o footer da embed")
    minha_embed.set_author(name="name", icon_url="https://i.pinimg.com/736x/ee/d8/7a/eed87a55a566c048e0897bf05ca202f1.jpg")

    await ctx.reply(embed=minha_embed, file=imagem)



#mensagem programada para um horario especifico, sendo com 3h a menos ex: 21 para exibir as meia noite
@tasks.loop(time=time(21))
async def enviar_mensagem():
    #canal = bot.get_channel(CHAVE DO SEU CANAL)
    canal = bot.get_channel()
    await canal.send("Mensagem programada: Meia noite, horário oficial do óleo de macaco!")



#comando para o bot nao bugar apos um pequeno periodo, esses comandos sao usados com /
@bot.tree.command()
async def ola(interact:discord.Interaction):
    #await interact.response.send_message(f"Olá, {interact.user.name}")
    await interact.response.defer()
    await interact.followup.send("Pronto!")

@bot.tree.command()
async def falar(interact:discord.Interaction, texto:str):
    await interact.response.send_message(texto)

@bot.tree.command()
async def selecionar_membro(interact:discord.Interaction, membro:discord.Member):
    await interact.response.send_message(f"Você selecionou o usuário{membro.mention}")



#key do bot
bot.run("KEYDOBOT")