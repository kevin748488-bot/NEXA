import asyncio
from bleak import BleakClient, BleakScanner

class ConexionBluetooth:
    def __init__(self):
        self.dispositivos = []
        self.cliente = None

    async def escanear_dispositivos(self):
        print("🔍 Buscando dispositivos Bluetooth...")

        devices = await BleakScanner.discover()

        self.dispositivos = []

        for d in devices:
            print(f"Encontrado: {d.name} - {d.address}")
            self.dispositivos.append({
                "nombre": d.name,
                "direccion": d.address
            })

        return self.dispositivos

    async def conectar(self, address):
        print(f"🔗 Conectando a {address}...")

        self.cliente = BleakClient(address)

        conectado = await self.cliente.connect()

        print("Estado conexión:", conectado)

        return conectado

    async def obtener_servicios(self):
        if not self.cliente or not await self.cliente.is_connected():
            print("❌ No hay dispositivo conectado")
            return None

        print("📡 Obteniendo servicios Bluetooth...")

        servicios = await self.cliente.get_services()

        for servicio in servicios:
            print("🔧 Servicio:", servicio)

        return servicios

    async def desconectar(self):
        if self.cliente:
            await self.cliente.disconnect()
            print("👋 Dispositivo desconectado")
