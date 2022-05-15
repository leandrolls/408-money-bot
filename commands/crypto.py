from discord.ext import commands
import requests

class Cryptos(commands.Cog):
    """ TREAT THE ERRORS """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='bitbr',help="Retorna o valor do bitcoin em real (R$) ")
    async def bitcoinbr(self,ctx):
        try:
            response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol=BTCBRL")

            data = response.json()
            price = data.get("price")
            if price:
                await ctx.send(f"O valor do Bitcoin é de R${price}")
            else:
                await ctx.send(f"Inválido. Escreva !ajuda para exibir os comandos")
        except:
            await ctx.send("Ops.. deu um erro")

    @commands.command(name='bitusa', help='Retorna o valor do bitocin em dólares ($) ')
    async def bitcoinusa(self,ctx):
        try:
            response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
            data = response.json()
            price = data.get("price")
            if price:
                    await ctx.send(f"O valor do Bitcoin é de ${price}")
            else:
                await ctx.send(f"Inválido. Escreva !ajuda para exibir os comandos")
        except:
            await ctx.send("Ops.. deu um erro")

    @commands.command(name='dolar', help="Retorna o valor do dolár no momento em que foi dado o comando")
    async def dolar(self, ctx):
        try:
            response = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
            data = requests.get(response)
            cotacao = data.json()

            cotacaoDolar = cotacao["USDBRL"]["bid"]
            if cotacao:
                await ctx.send(f"O valor do Dólar($) é de R${cotacaoDolar}")
            else:
                await ctx.send(f"Inválido. Escreva !ajuda para exibir os comandos")
        except:
            await ctx.send("Ops.. deu um erro")

    @commands.command(name='euro', help='Retorna o valor do Euro no momento em que foi dado o comando')
    async def euro(self, ctx):
        try:
            response = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
            data = requests.get(response)
            cotacao = data.json()

            cotacaoEuro = cotacao["EURBRL"]["bid"]
            if cotacao:
                await ctx.send(f"O valor do Euro (€) é de R${cotacaoEuro}")
            else:
                await ctx.send(f"Inválido. Escreva !ajuda para exibir os comandos")
        except:
            await ctx.send("Opa, deu um erro")

    # @commands.command(name='dolardata', help='Retorna o valor do dolar em um periodo específico')
    #     # async def dolardate(self, ctx,begin, end):
    #     #     beginrequest =
    #     #     endrequest =
    #     #     try:
    #     #         response = f"https://economia.awesomeapi.com.br/USD-BRL/10?start_date={beginrequest}&end_date={endrequest}"
    #     #         data = requests.get(response)
    #     #         cotacao = data.json()
    #     #
    #     #         cotacaoEspec = cotacao["USDBRL"]["bid"]
    #     #         if  cotacao:
    #     #             await ctx.send(f"O valor do dolar no periodo de {begin} até {end} é de {cotacaoEspec})
    #     #         else:
    #                     await ctx.send(f"Inválido. Escreva !ajuda para exibir os comandos")
    #     #     except:
    #     #         ctx.send("Ops, deu um erro")

    # @commands.command(name='eurodata', help='Retorna o valor do euro em um periodo específico')
    #     # async def eurodate(self, ctx,begin, end):
    #     #     beginrequest =
    #     #     endrequest =
    #     #     try:
    #     #         response = f"https://economia.awesomeapi.com.br/EUR-BRL/10?start_date={beginrequest}&end_date={endrequest}"
    #     #         data = requests.get(response)
    #     #         cotacao = data.json()
    #     #
    #     #         cotacaoEspec = cotacao["EURBRL"]["bid"]
    #     #         if  cotacao:
    #     #             await ctx.send(f"O valor do euro no periodo de {begin} até {end} é de {cotacaoEspec})
    #     #         else:
    #                     await ctx.send(f"Inválido. Escreva !ajuda para exibir os comandos")
    #     #     except:
    #     #         ctx.send("Ops, deu um erro")

    # @commands.command(name='bitdata', help='Retorna o valor do bit em um periodo específico')
    #     # async def bitdata(self, ctx,begin, end):
    #     #     beginrequest =
    #     #     endrequest =
    #     #     try:
    #     #         response = f"https://economia.awesomeapi.com.br/BTC-BRL/10?start_date={beginrequest}&end_date={endrequest}"
    #     #         data = requests.get(response)
    #     #         cotacao = data.json()
    #     #
    #     #         cotacaoEspec = cotacao["BTCBRL"]["bid"]
    #     #         if  cotacao:
    #     #             await ctx.send(f"O valor do Bitcoin no periodo de {begin} até {end} é de {cotacaoEspec})
    #     #         else:
    #                     await ctx.send(f"Inválido. Escreva !ajuda para exibir os comandos")
    #     #     except:
    #     #         ctx.send("Ops, deu um erro")

def setup(bot):
    bot.add_cog(Cryptos(bot))