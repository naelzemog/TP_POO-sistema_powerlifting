CREATE DATABASE IF NOT EXISTS sistema_fuerza;
USE sistema_fuerza;

CREATE TABLE IF NOT EXISTS atletas (
    id_atleta INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    peso DECIMAL(5,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS evaluaciones (
    id_evaluacion INT AUTO_INCREMENT PRIMARY KEY,
    id_atleta INT NOT NULL,
    movimiento VARCHAR(50) NOT NULL,
    variante_recomendada VARCHAR(100) NOT NULL,
    rm_evaluado DECIMAL(6,2) NOT NULL,
    fecha_evaluacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_atleta) REFERENCES atletas(id_atleta) ON DELETE CASCADE
);