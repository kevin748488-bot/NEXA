import pyttsx3

# Inicializar motor de voz
engine = pyttsx3.init()

def hablar(texto):
    print("NEXA:", texto)
    engine.say(texto)
    engine.runAndWait()

print("🤖 NEXA con voz iniciada")

memoria = {}

while True:
    user = input("Tú: ").lower()

    if "hola" in user:
        hablar("Hola, estoy contigo")

    elif "mi nombre es" in user:
        nombre = user.replace("mi nombre es", "").strip()
        memoria["nombre"] = nombre
        hablar(f"Encantado {nombre}")

    elif "como me llamo" in user:
        hablar(memoria.get("nombre", "No lo sé todavía"))

    elif "estres" in user:
        hablar("Respira conmigo... todo va a estar bien")

    elif "audifonos" in user:
        hablar("Configurando modo de audio optimizado")

    elif "salir" in user:
        hablar("Hasta luego")
        break

    else:
        hablar("Estoy aprendiendo aún")
