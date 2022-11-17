import asyncio
import random

import discord
from discord import app_commands
from discord.ext import commands
from Utils import Data, Parole



class wordle(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
        
    @app_commands.command(name = "ciao", description="test")
    async def ciao(self,interaction: discord.Interaction)->None:
        await interaction.response.send_message("Ciao")

    @commands.Cog.listener()
    async def on_ready(self):
        print("Wordle_On")

    def listatest(self, lista):
        azz = ""
        #passo la lista ad una variabile
        for i in lista:
            azz += f"{i['nickname']}: {i['punti']} punti\n"
        print(azz)
        return azz


    @commands.command(name="classifica")
    async def classifica(self,ctx):
        lista = []
        lista = Data.Lista()
        embed = discord.Embed()
        embed.title = "Classifica"
        embed.description = self.listatest(lista)
        await ctx.send(embed=embed)

    @commands.command(name="info")
    async def info(self,ctx):
        embed = discord.Embed(title="Come giocare", description="Guida di Pietroppeter", color=0x00ff00)  # creates embed
        file = discord.File("rules.png", filename="image.png")
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=file, embed=embed)

    # Comando per far partire il gioco
    @commands.command(name="wordle")
    async def wordle(self, ctx):
        user = ctx.author.id
        # Apre il file dizionario e lo mappa trovando una parola a caso tra i tanti.
        with open(r"dict\curated.txt", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))

            # print random string
            indovina = random.choice(words)
            print(indovina)
        # INDOVINA è la parola da trovare

        # arr per salvarsi le parole giuste
        arr = []
        #
        embed = Parole.genera_blocchi()
        mex = await ctx.send(embed=embed)

        # Funzione che ritorna True se parola è valida
        def check(m):
            # print(m)
            # Lo uso qui simile nel return infondo solo per non avere continui log
            if user != m.author.id:
                return False
            if len(m.content) > 5:
                print("Parola con piu di 5 caratteri!")
                return False
            # Controllo se la parola esiste nel dizionario
            if not (Parole.parola_esistente(m.content.lower())):
                print("Non esiste questa parola!")
                return False
            # print(f'ID UTENTE {m.author.id} + id user {user}')
            return m.content is not None and len(m.content) == 5 and user == m.author.id

        # Funzione che aspetta il termine giusto da mettere
        # TODO rindondante, si può sistemare
        try:
        #potrei usare asyncio.timeout, unito alla funzione per cercare se quando arriva il messaggio
            parola = await self.bot.wait_for("message", check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.send("Ci hai messo troppo!")
            return
        await mex.edit(embed=Parole.update_embed(str(parola.content.lower()), 0, arr, indovina))
        if parola.content == indovina:
            await ctx.send("Hai vinto!")
            Data.Aggiorna_punti(ctx.author.id, ctx.author.name, 60)
            return
        try:
            parola = await self.bot.wait_for("message", check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.send("Ci hai messo troppo!")
            return
        await mex.edit(embed=Parole.update_embed(str(parola.content.lower()), 1, arr, indovina))
        if parola.content == indovina:
            await ctx.send("Hai vinto!")
            Data.Aggiorna_punti(ctx.author.id, ctx.author.name, 50)
            return
        try:
            parola = await self.bot.wait_for("message", check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.send("Ci hai messo troppo!")
            return
        await mex.edit(embed=Parole.update_embed(str(parola.content.lower()), 2, arr, indovina))
        if parola.content == indovina:
            Data.Aggiorna_punti(ctx.author.id, ctx.author.name, 40)
            await ctx.send("Hai vinto!")
            return
        try:
            parola = await self.bot.wait_for("message", check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.send("Ci hai messo troppo!")
            return
        await mex.edit(embed=Parole.update_embed(str(parola.content.lower()), 3, arr, indovina))
        if parola.content == indovina:
            Data.Aggiorna_punti(ctx.author.id, ctx.author.name, 30)
            await ctx.send("Hai vinto!")
            return
        try:
            parola = await self.bot.wait_for("message", check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.send("Ci hai messo troppo!")
            return
        await mex.edit(embed=Parole.update_embed(str(parola.content.lower()), 4, arr, indovina))
        if parola.content == indovina:
            await ctx.send("Hai vinto!")
            Data.Aggiorna_punti(ctx.author.id, ctx.author.name, 20)
            return
        try:
            parola = await self.bot.wait_for("message", check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.send("Ci hai messo troppo!")
            return
        await mex.edit(embed=Parole.update_embed(str(parola.content.lower()), 5, arr, indovina))
        if parola.content == indovina:
            await ctx.send("Hai vinto!")
            Data.Aggiorna_punti(ctx.author.id, ctx.author.name, 10)
            return
        else:
            await ctx.send(f'La parola era: "{indovina}"')
            return


async def setup(bot):
    await bot.add_cog(wordle(bot))