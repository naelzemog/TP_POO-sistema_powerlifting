from clases.objetos import Persona, Ejercicio, ValidacionAtletaError
from servicios.funciones import Recomendador
from datos.persistencia import BaseDeDatos

def main():
    db = BaseDeDatos()
    
    while True:
        print("\n" + "="*35)
        print("   SISTEMA EXPERTO DE FUERZA")
        print("="*35)
        print("1. [CREATE] Evaluar Atleta (Transacción)")
        print("2. [READ]   Ver Historial General (JOIN)")
        print("3. [UPDATE] Corregir una variante recetada")
        print("4. [DELETE] Eliminar una evaluación del registro")
        print("5. Salir")
        opcion = input("Elegí una opción (1-5): ")
        
        match opcion:
            case "1":
                try:
                    nom = input("Nombre: ")
                    p = input("Peso Corporal (kg): ")
                    sq = input("Tu 1RM en Sentadilla (kg): ")
                    bn = input("Tu 1RM en Banca (kg): ")
                    dl = input("Tu 1RM en Peso Muerto (kg): ")
                    
                    atleta = Persona(nom, p, sq, bn, dl)
                    
                    peor_mov, peor_rm = atleta.evaluar_y_obtener_peor()
                    print(f"\n>> Análisis Final: Tu movimiento a mejorar prioritariamente es: {peor_mov}.")
                    
                    print(f"\n¿En qué fase de tu {peor_mov} presentas mayor dificultad técnica?")
                    print("1. Entrada (Bajada excéntrica)\n2. Pausa (Transición/Estancamiento)\n3. Salida (Bloqueo final)")
                    fase_op = input("Elige una opción (1/2/3): ")
                    
                    fases = {"1": "entrada", "2": "pausa", "3": "salida"}
                    fase_elegida = fases.get(fase_op, "pausa")
                    
                    motor = Recomendador()
                    ej_base = Ejercicio(peor_mov)
                    var_rec = motor.buscar(ej_base.nombre, fase_elegida)
                    
                    print("\n--- PRESCRIPCIÓN DE ENTRENAMIENTO ---")
                    print(f"Variante recetada: {var_rec.nombre_variante} | Intensidad: {var_rec.rpe_sugerido}")
                    
                    # Guarda en DB asegurando consistencia (Transacción)
                    db.guardar_evaluacion(atleta, ej_base, var_rec, peor_rm)
                    
                    # Generación del Macrociclo por consola
                    print(f"\n¿Deseas generar un macrociclo estructurado de 15 semanas para {peor_mov}?")
                    if input("(S/N): ").upper() == 'S':
                        print(motor.generar_periodizacion_bloques(peor_mov, peor_rm))
                        
                except ValidacionAtletaError as e:
                    print(f"\n⚠️ ERROR DE NEGOCIO: {e}")
                except ValueError:
                    print(f"\n⚠️ ERROR TÉCNICO: Ingresá solo valores válidos.")
                    
            case "2":
                db.leer_historial_con_join()
                
            case "3":
                try:
                    
                    print("\n(Tip: Revisá la opción 2 para conocer el ID de la evaluación)")
                    id_ev = int(input("Ingresá el ID de la evaluación a modificar: "))
                    nueva_var = input("Nueva variante a recetar: ")
                    db.actualizar_variante(id_ev, nueva_var)
                except ValueError:
                    print("\n⚠️ Error: El ID debe ser un número.")
                    
            case "4":
                try:
                    id_del = int(input("Ingresá el ID de la evaluación a eliminar: "))
                    db.eliminar_evaluacion(id_del)
                except ValueError:
                    print("\n⚠️ Error: El ID debe ser un número.")
                    
            case "5":
                print("\nCerrando el sistema... ¡Entrenamiento finalizado!")
                break
                
            case _:
                print("\n⚠️ Opción inválida. Seleccioná del 1 al 5.")

if __name__ == "__main__":
    main()