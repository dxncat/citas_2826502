-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.28-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para citas_2826502
DROP DATABASE IF EXISTS `citas_2826502`;
CREATE DATABASE IF NOT EXISTS `citas_2826502` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `citas_2826502`;

-- Volcando estructura para tabla citas_2826502.citas
DROP TABLE IF EXISTS `citas`;
CREATE TABLE IF NOT EXISTS `citas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL DEFAULT current_timestamp(),
  `hora` time NOT NULL,
  `consultorio` int(11) NOT NULL DEFAULT 0,
  `doctor_id` int(11) NOT NULL,
  `paciente_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_citas_medicos` (`doctor_id`),
  KEY `FK_citas_pacientes` (`paciente_id`),
  CONSTRAINT `FK_citas_medicos` FOREIGN KEY (`doctor_id`) REFERENCES `medicos` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_citas_pacientes` FOREIGN KEY (`paciente_id`) REFERENCES `pacientes` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla citas_2826502.citas: ~4 rows (aproximadamente)
DELETE FROM `citas`;
INSERT INTO `citas` (`id`, `fecha`, `hora`, `consultorio`, `doctor_id`, `paciente_id`) VALUES
	(1, '2030-10-10', '16:03:00', 413, 1, 2),
	(2, '0000-00-00', '19:57:50', 401, 2, 2),
	(3, '2026-02-14', '19:58:31', 306, 2, 1),
	(7, '2024-02-14', '17:01:11', 302, 1, 2);

-- Volcando estructura para tabla citas_2826502.medicos
DROP TABLE IF EXISTS `medicos`;
CREATE TABLE IF NOT EXISTS `medicos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombres` varchar(50) NOT NULL,
  `especialidad` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla citas_2826502.medicos: ~2 rows (aproximadamente)
DELETE FROM `medicos`;
INSERT INTO `medicos` (`id`, `nombres`, `especialidad`) VALUES
	(1, 'Gustavo ', 'Pediatra'),
	(2, 'Margarita', 'Oncologia');

-- Volcando estructura para tabla citas_2826502.pacientes
DROP TABLE IF EXISTS `pacientes`;
CREATE TABLE IF NOT EXISTS `pacientes` (
  `Nombre` varchar(50) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `n_documento` bigint(20) NOT NULL DEFAULT 0,
  `celular` bigint(20) NOT NULL DEFAULT 0,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla citas_2826502.pacientes: ~2 rows (aproximadamente)
DELETE FROM `pacientes`;
INSERT INTO `pacientes` (`Nombre`, `apellidos`, `n_documento`, `celular`, `id`) VALUES
	('Jhosep', 'Medina', 1032386864, 3112434602, 1),
	('Alejandro', 'Vidal', 1032386865, 3112434603, 2);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
