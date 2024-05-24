-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS NYCTaxisDB;

-- Usar la base de datos NYCTaxisDB
USE NYCTaxisDB;

-- Crear la tabla registros
CREATE TABLE IF NOT EXISTS carrerasporzonas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    anio INT,
    mes INT,
    PUlocationId INT,
    conteo_carreras INT,
    taxi_cab VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS ingresosporzonas(
    id INT AUTO_INCREMENT PRIMARY KEY,
    anio INT,
    mes INT,
    PUlocationId INT,
    total_ingresos INT,
    taxi_cab VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS horaspicoporzonas(
    id INT AUTO_INCREMENT PRIMARY KEY,
    anio INT,
    mes INT,
    PUlocationId INT,
    pickup_hour INT,
    conteo_carreras INT,
    taxi_cab VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS zonas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    zone VARCHAR(255),
    LocationID INT,
    borough VARCHAR(255),
    geometry GEOMETRY NOT NULL
);

CREATE TABLE IF NOT EXISTS distanciarecorridoturnolaboral (
    id INT AUTO_INCREMENT PRIMARY KEY,
	anio INT,
    mes INT,
    distancia_recorrida INT,
    taxi_cab VARCHAR(255)

);

CREATE TABLE IF NOT EXISTS cargadoresporcondado(
	id INT AUTO_INCREMENT PRIMARY KEY,
    ciudad VARCHAR(30),
    total_cargadores INT
);

CREATE TABLE IF NOT EXISTS auditoria(
    id INT AUTO_INCREMENT PRIMARY KEY,
    ultima_carga_datos DATE
)


