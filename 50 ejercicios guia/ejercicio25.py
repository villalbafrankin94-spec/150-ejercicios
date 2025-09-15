class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.calificaciones = {} 

    def agregar_calificacion(self, materia, nota):
        self.calificaciones[materia] = nota
        print(f"✅ Calificación agregada a {self.nombre}: {materia} = {nota}")

    def calcular_promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones.values()) / len(self.calificaciones)

    def __str__(self): 
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Grado: {self.grado}"

class SistemaRegistroEstudiantes:
    def __init__(self):
        self.estudiantes = {} 

    def agregar_estudiante(self, nombre, edad, grado):
        if nombre in self.estudiantes:
            print(f"❌ Estudiante {nombre} ya existe.")
            return
        nuevo_estudiante = Estudiante(nombre, edad, grado)
        self.estudiantes[nombre] = nuevo_estudiante
        print(f"✅ Estudiante {nombre} agregado exitosamente.")

    def buscar_estudiante(self, nombre):
        return self.estudiantes.get(nombre) 

    def mostrar_reporte(self):
        print("\n" + "=" * 50)
        print("REPORTE DE ESTUDIANTES")
        print("=" * 50)
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
            return

        for nombre, estudiante in self.estudiantes.items():
            print(f"\n{estudiante}")
            if estudiante.calificaciones:
                print("Calificaciones:")
                for materia, nota in estudiante.calificaciones.items():
                    print(f"  - {materia}: {nota}")
                promedio = estudiante.calcular_promedio()
                print(f"Promedio general: {promedio:.2f}")
            else:
                print("Sin calificaciones registradas")
            print("-" * 30)


sistema = SistemaRegistroEstudiantes()
sistema.agregar_estudiante("Ana García", 16, "10°")
sistema.agregar_estudiante("Carlos López", 15, "9°")

ana = sistema.buscar_estudiante("Ana García")
if ana:
    ana.agregar_calificacion("Matemáticas", 9.2)
    ana.agregar_calificacion("Historia", 8.8)

carlos = sistema.buscar_estudiante("Carlos López")
if carlos:
    carlos.agregar_calificacion("Matemáticas", 7.5)

sistema.mostrar_reporte()