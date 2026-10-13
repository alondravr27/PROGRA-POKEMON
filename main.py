from clases.pokemon import Pokemon

pokemons = []


def capturar_pokemon():
    print("\n CAPTURAR POKEMON")

    nombre = input("Nombre: ").strip()
    tipo = input("Tipo: ").strip()

    if not nombre or not tipo:
        print("El nombre y el tipo son obligatorios.")
        return

    try:
        ataque = int(input("Ataque inicial: "))
        defensa = int(input("Defensa inicial: "))
        salud = int(input("Salud inicial: "))

        if ataque < 0 or defensa < 0 or salud <= 0:
            print("Ataque y defensa deben ser >= 0, y salud > 0.")
            return

        pokemon = Pokemon(nombre, tipo, ataque, defensa, salud)
        pokemons.append(pokemon)

    except ValueError:
        print("Error: introduce numeros enteros validos.")


def seleccionar_pokemon():
    if not pokemons:
        print("\nNo hay Pokemon capturados.")
        return None

    print("\n LISTA DE POKEMON")

    for i, pokemon in enumerate(pokemons, start=1):
        print(f"{i}. {pokemon.nombre} (Nivel {pokemon.nivel})")

    try:
        opcion = int(input("Selecciona un Pokemon: "))

        if 1 <= opcion <= len(pokemons):
            return pokemons[opcion - 1]

        print("Opcion fuera de rango.")

    except ValueError:
        print("Debes introducir un numero entero.")

    return None


def entrenar_pokemon():
    pokemon = seleccionar_pokemon()

    if pokemon is None:
        return

    print("\n1. Entrenamiento automatico")
    print("2. Mejorar solo el ataque")
    print("3. Mejorar ataque y defensa")
    print("4. Personalizar las tres estadisticas")

    try:
        opcion = int(input("Elige una opcion: "))

        if opcion == 1:
            pokemon.entrenar()

        elif opcion == 2:
            ataque = int(input("Puntos de ataque a mejorar: "))
            pokemon.entrenar(ataque)

        elif opcion == 3:
            ataque = int(input("Puntos de ataque a mejorar: "))
            defensa = int(input("Puntos de defensa a mejorar: "))
            pokemon.entrenar(ataque, defensa)

        elif opcion == 4:
            ataque = int(input("Mejora de ataque: "))
            defensa = int(input("Mejora de defensa: "))
            salud = int(input("Mejora de salud: "))
            pokemon.entrenar(ataque, defensa, salud)

        else:
            print("Opción no valida.")

    except ValueError as error:
        print(f"Entrada inválida: {error}")


def mostrar_todos():
    if not pokemons:
        print("\nNo hay Pokemon para mostrar.")
        return

    for pokemon in pokemons:
        pokemon.mostrar_info()


def combatir():
    print("\n COMBATE POKEMON")

    if len(pokemons) < 2:
        print("Necesitas al menos dos Pokemon para combatir.")
        return

    print("Selecciona al Pokemon atacante:")
    atacante = seleccionar_pokemon()

    if atacante is None:
        return

    print("Selecciona al Pokemon objetivo:")
    objetivo = seleccionar_pokemon()

    if objetivo is None:
        return

    if atacante is objetivo:
        print("Un Pokemon no puede atacarse a si mismo.")
        return

    atacante.atacar(objetivo)


def liberar_pokemon():
    pokemon = seleccionar_pokemon()

    if pokemon is None:
        return

    nombre = pokemon.nombre
    indice = pokemons.index(pokemon)

    del pokemons[indice]

    print(f"{nombre} ha sido liberado de tu equipo.")


def menu():
    while True:
        print("\n" + "=" * 35)
        print("POKEMON SIMULATOR")
        print("=" * 35)
        print("1. Capturar Pokemon")
        print("2. Entrenar Pokemon")
        print("3. Ver información de todos")
        print("4. Calcular Pokemon creados")
        print("5. Liberar un Pokémon")
        print("6. Combatir")
        print("0. Salir")
        print("=" * 35)

        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            capturar_pokemon()

        elif opcion == "2":
            entrenar_pokemon()

        elif opcion == "3":
            mostrar_todos()

        elif opcion == "4":
            Pokemon.total_pokemons()

        elif opcion == "5":
            liberar_pokemon()

        elif opcion == "6":
            combatir()

        elif opcion == "0":
            print("¡Gracias por jugar Pokémon Simulator! 👋")
            break

        else:
            print("Opcion no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()