CREATE DATABASE IF NOT EXISTS sistema_fuerza;
USE sistema_fuerza;

CREATE TABLE IF NOT EXISTS atletas (
    id_atleta INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE NOT NULL,
    peso_corporal DECIMAL(5,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS evaluaciones (
    id_evaluacion INT AUTO_INCREMENT PRIMARY KEY,
    id_atleta INT NOT NULL,
    movimiento VARCHAR(30) NOT NULL,
    variante_recetada VARCHAR(50) NOT NULL,
    rm_evaluado DECIMAL(5,2) NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_atleta) REFERENCES atletas(id_atleta) ON DELETE CASCADE
);