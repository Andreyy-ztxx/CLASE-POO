

class Encuesta:
    def __init__(self, preguntas, opciones_preferencia):
        self.preguntas = preguntas                     
        self.opciones_preferencia = opciones_preferencia  
        self.respuestas = []                            

    def agregar_respuesta(self, respuestas_estudiante):
        self.respuestas.append(respuestas_estudiante)

    def mostrar_resultados(self):

        print("\n=== RESULTADOS POR PREGUNTA ===")
        for i in range(len(self.preguntas)):
            print(f"\nPregunta {i+1}: {self.preguntas[i]}")
            for fila in self.respuestas:
                print("-", fila[i])

        
        print("\n=== RESUMEN DE PREFERENCIAS (Pregunta 1) ===")
        conteo = {"Web": 0, "Datos": 0, "Juegos": 0}
        for fila in self.respuestas:
            op = fila[0]
            if op in conteo:
                conteo[op] += 1
        print("Web  :", conteo["Web"], "voto(s)")
        print("Datos:", conteo["Datos"], "voto(s)")
        print("Juegos:", conteo["Juegos"], "voto(s)")
        print("\nTotal de estudiantes:", len(self.respuestas))


preguntas = [
    "¿Qué tema prefieres para el proyecto? (Web/Datos/Juegos)",
    "¿Sabes trabajar en equipo? (si/no)",
    "¿Conoces alguna librería de Python?"
]
opciones_preferencia = ["Web", "Datos", "Juegos"]

encuesta = Encuesta(preguntas, opciones_preferencia)

print("Bienvenido/a. Responderán 10 estudiantes.\n")


for i in range(1, 11):
    print(f"\n--- Estudiante {i} ---")

   
    while True:
        r1 = input("1) " + preguntas[0] + " ").strip().lower()
        if r1 in ("web", "datos", "juegos"):
            r1 = r1.capitalize()  
            break
        print("Escribe: Web, Datos o Juegos.")

    while True:
        r2 = input("2) " + preguntas[1] + " ").strip().lower()
        if r2 in ("si", "no"):
            break
        print("Responde 'si' o 'no'.")

    r3 = input("3) " + preguntas[2] + " ").strip()

    encuesta.agregar_respuesta([r1, r2, r3])

encuesta.mostrar_resultados()