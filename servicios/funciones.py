from Clases.objetos import Variante

class Recomendador:
    def buscar(self, nombre_ejercicio, fase):
        sugerencia = "Variante no encontrada"
        rpe_ideal = ""
        
        match nombre_ejercicio:
            case "Sentadilla":
                match fase:
                    case "entrada": sugerencia, rpe_ideal = "Sentadilla Tempo (3-2-0)", "RPE 7"
                    case "pausa": sugerencia, rpe_ideal = "Sentadilla con Pausa", "RPE 8"
                    case "salida": sugerencia, rpe_ideal = "Pin Squat", "RPE 8-9"
            case "Banca":
                match fase:
                    case "entrada": sugerencia, rpe_ideal = "Press con Mancuernas", "RPE 7-8"
                    case "pausa": sugerencia, rpe_ideal = "Spoto Press", "RPE 8"
                    case "salida": sugerencia, rpe_ideal = "Floor Press", "RPE 8.5"
            case "Peso Muerto":
                match fase:
                    case "entrada": sugerencia, rpe_ideal = "Peso Muerto con Déficit", "RPE 7.5"
                    case "pausa": sugerencia, rpe_ideal = "Peso Muerto Pausa en Rodilla", "RPE 8"
                    case "salida": sugerencia, rpe_ideal = "Block Pulls", "RPE 9"

        return Variante(nombre_ejercicio, sugerencia, fase, rpe_ideal)

    def generar_rutina_completa(self, movimiento, variante_recetada):
        rutina = f"\n" + "="*60 + "\n"
        rutina += f"   RUTINA DE ESPECIALIZACIÓN: ENFOQUE EN {movimiento.upper()}\n"
        rutina += "="*60 + "\n"
        
        if movimiento == "Sentadilla":
            rutina += f"1️⃣ EJERCICIO PRINCIPAL (Fuerza Base):\n"
            rutina += f"   -> Sentadilla Libre: 3 series x 5 repeticiones.\n\n"
            rutina += f"2️⃣ VARIANTE TÉCNICA CORRECTIVA:\n"
            rutina += f"   -> {variante_recetada}: 3 series x 6 repeticiones.\n\n"
            rutina += f"3️⃣ ACCESORIOS HIPERTROFIA (Sinergistas):\n"
            rutina += f"   - Prensa Inclinada: 3 series x 10-12 reps.\n"
            rutina += f"   - Sillón de Isquios: 3 series x 12 reps.\n"
            rutina += f"   - Plancha Abdominal: 3 series al fallo.\n"
        elif movimiento == "Banca":
            rutina += f"1️⃣ EJERCICIO PRINCIPAL (Fuerza Base):\n"
            rutina += f"   -> Press de Banca Plano: 3 series x 5 repeticiones.\n\n"
            rutina += f"2️⃣ VARIANTE TÉCNICA CORRECTIVA:\n"
            rutina += f"   -> {variante_recetada}: 3 series x 6 repeticiones.\n\n"
            rutina += f"3️⃣ ACCESORIOS HIPERTROFIA (Sinergistas):\n"
            rutina += f"   - Press Inclinado con Mancuernas: 3 series x 10 reps.\n"
            rutina += f"   - Remo con Barra: 4 series x 8 reps.\n"
            rutina += f"   - Extensiones de Tríceps: 3 series x 12 reps.\n"
        elif movimiento == "Peso Muerto":
            rutina += f"1️⃣ EJERCICIO PRINCIPAL (Fuerza Base):\n"
            rutina += f"   -> Peso Muerto Tradicional: 3 series x 3 repeticiones.\n\n"
            rutina += f"2️⃣ VARIANTE TÉCNICA CORRECTIVA:\n"
            rutina += f"   -> {variante_recetada}: 3 series x 5 repeticiones.\n\n"
            rutina += f"3️⃣ ACCESORIOS HIPERTROFIA (Sinergistas):\n"
            rutina += f"   - Peso Muerto Rumano: 3 series x 8 reps.\n"
            rutina += f"   - Hip Thrust: 3 series x 10 reps.\n"
            rutina += f"   - Farmer Walks: 3 series x 40 metros.\n"

        rutina += "="*60 + "\n"
        return rutina

    def generar_periodizacion_bloques(self, movimiento, rm_maximo):
        b1_min, b1_max = rm_maximo * 0.65, rm_maximo * 0.70
        b2_min, b2_max = rm_maximo * 0.75, rm_maximo * 0.80
        b3_min, b3_max = rm_maximo * 0.80, rm_maximo * 0.85
        b4_min, b4_max = rm_maximo * 0.90, rm_maximo * 0.95
        b5_min, b5_max = rm_maximo * 0.50, rm_maximo * 0.60

        plan = f"\n" + "="*78 + "\n"
        plan += f"  MACROCICLO DE PERIODIZACIÓN: {movimiento.upper()} (1RM Base: {rm_maximo} kg)\n"
        plan += "="*78 + "\n"
        plan += f"| {'BLOQUE':<15} | {'SEMANAS':<9} | {'ESQUEMA (Ser x Rep)':<20} | {'CARGA EXACTA (kg)':<20} |\n"
        plan += f"|" + "-"*17 + "|" + "-"*11 + "|" + "-"*22 + "|" + "-"*22 + "|\n"
        plan += f"| {'1. Hipertrofia':<15} | {'1 a 4':<9} | {'4 series x 8-10':<20} | {b1_min:.1f} a {b1_max:.1f} kg{' ':>7}|\n"
        plan += f"| {'2. Fuerza Base':<15} | {'5 a 8':<9} | {'4 series x 5-6':<20} | {b2_min:.1f} a {b2_max:.1f} kg{' ':>7}|\n"
        plan += f"| {'3. Volumen':<15} | {'9 a 11':<9} | {'5 series x 4':<20} | {b3_min:.1f} a {b3_max:.1f} kg{' ':>7}|\n"
        plan += f"| {'4. Peaking':<15} | {'12 a 14':<9} | {'3 series x 2-3':<20} | {b4_min:.1f} a {b4_max:.1f} kg{' ':>7}|\n"
        plan += f"| {'5. Descarga':<15} | {'15':<9} | {'2 series x 3 (vel.)':<20} | {b5_min:.1f} a {b5_max:.1f} kg{' ':>7}|\n"
        plan += "="*78 + "\n"
        return plan