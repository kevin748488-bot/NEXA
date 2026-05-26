print("🤖 NEXA AI iniciada")

memoria = {}

while True:
    user = input("Tú: ").lower()

    if "mi nombre es" in user:
        nombre = user.replace("mi nombre es", "").strip()
        memoria["nombre"] = nombre
        print(f"NEXA: Encantado {nombre} 👋")

    elif "como me llamo" in user:
        print("NEXA:", memoria.get("nombre", "No lo sé todavía 😅"))

    elif "hola" in user:
        print("NEXA: Hola 👋 estoy contigo")

    elif "estres" in user:
        print("NEXA: Activando modo calma 🧘 respira conmigo...")

    elif "audifonos" in user:
        print("NEXA: Ajustando perfil de audio 🎧")

    elif "salir" in user:
        print("NEXA: Hasta luego 👋")
        break

    else:
        print("NEXA: Estoy aprendiendo aún 🤖")
