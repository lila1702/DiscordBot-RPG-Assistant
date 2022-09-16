import database
import discord

class Fichas_Old_Dragon(discord.Client):
    
    async def on_ready(self):
        print(f"[{self.user.name}: {self.user.id}] está na área!")

    async def on_message(self, message):
        if(message.author.id == self.user.id):
            return

        if(message.content.startswith("!ficha")):
            await message.channel.send("Printar ficha futuramente")
            print(message.guild.name)
            print(message.guild.id)

"""Main"""
token_arquivo = open("C:/Users/Lila/Documents/Projetos/Privados/my_token.txt", 'r')
token = token_arquivo.read()
token_arquivo.close()

discord_client = Fichas_Old_Dragon()
discord_client.run(token)