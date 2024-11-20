import datetime
import statistics

# Lista para almacenar los experimentos
experimentos = []

# Definimos una clase para los experimentos
class Experimento:
    def __init__(self, nombre, fecha, tipo, resultados):
        self.nombre = nombre
        self.fecha = fecha
        self.tipo = tipo
        self.resultados = resultados

    def __str__(self):
        return f"Nombre: {self.nombre}, Fecha: {self.fecha}, Tipo: {self.tipo}, Resultados: {self.resultados}"

def agregar_experimentos():
    """Permite agregar un nuevo experimento."""
    nombre = input("Introduce el nombre del experimento: ")
    fecha = input("Introduce la fecha del experimento (YYYY-MM-DD): ")
    tipo = input("Introduce el tipo de experimento: ")
    resultados_str = input("Introduce los resultados numéricos (separados por comas): ")
    resultados = list(map(float, resultados_str.split(',')))

    # Crear un nuevo experimento
    experimento = Experimento(nombre, fecha, tipo, resultados)
    experimentos.append(experimento)
    print("Experimento agregado con éxito.")

def visualizar_experimentos():
    """Muestra todos los experimentos almacenados."""
    if not experimentos:
        print("No hay experimentos registrados.")
    else:
        for exp in experimentos:
            print(exp)

def gestionar_experimentos():
    """Permite eliminar un experimento por nombre."""
    nombre = input("Introduce el nombre del experimento a eliminar: ")
    global experimentos
    experimentos = [exp for exp in experimentos if exp.nombre != nombre]
    print(f"Experimento {nombre} eliminado si existía.")

def calcular_datosestadisticos():
    """Calcula estadísticas básicas de los experimentos (media, desviación estándar)."""
    if not experimentos:
        print("No hay experimentos registrados para calcular estadísticas.")
        return

    for exp in experimentos:
        media = statistics.mean(exp.resultados)
        desviacion = statistics.stdev(exp.resultados) if len(exp.resultados) > 1 else 0
        print(f"Estadísticas del experimento '{exp.nombre}':")
        print(f" - Media: {media}")
        print(f" - Desviación estándar: {desviacion}")
        print()

def generar_informeExperimentos():
    """Genera un informe con todos los experimentos registrados."""
    if not experimentos:
        print("No hay experimentos para generar un informe.")
        return

    informe = "Informe de Experimentos:\n"
    for exp in experimentos:
        informe += f"Nombre: {exp.nombre}, Fecha: {exp.fecha}, Tipo: {exp.tipo}, Resultados: {exp.resultados}\n"
    
    # Guardar el informe en un archivo
    with open("informe_experimentos.txt", "w") as f:
        f.write(informe)
    
    print("Informe generado con éxito: 'informe_experimentos.txt'")

def mostrar_menu():
    """Muestra el menú principal."""
    print("**********MENU PRINCIPAL***********")
    print("**********Gestion de Experimentos***********")
    print("1. Agregar experimento")
    print("2. Visualizar experimentos")
    print("3. Eliminar experimento")
    print("**********Analisis de datos***********")
    print("4. Calcular estadísticas")
    print("5. Comparar experimentos")
    print("**********Informes***********")
    print("6. Generar informes")
    print("7. Salir")

def comparar_experimentos():
    """Compara los resultados de dos experimentos."""
    if len(experimentos) < 2:
        print("Se necesitan al menos dos experimentos para comparar.")
        return
    
    nombre1 = input("Introduce el nombre del primer experimento: ")
    nombre2 = input("Introduce el nombre del segundo experimento: ")

    exp1 = next((exp for exp in experimentos if exp.nombre == nombre1), None)
    exp2 = next((exp for exp in experimentos if exp.nombre == nombre2), None)

    if exp1 and exp2:
        print(f"Comparando '{exp1.nombre}' y '{exp2.nombre}'")
        print(f"Media de {exp1.nombre}: {statistics.mean(exp1.resultados)}")
        print(f"Media de {exp2.nombre}: {statistics.mean(exp2.resultados)}")
        # Aquí puedes agregar más criterios de comparación si es necesario
    else:
        print("No se encontraron experimentos con los nombres dados.")

def main():
    """Controla el flujo general del sistema."""
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_experimentos()
        elif opcion == '2':
            visualizar_experimentos()
        elif opcion == '3':
            gestionar_experimentos()
        elif opcion == '4':
            calcular_datosestadisticos()
        elif opcion == '5':
            comparar_experimentos()
        elif opcion == '6':
            generar_informeExperimentos()
        elif opcion == '7':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

# Llamamos a la función principal para ejecutar el programa
main()