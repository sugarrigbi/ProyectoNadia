import asyncio
import discord
import aiohttp

WEBHOOK_URL = "INSERTAR LINK" 
AVATAR_NOPAL = "INSERTAR LINK"
NOMBRE_BOT = "Moon-Bot"

async def Enviar_Embed():
    while True:
        Texto = discord.Embed(
            title=input("Titulo del embed: "),
            description=input("Descripcion: ").replace("\\n", "\n"),
            color=discord.Color(0x4509B3)
        )
        Imagen = input("Imagen (Enter para omitir): ")
        if Imagen != "":
            Texto.set_image(url=Imagen)

        async with aiohttp.ClientSession() as session:
            Webhook = discord.Webhook.from_url(WEBHOOK_URL, session=session)
            await Webhook.send(embed=Texto, username=NOMBRE_BOT, avatar_url=AVATAR_NOPAL, allowed_mentions=discord.AllowedMentions(everyone=True))
            print("--Embed enviado correctamente--")

        Respuesta = input("Desea enviar otro Embed? (y/n): ")
        if Respuesta != "y":
            break

async def Enviar_Mensaje():
    while True:
        Mensaje = input("Escribe el mensaje a enviar: ")

        async with aiohttp.ClientSession() as session:
            Webhook = discord.Webhook.from_url(WEBHOOK_URL, session=session)
            await Webhook.send(content=Mensaje, username=NOMBRE_BOT, avatar_url=AVATAR_NOPAL, allowed_mentions=discord.AllowedMentions(everyone=True))
            print("--Mensaje enviado correctamente--")

        Respuesta = input("Desea enviar otro Mensaje? (y/n): ")
        if Respuesta != "y":
            break

async def Enviar_Hilo():
    while True:
        Titulo = input("Titulo del hilo: ")
        Descripcion = input("Descripcion: ").replace("\\n", "\n")

        async with aiohttp.ClientSession() as session:
            Webhook = discord.Webhook.from_url(WEBHOOK_URL, session=session)
            await Webhook.send(thread_name=Titulo,content=Descripcion,username=NOMBRE_BOT, avatar_url=AVATAR_NOPAL, allowed_mentions=discord.AllowedMentions(everyone=True))
            print("--Hilo enviado correctamente--")

        Respuesta = input("Desea enviar otro Hilo? (y/n): ")
        if Respuesta != "y":
            break            

async def Main():
    while True:
        try:
            print("MENU EMBED")
            print("1.) Enviar Embed")
            print("2.) Enviar Mensaje")
            print("3.) Enviar Hilo")
            print("9.) Salir")
            Res = int(input("Elije una opcion: "))
            if Res == 1:
                await Enviar_Embed()
            elif Res == 2:
                await Enviar_Mensaje()
            elif Res == 3:
                await Enviar_Hilo()        
            elif Res == 9:
                break     
            else:
                print("Respuesta incorrecta")
        except ValueError:
            print("Respuesta incorrecta")

asyncio.run(Main())