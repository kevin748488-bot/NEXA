print("NEXA AI iniciada")

while True:
    user = input("Usuario: ").lower()

    if "hola" in user:
        print("NEXA: Hola 👋 estoy contigo")
    elif "audifonos" in user:
        print("NEXA: Configurando modo audio optimizado 🎧")
    elif "estres" in user:
        print("NEXA: Activando modo calma 🧘")
    elif "salir" in user:
        print("NEXA: Hasta luego 👋")
        break
    else:
        print("NEXA: Entendido.")
