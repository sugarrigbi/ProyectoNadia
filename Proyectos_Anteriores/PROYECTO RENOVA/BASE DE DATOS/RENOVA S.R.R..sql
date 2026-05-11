-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: renova_db
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `actividades`
--

DROP TABLE IF EXISTS `actividades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actividades` (
  `id_actividad` int NOT NULL AUTO_INCREMENT,
  `id_plan` int DEFAULT NULL,
  `nombre_actividad` varchar(150) DEFAULT NULL,
  `descripcion` text,
  PRIMARY KEY (`id_actividad`),
  KEY `id_plan` (`id_plan`),
  CONSTRAINT `actividades_ibfk_1` FOREIGN KEY (`id_plan`) REFERENCES `planes_reparacion` (`id_plan`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actividades`
--

LOCK TABLES `actividades` WRITE;
/*!40000 ALTER TABLE `actividades` DISABLE KEYS */;
INSERT INTO `actividades` VALUES (1,1,'Recolectar basura','Limpieza de parque'),(2,2,'Servir alimentos','Apoyo en comedor'),(3,3,'Siembra de árboles','Reforestación en parques'),(4,4,'Charlas educativas','Educación vial'),(5,5,'Apoyo en urgencias','Ayuda en hospitales'),(6,6,'Reparación de calles','Mantenimiento urbano');
/*!40000 ALTER TABLE `actividades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asignacion_planes`
--

DROP TABLE IF EXISTS `asignacion_planes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asignacion_planes` (
  `id_asignacion` int NOT NULL AUTO_INCREMENT,
  `id_infractor` int DEFAULT NULL,
  `id_plan` int DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_fin` date DEFAULT NULL,
  `estado` enum('Activo','Finalizado','Cancelado') DEFAULT NULL,
  PRIMARY KEY (`id_asignacion`),
  KEY `id_infractor` (`id_infractor`),
  KEY `idx_plan_asignacion` (`id_plan`),
  CONSTRAINT `asignacion_planes_ibfk_1` FOREIGN KEY (`id_infractor`) REFERENCES `infractores` (`id_infractor`),
  CONSTRAINT `asignacion_planes_ibfk_2` FOREIGN KEY (`id_plan`) REFERENCES `planes_reparacion` (`id_plan`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asignacion_planes`
--

LOCK TABLES `asignacion_planes` WRITE;
/*!40000 ALTER TABLE `asignacion_planes` DISABLE KEYS */;
INSERT INTO `asignacion_planes` VALUES (1,1,1,'2026-02-05','2026-03-05','Activo'),(2,2,2,'2026-02-06','2026-03-20','Activo'),(3,3,3,'2026-02-10','2026-03-20','Activo'),(4,4,4,'2026-02-12','2026-03-15','Activo'),(5,5,5,'2026-02-15','2026-04-10','Activo'),(6,6,6,'2026-02-18','2026-03-18','Activo');
/*!40000 ALTER TABLE `asignacion_planes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clasificacion_delitos`
--

DROP TABLE IF EXISTS `clasificacion_delitos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clasificacion_delitos` (
  `id_clasificacion` int NOT NULL AUTO_INCREMENT,
  `nombre_clasificacion` varchar(100) DEFAULT NULL,
  `descripcion` text,
  PRIMARY KEY (`id_clasificacion`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clasificacion_delitos`
--

LOCK TABLES `clasificacion_delitos` WRITE;
/*!40000 ALTER TABLE `clasificacion_delitos` DISABLE KEYS */;
INSERT INTO `clasificacion_delitos` VALUES (1,'Contra la propiedad','Delitos relacionados con bienes materiales'),(2,'Contra la persona','Delitos que afectan la integridad física'),(3,'Contra la sociedad','Delitos que afectan la convivencia'),(4,'Contra la familia','Delitos dentro del núcleo familiar'),(5,'Administrativos','Infracciones a normas legales o administrativas');
/*!40000 ALTER TABLE `clasificacion_delitos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delitos`
--

DROP TABLE IF EXISTS `delitos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delitos` (
  `id_delito` int NOT NULL AUTO_INCREMENT,
  `nombre_delito` varchar(150) NOT NULL,
  `descripcion` text,
  `nivel_gravedad` enum('Bajo','Medio','Alto') NOT NULL,
  `id_clasificacion` int DEFAULT NULL,
  PRIMARY KEY (`id_delito`),
  KEY `fk_delito_clasificacion` (`id_clasificacion`),
  CONSTRAINT `fk_delito_clasificacion` FOREIGN KEY (`id_clasificacion`) REFERENCES `clasificacion_delitos` (`id_clasificacion`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delitos`
--

LOCK TABLES `delitos` WRITE;
/*!40000 ALTER TABLE `delitos` DISABLE KEYS */;
INSERT INTO `delitos` VALUES (1,'Hurto menor','Robo sin violencia','Bajo',1),(2,'Daño a propiedad','Daño a bienes públicos','Medio',1),(3,'Hurto calificado','Robo con agravantes','Alto',1),(4,'Lesiones personales','Daño físico a otra persona','Medio',1),(5,'Vandalismo','Daño a bienes públicos o privados','Bajo',NULL),(6,'Fraude','Engaño con beneficio económico','Alto',NULL),(7,'Violencia intrafamiliar','Maltrato dentro del núcleo familiar','Alto',NULL),(8,'Consumo de sustancias en vía pública','Consumo en espacios públicos','Bajo',NULL),(9,'Conducción en estado de embriaguez','Manejo bajo efectos del alcohol','Medio',NULL),(10,'Perturbación del orden público','Alteración de la convivencia','Bajo',NULL);
/*!40000 ALTER TABLE `delitos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `evaluaciones`
--

DROP TABLE IF EXISTS `evaluaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `evaluaciones` (
  `id_evaluacion` int NOT NULL AUTO_INCREMENT,
  `id_infractor` int DEFAULT NULL,
  `id_delito` int DEFAULT NULL,
  `id_evaluador` int DEFAULT NULL,
  `elegible` tinyint(1) DEFAULT NULL,
  `observaciones` text,
  `fecha_evaluacion` date DEFAULT NULL,
  PRIMARY KEY (`id_evaluacion`),
  KEY `id_evaluador` (`id_evaluador`),
  KEY `idx_infractor_eval` (`id_infractor`),
  KEY `idx_delito_eval` (`id_delito`),
  CONSTRAINT `evaluaciones_ibfk_1` FOREIGN KEY (`id_infractor`) REFERENCES `infractores` (`id_infractor`),
  CONSTRAINT `evaluaciones_ibfk_2` FOREIGN KEY (`id_delito`) REFERENCES `delitos` (`id_delito`),
  CONSTRAINT `evaluaciones_ibfk_3` FOREIGN KEY (`id_evaluador`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evaluaciones`
--

LOCK TABLES `evaluaciones` WRITE;
/*!40000 ALTER TABLE `evaluaciones` DISABLE KEYS */;
INSERT INTO `evaluaciones` VALUES (1,1,1,2,1,'Apto para programa','2026-02-01'),(2,2,2,2,1,'Debe cumplir actividades','2026-02-02');
/*!40000 ALTER TABLE `evaluaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `impacto_comunitario`
--

DROP TABLE IF EXISTS `impacto_comunitario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `impacto_comunitario` (
  `id_impacto` int NOT NULL AUTO_INCREMENT,
  `id_infractor` int DEFAULT NULL,
  `descripcion` text,
  `puntuacion` int DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL,
  PRIMARY KEY (`id_impacto`),
  KEY `id_infractor` (`id_infractor`),
  CONSTRAINT `impacto_comunitario_ibfk_1` FOREIGN KEY (`id_infractor`) REFERENCES `infractores` (`id_infractor`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `impacto_comunitario`
--

LOCK TABLES `impacto_comunitario` WRITE;
/*!40000 ALTER TABLE `impacto_comunitario` DISABLE KEYS */;
INSERT INTO `impacto_comunitario` VALUES (1,1,'Mejora del parque',8,'2026-03-01'),(2,2,'Apoyo social positivo',7,'2026-03-02'),(3,3,'Reforestación exitosa',9,'2026-03-05'),(4,4,'Conciencia vial generada',8,'2026-03-06'),(5,5,'Apoyo hospitalario',7,'2026-03-07'),(6,6,'Mejora urbana visible',9,'2026-03-08');
/*!40000 ALTER TABLE `impacto_comunitario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `infractores`
--

DROP TABLE IF EXISTS `infractores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `infractores` (
  `id_infractor` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) DEFAULT NULL,
  `documento` varchar(20) DEFAULT NULL,
  `edad` int DEFAULT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `ciudad` varchar(100) DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_infractor`),
  UNIQUE KEY `documento` (`documento`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `infractores`
--

LOCK TABLES `infractores` WRITE;
/*!40000 ALTER TABLE `infractores` DISABLE KEYS */;
INSERT INTO `infractores` VALUES (1,'Juan','Perez','12345678',25,'Calle 10','Bogotá','2026-01-10',NULL),(2,'Maria','Gomez','87654321',30,'Carrera 20','Bogotá','2026-01-12',NULL),(3,'Luis','Martinez','11223344',22,'Calle 45','Bogotá','2026-01-15','3011111111'),(4,'Andres','Lopez','22334455',28,'Carrera 15','Bogotá','2026-01-16','3022222222'),(5,'Camila','Torres','33445566',19,'Calle 80','Bogotá','2026-01-18','3033333333'),(6,'Sofia','Ramirez','44556677',35,'Av Boyacá','Bogotá','2026-01-20','3044444444');
/*!40000 ALTER TABLE `infractores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `planes_reparacion`
--

DROP TABLE IF EXISTS `planes_reparacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `planes_reparacion` (
  `id_plan` int NOT NULL AUTO_INCREMENT,
  `nombre_plan` varchar(150) DEFAULT NULL,
  `descripcion` text,
  `duracion_semanas` int DEFAULT NULL,
  PRIMARY KEY (`id_plan`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `planes_reparacion`
--

LOCK TABLES `planes_reparacion` WRITE;
/*!40000 ALTER TABLE `planes_reparacion` DISABLE KEYS */;
INSERT INTO `planes_reparacion` VALUES (1,'Limpieza comunitaria','Limpieza de parques',4),(2,'Apoyo social','Ayuda en comedores comunitarios',6),(3,'Reforestación','Siembra de árboles en zonas afectadas',8),(4,'Educación vial','Charlas sobre normas de tránsito',4),(5,'Apoyo en hospitales','Colaboración en centros de salud',6),(6,'Mantenimiento urbano','Reparación de espacios públicos',5);
/*!40000 ALTER TABLE `planes_reparacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reduccion_pena`
--

DROP TABLE IF EXISTS `reduccion_pena`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reduccion_pena` (
  `id_reduccion` int NOT NULL AUTO_INCREMENT,
  `id_infractor` int DEFAULT NULL,
  `porcentaje_reduccion` decimal(5,2) DEFAULT NULL,
  `motivo` text,
  `fecha_calculo` date DEFAULT NULL,
  PRIMARY KEY (`id_reduccion`),
  KEY `id_infractor` (`id_infractor`),
  CONSTRAINT `reduccion_pena_ibfk_1` FOREIGN KEY (`id_infractor`) REFERENCES `infractores` (`id_infractor`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reduccion_pena`
--

LOCK TABLES `reduccion_pena` WRITE;
/*!40000 ALTER TABLE `reduccion_pena` DISABLE KEYS */;
INSERT INTO `reduccion_pena` VALUES (1,1,20.00,'Buen desempeño','2026-03-10'),(2,2,15.00,'Cumplimiento parcial','2026-03-12'),(3,3,25.00,'Excelente desempeño','2026-03-15'),(4,4,18.00,'Buen cumplimiento','2026-03-16'),(5,5,10.00,'Participación parcial','2026-03-17'),(6,6,30.00,'Desempeño sobresaliente','2026-03-18');
/*!40000 ALTER TABLE `reduccion_pena` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id_rol` int NOT NULL AUTO_INCREMENT,
  `nombre_rol` varchar(50) NOT NULL,
  PRIMARY KEY (`id_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Administrador'),(2,'Evaluador'),(3,'Supervisor'),(4,'Administrador'),(5,'Evaluador'),(6,'Supervisor'),(7,'superivisor'),(8,'Administrador'),(9,'Evaluador'),(10,'Supervisor'),(11,'superivisor'),(12,'Administrador'),(13,'Evaluador'),(14,'Supervisor');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seguimiento`
--

DROP TABLE IF EXISTS `seguimiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seguimiento` (
  `id_seguimiento` int NOT NULL AUTO_INCREMENT,
  `id_actividad` int DEFAULT NULL,
  `id_infractor` int DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `estado` enum('Pendiente','En proceso','Completado') DEFAULT NULL,
  `observaciones` text,
  PRIMARY KEY (`id_seguimiento`),
  KEY `id_actividad` (`id_actividad`),
  KEY `id_infractor` (`id_infractor`),
  CONSTRAINT `seguimiento_ibfk_1` FOREIGN KEY (`id_actividad`) REFERENCES `actividades` (`id_actividad`),
  CONSTRAINT `seguimiento_ibfk_2` FOREIGN KEY (`id_infractor`) REFERENCES `infractores` (`id_infractor`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seguimiento`
--

LOCK TABLES `seguimiento` WRITE;
/*!40000 ALTER TABLE `seguimiento` DISABLE KEYS */;
INSERT INTO `seguimiento` VALUES (1,1,1,'2026-02-10','Completado','Actividad realizada correctamente'),(2,2,2,'2026-02-12','En proceso','Actividad en curso');
/*!40000 ALTER TABLE `seguimiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `id_rol` int DEFAULT NULL,
  `fecha_registro` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `email` (`email`),
  KEY `id_rol` (`id_rol`),
  CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'julian Administrador','admin@renova.com','hash123',1,'2026-03-19 19:45:32'),(2,'alejandro Evaluador','evaluador@renova.com','hash123',2,'2026-03-19 19:45:32'),(3,'duvan Supervisor','supervisor@renova.com','hash123',3,'2026-03-19 19:45:32'),(4,'sebastian Supervisor','supervisor2@renova.com','hash123',3,'2026-03-19 19:45:32');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'renova_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-19 15:22:32
