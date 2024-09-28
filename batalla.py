import random

class Unidad:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def esta_vivo(self):
        return self.vida > 0

class Arquero(Unidad):
    def __init__(self, nombre, vida, ataque, defensa):
        super().__init__(nombre, vida, ataque, defensa)

class Infanteria(Unidad):
    def __init__(self, nombre, vida, ataque, defensa):
        super().__init__(nombre, vida, ataque, defensa)

class Caballeria(Unidad):
    def __init__(self, nombre, vida, ataque, defensa):
        super().__init__(nombre, vida, ataque, defensa)

#------------------------------------------------------------

class Ejercito:
    def __init__(self, nombre):
        self.nombre = nombre
        self.unidades = []

    def reclutar_unidades(self, unidad):
        self.unidad.append(unidad)
    
    def tiene_unidades(self):
        return any([unidad.esta_vivo() for unidad in self.unidades])

#------------------------------------------------------------

def combat(unidad1, unidad2):
    print(f"{unidad1.nombre} ({unidad1.vida} HP) vs {unidad2.nombre} ({unidad2.vida} HP)")
    daño1 = max(0, unidad1.ataque - unidad2.defensa)
    unidad2.vida -= daño1
    print(f"{unidad1.nombre} hace {daño1} de daño a  {unidad2.nombre}")
    
    if(unidad2.esta_vivo()):
        daño2 = max(0, unidad2.ataque - unidad1.defensa)
        unidad1.vida -= daño2
        print(f"{unidad2.nombre} hace {daño2} de daño a {unidad1.nombre}")
        
        if not unidad1.esta_vivo():
            print(f"{unidad1.nombre} ha muerto")
            
    else:
        print(f"{unidad2.nombre} ha muerto")

def batalla(ejercito1, ejercito2):
    ronda = 1
    while ejercito1.tiene_unidades() and ejercito2.tiene_unidades():
        print(f"Ronda {ronda}")
        unidad1 = random.choice([unidad for unidad in ejercito1.unidades if unidad.esta_vivo()])
        unidad2 = random.choice([unidad for unidad in ejercito2.unidades if unidad.esta_vivo()])
        combat(unidad1, unidad2)
        ronda+=1
    if ejercito1.tiene_unidades():
        print(f"{ejercito1.nombre} ha ganado")
    else:
        print(f"{ejercito2.nombre} ha ganado")

#------------------------------------------------------------

ejercito1 = Ejercito("Ejercito rojo")
ejercito2 = Ejercito("Ejercito azul")

for _ in range(5):
    ejercito1.reclutar_unidades(Arquero("Arquero", 100, 10, 5))
    ejercito1.reclutar_unidades(Infanteria("Infanteria", 100, 15, 10))
    ejercito1.reclutar_unidades(Caballeria("Caballeria", 100, 20, 15))

for _ in range(5):
    ejercito2.reclutar_unidades(Arquero("Arquero", 100, 10, 5))
    ejercito2.reclutar_unidades(Infanteria("Infanteria", 100, 15, 10))
    ejercito2.reclutar_unidades(Caballeria("Caballeria", 100, 20, 15))

batalla(ejercito1, ejercito2)