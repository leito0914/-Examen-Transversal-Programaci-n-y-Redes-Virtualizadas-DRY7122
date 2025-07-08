from geopy.distance import geodesic

ciudades = {
    "santiago": (-33.4489, -70.6693),
    "valparaiso": (-33.0472, -71.6127),
    "buenos aires": (-34.6037, -58.3816),
    "mendoza": (-32.8895, -68.8458),
    "cordoba": (-31.4201, -64.1888)
}

velocidades = {
    "auto": 80,
    "bus": 60,
    "avion": 800
}

while True:
    print("\n--- Calculadora de Viaje Chile - Argentina ---")
    origen = input("Ingrese Ciudad de Origen (o 's' para salir): ").lower()
    if origen == 's':
        break
    destino = input("Ingrese Ciudad de Destino (o 's' para salir): ").lower()
    if destino == 's':
        break

    if origen not in ciudades or destino not in ciudades:
        print("Una o ambas ciudades no están registradas. Intente nuevamente.")
        continue

    coord_origen = ciudades[origen]
    coord_destino = ciudades[destino]

    distancia_km = geodesic(coord_origen, coord_destino).kilometers
    distancia_millas = distancia_km * 0.621371

    print(f"\nDistancia entre {origen.title()} y {destino.title()}:")
    print(f"- {distancia_km:.2f} km")
    print(f"- {distancia_millas:.2f} millas")

    medio = input("Seleccione medio de transporte (auto, bus, avion): ").lower()
    if medio not in velocidades:
        print("Medio no reconocido. Se asume auto.")
        medio = "auto"

    duracion_horas = distancia_km / velocidades[medio]
    print(f"Duración aproximada en {medio}: {duracion_horas:.2f} horas.")

    print(f"\nNarrativa del viaje: Desde {origen.title()} partirás rumbo a {destino.title()}, "
          f"recorriendo {distancia_km:.2f} km en aproximadamente {duracion_horas:.2f} horas en {medio}.\n")
