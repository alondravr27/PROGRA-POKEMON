class Pokemon:
    contador = 0

    def __init__(self, nombre: str, tipo: str, ataque: int, defensa: int, salud: int):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = 1
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        self.salud_maxima = salud

        Pokemon.contador += 1

        print(
            f"¡{self.nombre} ha sido capturado! "
            f"Es un Pokemon de tipo {self.tipo}."
        )

    def __del__(self):
        nombre = getattr(self, "nombre", "Pokemon")
        print(f"{nombre} ha sido liberado ✨")

    def entrenar(self, *args):
        self.nivel += 1

        if not args:
            mejoras = (2, 2, 10)
        else:
            mejoras = list(args[:3])

            mejoras += [0] * (3 - len(mejoras))

        if any(valor < 0 for valor in mejoras):
            raise ValueError("Las mejoras no pueden ser negativas.")

        self.ataque += mejoras[0]
        self.defensa += mejoras[1]
        self.salud += mejoras[2]
        self.salud_maxima += mejoras[2]

        print(f"\n ¡{self.nombre} ha entrenado!")
        print(f"Nuevo nivel: {self.nivel}")
        print(
            f"Mejoras: ataque +{mejoras[0]}, "
            f"defensa +{mejoras[1]}, salud +{mejoras[2]}"
        )

    def mostrar_info(self):
        print("\n" + "=" * 30)
        print(f"Pokémon: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Nivel: {self.nivel}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Salud: {self.salud}/{self.salud_maxima}")
        print("=" * 30)

    def atacar(self, objetivo):
        if self.salud <= 0:
            print(f"{self.nombre} no puede atacar: está debilitado.")
            return

        if objetivo.salud <= 0:
            print(f"{objetivo.nombre} ya está debilitado.")
            return

        danio = max(1, self.ataque - objetivo.defensa)

        objetivo.salud = max(0, objetivo.salud - danio)

        print(
            f"\n{self.nombre} ataca a {objetivo.nombre} "
            f"e inflige {danio} puntos de daño."
        )
        print(
            f"Salud restante de {objetivo.nombre}: "
            f"{objetivo.salud}/{objetivo.salud_maxima}"
        )

        if objetivo.salud == 0:
            print(f"¡{objetivo.nombre} ha sido debilitado!")

    @classmethod
    def total_pokemons(cls):
        print(f"\nTotal de Pokemon creados: {cls.contador}")
        return cls.contador