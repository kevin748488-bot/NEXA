import asyncio
import edge_tts
import os

async def hablar(texto):
    print("NEXA:", texto)

    tts = edge_tts.Communicate(texto, "es-MX-DaliaNeural")
    await tts.save("voz.mp3")

    # Windows
    os.system("start voz.mp3")
    # Para Linux/Mac, descomentar:
    # os.system("mpg123 voz.mp3")  # Linux
    # os.system("afplay voz.mp3")  # macOS

async def main():
    print("🤖 NEXA con voz iniciada")

    memoria = {}

    while True:
        user = input("Tú: ").lower()

        if "hola" in user:
            await hablar("Hola, estoy contigo")

        elif "mi nombre es" in user:
            nombre = user.replace("mi nombre es", "").strip()
            memoria["nombre"] = nombre
            await hablar(f"Encantado {nombre}")

        elif "como me llamo" in user:
            await hablar(memoria.get("nombre", "No lo sé todavía"))

        elif "estres" in user:
            await hablar("Respira conmigo... todo va a estar bien")

        elif "audifonos" in user:
            await hablar("Configurando modo de audio optimizado")

        elif "salir" in user:
            await hablar("Hasta luego")
            break

        else:
            await hablar("Estoy aprendiendo aún")

if __name__ == "__main__":
    asyncio.run(main())
