-- =============================================================
-- SECCIÓN 2.1: Modelado de Datos (DDL)
-- =============================================================
-- Instrucciones:
-- Escribe las sentencias CREATE TABLE para almacenar 'desarrollos' y 'leads'.
-- Considera llaves primarias, foráneas, tipos de datos e índices recomendados.

-- CREATE TABLE desarrollos (...);

-- CREATE TABLE leads (...);

-- =============================================================
-- SECCIÓN 2.1: Modelado de Datos (DDL)
-- =============================================================

-- 1. Tabla de Desarrollos
CREATE TABLE desarrollos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    ubicacion VARCHAR(255) NOT NULL, -- Aquí se guardará "Ciudad" o dirección
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE,
    precio DECIMAL(10, 2) NOT NULL,
    descripcion TEXT
);

-- 2. Tabla de Leads (Conectada a Desarrollos)
CREATE TABLE leads (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    origen VARCHAR(255) NOT NULL,    -- Ej: Web, Facebook, Recomendado
    estatus VARCHAR(255) NOT NULL,   -- Ej: NUEVO, CONTACTADO, VENDIDO
    presupuesto DECIMAL(10, 2) NOT NULL,
    fecha_registro DATE NOT NULL,    -- Campo clave para reportes de tiempo
    desarrollo_id INT,               -- Llave foránea
    
    -- Definición de la Llave Foránea
    FOREIGN KEY (desarrollo_id) REFERENCES desarrollos(id) ON DELETE SET NULL
);
