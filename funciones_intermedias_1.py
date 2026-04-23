matriz = [[10, 15, 20], [3, 7, 14]]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
coordenadas = [{"latitud": 8.2588997, "longitud": -84.9399704}]


matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431

print("Ejercicio 1:")
print("matriz:", matriz)
print("cantantes:", cantantes)
print("ciudades:", ciudades)
print("coordenadas:", coordenadas)


def iterarDiccionario(lista):
    for elemento in lista:
        contenido = ", ".join(f"{clave} - {valor}" for clave, valor in elemento.items())
        print(contenido)


def iterarDiccionario2(llave, lista):
    for elemento in lista:
        if llave in elemento:
            print(elemento[llave])
        else:
            print(f"Clave '{llave}' no encontrada en el diccionario")


def imprimirInformacion(diccionario):
    for clave, valores in diccionario.items():
        print(f"{len(valores)} {clave.upper()}")
        for valor in valores:
            print(valor)
        print()



cantantes = [
    {"nombre": "Milo J", "pais": "Argentina"},
    {"nombre": "Cristian Castro", "pais": "México"},
    {"nombre": "Ado", "pais": "Japón"},
    {"nombre": "Marc Anthony", "pais": "Estados Unidos"}
]

print("\nEjercicio 2:")
iterarDiccionario(cantantes)

print("\nEjercicio 3:")
print("Nombres:")
iterarDiccionario2("nombre", cantantes)
print("\nPaises:")
iterarDiccionario2("pais", cantantes)

Mundo = {
    "ciudades": ["Ciudad de México", "Tokio", "Morón", "New York", "Madrid"],
    "comidas": ["Tacos al pastor", "ramen", "Asado", "Bagel", "Callos a la madrileña"]
}

print("Ejercicio 4:")
imprimirInformacion(Mundo)
