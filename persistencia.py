import mysql.connector

class BaseDeDatos:
    def _conectar(self):
        return mysql.connector.connect(
            host="localhost", user="root", password="", database="sistema_fuerza"
        )

    def guardar_evaluacion(self, atleta, ejercicio_base, variante_rec, rm_evaluado):
        conexion = self._conectar()
        cursor = conexion.cursor()
        try:
            conexion.autocommit = False 
            # Cambiado a 'peso' para que coincida con tu tabla atletas
            cursor.execute("SELECT id_atleta FROM atletas WHERE nombre = %s", (atleta.nombre,))
            resultado = cursor.fetchone()
            
            if resultado:
                id_atleta = resultado[0]
                cursor.execute("UPDATE atletas SET peso = %s WHERE id_atleta = %s", (atleta.peso, id_atleta))
            else:
                cursor.execute("INSERT INTO atletas (nombre, peso) VALUES (%s, %s)", (atleta.nombre, atleta.peso))
                id_atleta = cursor.lastrowid

            # Cambiado a 'variante_recetada' para coincidir con el registro histórico
            sql_eval = "INSERT INTO evaluaciones (id_atleta, movimiento, variante_recomendada, rm_evaluado) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_eval, (id_atleta, ejercicio_base.nombre, variante_rec.nombre_variante, float(rm_evaluado)))
            
            conexion.commit()
            print("\n✅ [BD] Transacción exitosa.")
        except mysql.connector.Error as err:
            conexion.rollback()
            print(f"\n❌ Error en transacción: {err}")
        finally:
            cursor.close()
            conexion.close()
    
    def leer_historial_con_join(self):
        conexion = self._conectar()
        cursor = conexion.cursor()
        # SELECCIONAMOS EL ID PARA QUE EL USUARIO PUEDA VERLO
        sql = """
            SELECT e.id_evaluacion, a.nombre, e.movimiento, e.variante_recomendada, e.rm_evaluado
            FROM atletas a
            INNER JOIN evaluaciones e ON a.id_atleta = e.id_atleta
            ORDER BY e.fecha_evaluacion DESC
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        
        print("\n--- Historial Completo (ID - Atleta - Movimiento - Variante - RM) ---")
        for fila in resultados:
            print(f"ID: {fila[0]} | Atleta: {fila[1]} | Movimiento: {fila[2]} | Variante: {fila[3]} | RM: {fila[4]}kg")
            
        cursor.close()
        conexion.close()

    def actualizar_variante(self, id_evaluacion, nueva_variante):
        conexion = self._conectar()
        cursor = conexion.cursor()
        sql = "UPDATE evaluaciones SET variante_recomendada = %s WHERE id_evaluacion = %s"
        cursor.execute(sql, (nueva_variante, id_evaluacion))
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar_evaluacion(self, id_evaluacion):
        conexion = self._conectar()
        cursor = conexion.cursor()
        sql = "DELETE FROM evaluaciones WHERE id_evaluacion = %s"
        cursor.execute(sql, (id_evaluacion,))
        conexion.commit()
        print(f"✅ Evaluación ID {id_evaluacion} eliminada correctamente.")
        cursor.close()
        conexion.close()