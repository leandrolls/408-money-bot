from discord.ext import commands
import discord

class Talks(commands.Cog):
    """ TALKS WITH USER """

    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='ajudac', help="O 408 Money Bot mostra todos os comandos")
    async def ajudac(self, ctx):
        embed_image = discord.Embed(title="PRECISANDO DE AJUDA? ", color=0xFFFFFF)
        embed_image.add_field(name="COMANDOS:", value="""
        !ajudac = Para exibir essa mensagem com os comandos e sua funções.
        !bitusa = Para exibir o valor do Bitcon em dólares.
        !bitbr = Para exibir o valor do Bitcon em real.
        !dolar = Para exibir o valor do dolar.
        !euro = Para exibir o valor do euro.
        """, inline=False)
        await ctx.send(embed=embed_image)

def setup(bot):
    bot.add_cog(Talks(bot))