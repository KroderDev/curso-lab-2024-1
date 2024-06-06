import random

class MascotaVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = 50  # 0 significa lleno, 100 significa muy hambriento
        self.energia = 50  # 0 significa agotado, 100 significa lleno de energía
        self.felicidad = 50  # 0 significa triste, 100 significa muy feliz
        self.salud = 100  # 0 significa enfermo, 100 significa muy saludable
        self.edad = 0  # Edad en días
        self.etapa = "Bebé"  # Etapas: Bebé, Niño, Adulto

    def alimentar(self):
        if self.hambre > 10:
            self.hambre -= 10
            self.felicidad += 5
            print(f"{self.nombre} ha sido alimentado.")
        else:
            print(f"{self.nombre} no tiene hambre.")
    
    def jugar(self):
        if self.energia > 10:
            self.energia -= 10
            self.felicidad += 10
            print(f"{self.nombre} está jugando.")
        else:
            print(f"{self.nombre} está muy cansado para jugar.")
    
    def descansar(self):
        self.energia += 20
        self.hambre += 10
        print(f"{self.nombre} está descansando.")

    def curar(self):
        if self.salud < 100:
            self.salud += 20
            print(f"{self.nombre} ha sido curado.")
        else:
            print(f"{self.nombre} está en perfectas condiciones.")

    def limpiar(self):
        self.felicidad += 5
        print(f"{self.nombre} ha sido limpiado y está más feliz.")
    
    def estado(self):
        estado = (f"Estado de {self.nombre}:\n"
                  f"Hambre: {self.hambre}\n"
                  f"Energía: {self.energia}\n"
                  f"Felicidad: {self.felicidad}\n"
                  f"Salud: {self.salud}\n"
                  f"Edad: {self.edad} días\n"
                  f"Etapa: {self.etapa}\n")
        return estado
        
    def actualizar_estado(self):
        if self.hambre < 100:
            self.hambre += 1
        if self.energia > 0:
            self.energia -= 1
        if self.felicidad > 0:
            self.felicidad -= 1
        if random.random() < 0.05:
            self.salud -= 10  # 5% de probabilidad de perder salud
        self.edad += 1

        # Actualizar etapa de la vida
        if self.edad > 10 and self.edad <= 20:
            self.etapa = "Niño"
        elif self.edad > 20:
            self.etapa = "Adulto"
