CREATE DATABASE basedatos;

USE basedatos;

CREATE TABLE persona (
	id INT AUTO_INCREMENT,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    fecha_nac DATE,
    doc_identidad VARCHAR(11) UNIQUE NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO persona
(nombre, apellido, fecha_nac, doc_identidad)
VALUES
("Albano", "Ablanco", "1980-01-01", "20111222"),
("Beny", "Benassi", "1985-01-01", "30111222"),
("Catalina", "Cantimplora", "1985-01-01", "35111222"),
("Zedd", "Zanahoria", "1999-01-01", "50111222");