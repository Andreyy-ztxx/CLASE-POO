class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau guau!")
    def felicidadperrx(self):
        print("===========================================") 
        print(f"Se acaricio a {self.nombre}")
        print(f"{self.nombre} tomo awita y comio")
        print(f"La mascota {self.nombre} es feliz")
        print("===========================================") 
        
# --- Programa principal ---
if __name__ == "__main__":
    print("=== Registro de un Perro ===")
    nombre_perro = input("Ingrese el nombre del perro: ")
    nombre_perro = nombre_perro.title()
    edad_perro = input("Ingrese la edad del perro: ")
    perro = Perro(nombre_perro, edad_perro)

    print("\n--- Acciones de los animales ---")
    print("===== Perrito ======")
    perro.felicidadperrx()
