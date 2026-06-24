class ValidacionAtletaError(Exception):
    """Excepción personalizada para reglas de negocio del sistema."""
    pass

class Persona:
    def __init__(self, nombre, peso, squat, bench, deadlift):
        self.nombre = nombre 
        self.peso = peso
        self.sq = float(squat)
        self.bn = float(bench)
        self.dl = float(deadlift)

    def __str__(self):
        return f"Atleta: {self.nombre} | Peso Corporal: {self.peso}kg"

    # --- ENCAPSULAMIENTO (Getters y Setters) ---
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        # Eliminamos espacios para verificar
        limpio = valor.strip()
        # Verificar si hay números en el string
        if any(char.isdigit() for char in limpio):
            raise ValueError("El nombre no puede contener números.")
        if len(limpio) < 3:
            raise ValueError("El nombre debe tener al menos 3 letras.")
        self.__nombre = limpio

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, valor):
        v = float(valor)
        if v <= 0 or v > 400:
            raise ValidacionAtletaError(f"El peso de {v}kg es inválido.")
        self.__peso = v

    # --- LÓGICA DE DIAGNÓSTICO ---
    def evaluar_y_obtener_peor(self):
        ratio_sq = self.sq / self.peso
        ratio_bn = self.bn / self.peso
        ratio_dl = self.dl / self.peso

        print("\n--- TUS NIVELES DE FUERZA ---")
        print(f"Sentadilla: {ratio_sq:.2f}x (Nivel: {self._clasificar(ratio_sq, 1.25, 2.0)})")
        print(f"Banca: {ratio_bn:.2f}x (Nivel: {self._clasificar(ratio_bn, 1.0, 1.5)})")
        print(f"Peso Muerto: {ratio_dl:.2f}x (Nivel: {self._clasificar(ratio_dl, 1.5, 2.5)})")

        falta_sq = 2.0 - ratio_sq
        falta_bn = 1.5 - ratio_bn
        falta_dl = 2.5 - ratio_dl

        if falta_sq >= falta_bn and falta_sq >= falta_dl: 
            return "Sentadilla", self.sq
        elif falta_bn >= falta_sq and falta_bn >= falta_dl: 
            return "Banca", self.bn
        else: 
            return "Peso Muerto", self.dl

    def _clasificar(self, ratio, intermedio, avanzado):
        if ratio >= avanzado: return "Avanzado/Élite"
        elif ratio >= intermedio: return "Intermedio"
        else: return "Principiante"

    def mostrar_tabla_rm(self, movimiento, rm_maximo):
        print(f"\n--- TABLA DE %RM PARA {movimiento.upper()} ---")
        print(f"100%: {rm_maximo} kg -> RPE 10 (Esfuerzo Máximo)")
        print(f" 90%: {rm_maximo * 0.90:.1f} kg -> RPE 9 (1 rep en recámara)")
        print(f" 80%: {rm_maximo * 0.80:.1f} kg -> RPE 8 (2 reps en recámara)")
        print(f" 70%: {rm_maximo * 0.70:.1f} kg -> RPE 7 (Velocidad y control)")

    def estimar_reps(self, movimiento, peso_objetivo):
        rm = self.sq if movimiento == "Sentadilla" else self.bn if movimiento == "Banca" else self.dl
        if peso_objetivo >= rm: return 1
        if peso_objetivo <= 0: raise ValueError("El peso debe ser mayor a 0.")
        return round(30 * ((rm / peso_objetivo) - 1))

# --- HERENCIA ---
class Ejercicio:
    def __init__(self, nombre):
        self.nombre = nombre

class Variante(Ejercicio):
    def __init__(self, nombre_base, nombre_variante, fase, rpe_sugerido):
        super().__init__(nombre_base)
        self.nombre_variante = nombre_variante
        self.fase = fase
        self.rpe_sugerido = rpe_sugerido