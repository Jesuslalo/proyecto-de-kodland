import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
CHANNEL_ID = 1150071144649601144

# Lista de URLs de gifs
gif_urls = [
    "https://tenor.com/qnlvAHuNqv8.gif",
    "https://tenor.com/bUXo8.gif",
    "https://tenor.com/bGmwM.gif",
    # Añade más URLs según sea necesario
]

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    # Saludo al iniciar el bot
    await bot.change_presence(activity=discord.Game(name="cuidar el medio ambiente"))

    # Añade un try-except para manejar posibles errores al obtener el canal
    try:
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            await channel.send("¡Hii! En qué te puedo ayudar hoy. Utiliza `/ayuda` para ver los comandos disponibles.")
        else:
            print(f"No se encontró un canal con el ID {CHANNEL_ID}.")
    except Exception as e:
        print(f"Error al enviar el mensaje de bienvenida: {e}")

#class EcoBot(commands.Cog):
   # def __init__(self, bot):
      #  self.bot = bot

@bot.command(name='leer_imagen')
async def read_image(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            if attachment.content_type.startswith('image'):
                degradation_time = random.choice(["Más de 1000 años", "2 a 5 meses", "Indefinido (no se degrada)"])
                await ctx.send(f"Imagen recibida: {attachment.url}\nEste objeto se degrada en aproximadamente {degradation_time}.")
                return
        await ctx.send("Por favor, adjunta una imagen válida (formatos: PNG, JPG)")
    else:
        await ctx.send("Por favor, adjunta una imagen válida (formatos: PNG, JPG)")

@bot.command(name='analizar_imagen')
async def analyze_image(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            if attachment.content_type.startswith('image'):
                # Simulación de un resultado aleatorio (ecológico o no ecológico)
                is_eco_friendly = random.choice([True, False])

                if is_eco_friendly:
                    await ctx.send(f"¡Esta imagen es ecológica y da vida! 🌱")
                else:
                    await ctx.send(f"Esta imagen no parece ser ecológica. 😢")
                return

        await ctx.send("Por favor, adjunta una imagen válida (formatos: PNG, JPG)")
    else:
        await ctx.send("Por favor, adjunta una imagen válida (formatos: PNG, JPG)")

@bot.command(name='ayuda')
async def show_help(ctx):
    help_message = """
    **Comandos disponibles:**
    - `/analizar_imagen`: Analiza si una imagen es ecológica o no.
    - `/leer_imagen`: Simula la degradación de un objeto de una imagen.
    - `/agricultura_sostenible`: Descubre la agricultura sostenible y su impacto positivo.
    - `/conservacion_agua`: Aprende sobre la conservación del agua y cómo contribuir.
    - `/reducir_residuos`: Obtén consejos sobre cómo reducir residuos y ser más sostenible.
    - `/huella_carbono`: Calcula tu huella de carbono.
    - `/reciclar`: Aprende sobre la importancia del reciclaje.
    - `/energia_renovable`: Descubre más sobre la energía renovable.
    - `/comida_local`: Apoya los alimentos locales y la sostenibilidad agrícola.
    - `/transporte_sostenible`: Explora opciones de transporte sostenible.
    - `/plantar`: Contribuye al medio ambiente plantando un árbol.
    """
    await ctx.send(help_message)

@bot.command(name='agricultura_sostenible')
async def sustainable_agriculture_info(ctx):
    agriculture_gif = "https://tenor.com/hgj8tW9x45S.gif"
    message = (
        "🌾 ¡Descubre la agricultura sostenible! 🚜\n\n"
        "La agricultura sostenible utiliza prácticas que cuidan el medio ambiente, mantienen la salud del suelo "
        "y promueven la biodiversidad. Conoce más sobre cómo la agricultura puede ser amigable con el planeta. 🌱🌾\n\n"
        f"¡Aprende más sobre la agricultura sostenible! {agriculture_gif}"
    )
    await ctx.send(message)

@bot.command(name='conservacion_agua')
async def water_conservation_info(ctx):
    water_gif = "https://tenor.com/b14ss.gif"
    message = (
        "💧 ¡Aprende sobre la conservación del agua! 🚿\n\n"
        "El agua es un recurso valioso, y su conservación es crucial. Descubre consejos prácticos para reducir el consumo de agua "
        "en tu hogar y contribuir a la preservación de este recurso vital. 💦🌎\n\n"
        f"¡Conoce más sobre la conservación del agua! {water_gif}"
    )
    await ctx.send(message)

@bot.command(name='reducir_residuos')
async def reduce_waste_tips(ctx):
    waste_gif = "https://tenor.com/bPGmX.gif"
    message = (
        "♻️ ¡Descubre cómo reducir residuos! 🗑️\n\n"
        "Pequeños cambios en tus hábitos diarios pueden marcar la diferencia. Aprende consejos sobre cómo reducir, reutilizar y reciclar, "
        "y contribuir así a la reducción de residuos y al bienestar del planeta. 🌍💚\n\n"
        f"¡Obtén más consejos sobre la reducción de residuos! {waste_gif}"
    )
    await ctx.send(message)

@bot.command(name='huella_carbono')
async def calculate_carbon_footprint(ctx):
    carbon_footprint_gif = "https://tenor.com/b1G15.gif"
    message = (
        "🌍 ¡Vamos a calcular tu huella de carbono! 🌿\n\n"
        "Responde a algunas preguntas sobre tus hábitos diarios para conocer tu impacto ambiental. "
        "Cada pequeño cambio cuenta para reducir nuestra huella de carbono y proteger el planeta. ♻️\n\n"
        f"¡Comencemos! {carbon_footprint_gif}"
    )
    await ctx.send(message)

@bot.command(name='reciclar')
async def recycle_info(ctx):
    recycle_gif = "https://tenor.com/bDSpA.gif"
    message = (
        "♻️ El reciclaje es fundamental para conservar nuestro planeta. "
        "Cuando reciclamos, reducimos la cantidad de residuos y ayudamos a preservar los recursos naturales. ♻️\n\n"
        f"¡Anímate a reciclar! {recycle_gif}"
    )
    await ctx.send(message)

@bot.command(name='energia_renovable')
async def renewable_energy_info(ctx):
    energy_gif = "https://tenor.com/bRWMi.gif"
    message = (
        "🌞 La energía renovable es clave para un futuro sostenible. "
        "Fuentes como la solar, eólica y hidroeléctrica son amigables con el medio ambiente. 🌍💡\n\n"
        f"¡Descubre más sobre la energía renovable! {energy_gif}"
    )
    await ctx.send(message)

@bot.command(name='comida_local')
async def promote_local_food(ctx):
    local_food_gif = "https://tenor.com/bWML9.gif"
    message = (
        "🍏 ¡Apoya los alimentos locales! 🌽\n\n"
        "Comer alimentos locales beneficia a la comunidad, reduce la huella de carbono asociada con el transporte de alimentos "
        "y promueve la sostenibilidad agrícola. Descubre los productos locales y disfruta de sus beneficios. 🌱🥕\n\n"
        f"¡Descubre más sobre la comida local! {local_food_gif}"
    )
    await ctx.send(message)

@bot.command(name='transporte_sostenible')
async def sustainable_transport_info(ctx):
    transport_gif = "https://tenor.com/bRUsi.gif"
    message = (
        "🚲 ¡Explora opciones de transporte sostenible! 🚍\n\n"
        "Optar por formas de transporte ecológicas, como andar en bicicleta, usar transporte público o vehículos eléctricos, "
        "contribuye a reducir las emisiones de carbono y mejorar la calidad del aire. 🌿🌎\n\n"
        f"¡Descubre más sobre el transporte sostenible! {transport_gif}"
    )
    await ctx.send(message)

@bot.command(name='plantar')
async def plant_tree(ctx):
    tree_gif = "https://tenor.com/xXB5.gif"
    message = (
        f"🌳 ¡Felicidades! Has plantado un árbol. 🌳\n\n"
        "Cada árbol que plantamos es un regalo para el futuro. "
        "Estás contribuyendo a combatir la deforestación, "
        "promoviendo la biodiversidad y proporcionando hábitats para la vida silvestre. 🌿🦉🌺\n\n"
        f"¡Gracias por ser parte de la solución! {tree_gif}"
    )
    await ctx.send(message)

#bot.add_cog(EcoBot(bot))
bot.run("MTIxMzUwMTI5NDIyOTA2NTc1OQ.GDfjZt.4RYUQN77lMrqmyI0QGIG_kxRj_hEMdtGbq3du8")