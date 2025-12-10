-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: prueba
-- ------------------------------------------------------
-- Server version	8.0.44

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
-- Table structure for table `tbl_adic_entidad`
--

DROP TABLE IF EXISTS `tbl_adic_entidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_adic_entidad` (
  `Id_Adic_Entidad` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Direccion` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Num_Contact` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `web_site` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fk_entidad` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Descripción` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_Adic_Entidad`),
  KEY `fk_entidad` (`fk_entidad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_adic_entidad`
--

LOCK TABLES `tbl_adic_entidad` WRITE;
/*!40000 ALTER TABLE `tbl_adic_entidad` DISABLE KEYS */;
INSERT INTO `tbl_adic_entidad` VALUES ('001ENA',' Avenida Carrera 30 #48-51','(601) 653 1888','http://www.igac.gov.co','001ENT','a'),('002ENA','Carrera 13 N° 52-95','01-8000-911-170','http://www.minjusticia.gov.co','002ENT','b'),('003ENA','Carrera 7 No. 32 – 42','01-8000-119-450','http://www.minagricultura.gov.co','003ENT','c'),('004ENA','Carrera 10 No. 27-51','(601) 341 2073','http://www.urt.gov.co','004ENT','d'),('005ENA','Entidad_Prueba','31440','Entidad_Prueba','005ENT','Entidad_PruebaEntidad_PruebaEntidad_Prueba');
/*!40000 ALTER TABLE `tbl_adic_entidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_adic_persona`
--

DROP TABLE IF EXISTS `tbl_adic_persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_adic_persona` (
  `Id_Adic_Persona` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Edad` int NOT NULL,
  `Dirección` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Num_Contact` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `fk_persona` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fk_dir` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Terminos_Condiciones` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_Adic_Persona`),
  KEY `fk_persona` (`fk_persona`),
  CONSTRAINT `tbl_adic_persona_ibfk_1` FOREIGN KEY (`fk_persona`) REFERENCES `tbl_persona` (`Id_Persona`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_adic_persona`
--

LOCK TABLES `tbl_adic_persona` WRITE;
/*!40000 ALTER TABLE `tbl_adic_persona` DISABLE KEYS */;
INSERT INTO `tbl_adic_persona` VALUES ('000PAD',0,'Admin','Admin','administrador@gaialink.online','00000000','','1'),('002PAD',18,'Exitoso','1111111111','sugarrigbi3@gmail.com','1145224601','001BAR','1'),('003PAD',25,'Bogotá','3144048151','kmanzolag@sanmateo.edu.co','123456789','002BAR','1'),('004PAD',18,'PruebaAdmin','3144048151','sugarrigbi2@gmail.com','987654321',NULL,'1'),('005PAD',23,'Prueba2','3144048151','pepito@gmail.com','192837465','003BAR','1'),('006PAD',25,'Prueba','3109876543','pedro@gmail.com','1324354657',NULL,'1'),('007PAD',20,'EXITOSA','1928373645','pepapin@gmail.com','123987465',NULL,'1');
/*!40000 ALTER TABLE `tbl_adic_persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_ayuda`
--

DROP TABLE IF EXISTS `tbl_ayuda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_ayuda` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) DEFAULT NULL,
  `Mensaje` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_ayuda`
--

LOCK TABLES `tbl_ayuda` WRITE;
/*!40000 ALTER TABLE `tbl_ayuda` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_ayuda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_barrio`
--

DROP TABLE IF EXISTS `tbl_barrio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_barrio` (
  `Id_barrio` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Barrio` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fk_local` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_barrio`),
  KEY `fk_local` (`fk_local`),
  CONSTRAINT `tbl_barrio_ibfk_1` FOREIGN KEY (`fk_local`) REFERENCES `tbl_localidad` (`Id_local`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_barrio`
--

LOCK TABLES `tbl_barrio` WRITE;
/*!40000 ALTER TABLE `tbl_barrio` DISABLE KEYS */;
INSERT INTO `tbl_barrio` VALUES ('001BAR','Santa Lucia','001LOC'),('002BAR','asdasdad','002LOC'),('003BAR','Prueba','003LOC');
/*!40000 ALTER TABLE `tbl_barrio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_calificanos`
--

DROP TABLE IF EXISTS `tbl_calificanos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_calificanos` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) DEFAULT NULL,
  `Pregunta1` varchar(50) DEFAULT NULL,
  `Pregunta2` varchar(50) DEFAULT NULL,
  `Pregunta3` varchar(50) DEFAULT NULL,
  `Pregunta4` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_calificanos`
--

LOCK TABLES `tbl_calificanos` WRITE;
/*!40000 ALTER TABLE `tbl_calificanos` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_calificanos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_caso`
--

DROP TABLE IF EXISTS `tbl_caso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_caso` (
  `Id_Caso_Incidente` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Fecha` date NOT NULL,
  `Descripción` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Personas_Afectadas` int NOT NULL,
  `Direccion` varchar(45) COLLATE utf8mb4_general_ci NOT NULL,
  `Fk_Usuario` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Fk_Incidente` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Fk_Dep` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Fk_Tipo_Caso` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Fk_Estado` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_Caso_Incidente`),
  KEY `Fk_Usuario` (`Fk_Usuario`),
  KEY `Fk_Incidente` (`Fk_Incidente`),
  KEY `Fk_Dep` (`Fk_Dep`),
  KEY `Fk_Estado` (`Fk_Estado`),
  KEY `Fk_Tipo_Caso` (`Fk_Tipo_Caso`),
  CONSTRAINT `tbl_caso_ibfk_1` FOREIGN KEY (`Fk_Usuario`) REFERENCES `tbl_usuario` (`Id_usuario`),
  CONSTRAINT `tbl_caso_ibfk_2` FOREIGN KEY (`Fk_Incidente`) REFERENCES `tbl_incidente` (`Id_incidente`),
  CONSTRAINT `tbl_caso_ibfk_3` FOREIGN KEY (`Fk_Dep`) REFERENCES `tbl_departamento` (`Id_dep`),
  CONSTRAINT `tbl_caso_ibfk_4` FOREIGN KEY (`Fk_Estado`) REFERENCES `tbl_estado` (`Id_estado`),
  CONSTRAINT `tbl_caso_ibfk_5` FOREIGN KEY (`Fk_Tipo_Caso`) REFERENCES `tbl_tipo_caso` (`Id_caso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_caso`
--

LOCK TABLES `tbl_caso` WRITE;
/*!40000 ALTER TABLE `tbl_caso` DISABLE KEYS */;
INSERT INTO `tbl_caso` VALUES ('001CAD','2025-11-06','aaaaaaaaaaaaaaa',2,'Dg 49 sur','000USU','Despl','001DEP','Caso','Caso_03'),('002CAD','2025-11-17','asdddddddddddddddddddddddddddddddd',23,'asdasdas','002USU','Despl','001DEP','Caso','Caso_04'),('003CAD','2025-12-01','asdasdaasdasdaasdasdaasdasda',3,'Prueba_Admin','007USU','Despl','001DEP','Caso','Caso_01');
/*!40000 ALTER TABLE `tbl_caso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_ciudad`
--

DROP TABLE IF EXISTS `tbl_ciudad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_ciudad` (
  `Id_ciudad` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Nom_ciudad` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Fk_Dep` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_ciudad`),
  KEY `Fk_Dep` (`Fk_Dep`),
  CONSTRAINT `tbl_ciudad_ibfk_1` FOREIGN KEY (`Fk_Dep`) REFERENCES `tbl_departamento` (`Id_dep`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_ciudad`
--

LOCK TABLES `tbl_ciudad` WRITE;
/*!40000 ALTER TABLE `tbl_ciudad` DISABLE KEYS */;
INSERT INTO `tbl_ciudad` VALUES ('001CIU','Bogota','001DEP'),('002CIU','PruebaAdmin','003DEP'),('003CIU','Prueba','004DEP'),('004CIU','EXITOSA','005DEP');
/*!40000 ALTER TABLE `tbl_ciudad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_contactanos`
--

DROP TABLE IF EXISTS `tbl_contactanos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_contactanos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `correo` varchar(100) NOT NULL,
  `mensaje` text NOT NULL,
  `fecha_envio` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_contactanos`
--

LOCK TABLES `tbl_contactanos` WRITE;
/*!40000 ALTER TABLE `tbl_contactanos` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_contactanos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_departamento`
--

DROP TABLE IF EXISTS `tbl_departamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_departamento` (
  `Id_dep` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Nom_departamento` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_dep`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_departamento`
--

LOCK TABLES `tbl_departamento` WRITE;
/*!40000 ALTER TABLE `tbl_departamento` DISABLE KEYS */;
INSERT INTO `tbl_departamento` VALUES ('001DEP','Cundinamarca'),('002DEP','asdasdasd'),('003DEP','PruebaAdmin'),('004DEP','Prueba'),('005DEP','EXITOSA');
/*!40000 ALTER TABLE `tbl_departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_entidad`
--

DROP TABLE IF EXISTS `tbl_entidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_entidad` (
  `Id_entidad` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Nombre_Entidad` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Fk_Incidente` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Fk_Estado` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_entidad`),
  KEY `tbl_entidad_ibfk_1_idx` (`Fk_Incidente`),
  KEY `fk_entidad_estado` (`Fk_Estado`),
  CONSTRAINT `fk_entidad_estado` FOREIGN KEY (`Fk_Estado`) REFERENCES `tbl_estado` (`Id_estado`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `tbl_entidad_ibfk_1` FOREIGN KEY (`Fk_Incidente`) REFERENCES `tbl_incidente` (`Id_incidente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_entidad`
--

LOCK TABLES `tbl_entidad` WRITE;
/*!40000 ALTER TABLE `tbl_entidad` DISABLE KEYS */;
INSERT INTO `tbl_entidad` VALUES ('001ENT','Instituto Geográfico Agustín Codazzi','Despl','Entidad_01'),('002ENT','Ministerio de Justicia y del Derecho','Despo','Entidad_01'),('003ENT','Ministerio de Agricultura y Desarrollo Rural','Expro','Entidad_01'),('004ENT','Unidad de Restitución de Tierras (URT)','Hurt','Entidad_01'),('005ENT','Entidad_Prueba','Despl','Entidad_01');
/*!40000 ALTER TABLE `tbl_entidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_estado`
--

DROP TABLE IF EXISTS `tbl_estado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_estado` (
  `Id_estado` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Estado` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`Id_estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_estado`
--

LOCK TABLES `tbl_estado` WRITE;
/*!40000 ALTER TABLE `tbl_estado` DISABLE KEYS */;
INSERT INTO `tbl_estado` VALUES ('Caso_00','Caso Pendiente'),('Caso_01','Caso Activo'),('Caso_02','Caso Resuelto'),('Caso_03','Caso Eliminado'),('Caso_04','En espera del usuario'),('Caso_05','Escalado a supervisor'),('Caso_06','Caso Reabierto'),('Entidad_00','Entidad Inactiva'),('Entidad_01','Entidad Activa'),('Usuario_00','Usuario Inactivo'),('usuario_01','Usuario Activo');
/*!40000 ALTER TABLE `tbl_estado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_incidente`
--

DROP TABLE IF EXISTS `tbl_incidente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_incidente` (
  `Id_incidente` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Incidente` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fk_prioridad` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_incidente`),
  KEY `fk_prioridad` (`fk_prioridad`),
  CONSTRAINT `tbl_incidente_ibfk_1` FOREIGN KEY (`fk_prioridad`) REFERENCES `tbl_prioridad` (`Id_prioridad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_incidente`
--

LOCK TABLES `tbl_incidente` WRITE;
/*!40000 ALTER TABLE `tbl_incidente` DISABLE KEYS */;
INSERT INTO `tbl_incidente` VALUES ('Despl','Desplazamiento','Nivel4'),('Despo','Predios-Despojados','Nivel3'),('Expro','Expropiacion','Nivel2'),('Hurt','Hurto','Nivel1');
/*!40000 ALTER TABLE `tbl_incidente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_localidad`
--

DROP TABLE IF EXISTS `tbl_localidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_localidad` (
  `Id_local` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Localidad` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fk_ciudad` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_local`),
  KEY `fk_ciudad` (`fk_ciudad`),
  CONSTRAINT `tbl_localidad_ibfk_1` FOREIGN KEY (`fk_ciudad`) REFERENCES `tbl_ciudad` (`Id_ciudad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_localidad`
--

LOCK TABLES `tbl_localidad` WRITE;
/*!40000 ALTER TABLE `tbl_localidad` DISABLE KEYS */;
INSERT INTO `tbl_localidad` VALUES ('001LOC','Rafael Uribe Uribe','001CIU'),('002LOC','Bogota','001CIU'),('003LOC','Prueba','003CIU');
/*!40000 ALTER TABLE `tbl_localidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_num_caso`
--

DROP TABLE IF EXISTS `tbl_num_caso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_num_caso` (
  `Id_num_caso` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Radicado` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Fk_Caso` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_num_caso`),
  KEY `Fk_Caso` (`Fk_Caso`),
  CONSTRAINT `tbl_num_caso_ibfk_1` FOREIGN KEY (`Fk_Caso`) REFERENCES `tbl_caso` (`Id_Caso_Incidente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_num_caso`
--

LOCK TABLES `tbl_num_caso` WRITE;
/*!40000 ALTER TABLE `tbl_num_caso` DISABLE KEYS */;
INSERT INTO `tbl_num_caso` VALUES ('001NUC','000001R','001CAD'),('002NUC','000002R','002CAD'),('003NUC','000003R','003CAD');
/*!40000 ALTER TABLE `tbl_num_caso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_persona`
--

DROP TABLE IF EXISTS `tbl_persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_persona` (
  `Id_Persona` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Pri_Nom` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Seg_Nom` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Pri_Ape` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Seg_Ape` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `fk_Tipo_documento` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Fecha_nacimiento` date NOT NULL,
  `fk_Usuario` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_Persona`),
  KEY `fk_Tipo_documento` (`fk_Tipo_documento`),
  KEY `fk_Usuario` (`fk_Usuario`),
  CONSTRAINT `tbl_persona_ibfk_1` FOREIGN KEY (`fk_Tipo_documento`) REFERENCES `tbl_tipo_documento` (`Id_Documento`),
  CONSTRAINT `tbl_persona_ibfk_2` FOREIGN KEY (`fk_Usuario`) REFERENCES `tbl_usuario` (`Id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_persona`
--

LOCK TABLES `tbl_persona` WRITE;
/*!40000 ALTER TABLE `tbl_persona` DISABLE KEYS */;
INSERT INTO `tbl_persona` VALUES ('00000000','Admin','Admin','Admin','Admin','CC','2000-01-01','000USU'),('1145224601','Exitoso','Exitoso','Exitoso','Exitoso','CC','2007-08-25','002USU'),('123456789','Kevin','Kevin','Garzon','Anzola','PA','2000-11-12','003USU'),('123987465','EXITOSA','EXITOSA','EXITOSA','EXITOSA','RC','2005-06-27','007USU'),('1324354657','Prueba','Prueba','Prueba','Prueba','CC','2000-08-26','006USU'),('192837465','Prueba','Prueba','Prueba','Prueba','CE','2002-01-07','005USU'),('987654321','PruebaAdmin','PruebaAdmin','PruebaAdmin','PruebaAdmin','RC','2007-06-12','004USU');
/*!40000 ALTER TABLE `tbl_persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_prioridad`
--

DROP TABLE IF EXISTS `tbl_prioridad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_prioridad` (
  `Id_prioridad` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Prioridad` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_prioridad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_prioridad`
--

LOCK TABLES `tbl_prioridad` WRITE;
/*!40000 ALTER TABLE `tbl_prioridad` DISABLE KEYS */;
INSERT INTO `tbl_prioridad` VALUES ('Nivel1','Baja'),('Nivel2','Medio_baja'),('Nivel3','Medio_alta'),('Nivel4','Alta');
/*!40000 ALTER TABLE `tbl_prioridad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_rol`
--

DROP TABLE IF EXISTS `tbl_rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_rol` (
  `id_rol` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Rol` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id_rol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_rol`
--

LOCK TABLES `tbl_rol` WRITE;
/*!40000 ALTER TABLE `tbl_rol` DISABLE KEYS */;
INSERT INTO `tbl_rol` VALUES ('Admin','Administrador'),('Usu','Usuario_sistema');
/*!40000 ALTER TABLE `tbl_rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_tipo_caso`
--

DROP TABLE IF EXISTS `tbl_tipo_caso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_tipo_caso` (
  `Id_caso` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Tipo_Caso` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_caso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_tipo_caso`
--

LOCK TABLES `tbl_tipo_caso` WRITE;
/*!40000 ALTER TABLE `tbl_tipo_caso` DISABLE KEYS */;
INSERT INTO `tbl_tipo_caso` VALUES ('Caso','Caso incidente'),('Ticket','Ticket ayuda');
/*!40000 ALTER TABLE `tbl_tipo_caso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_tipo_documento`
--

DROP TABLE IF EXISTS `tbl_tipo_documento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_tipo_documento` (
  `Id_Documento` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Tipo_documento` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_Documento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_tipo_documento`
--

LOCK TABLES `tbl_tipo_documento` WRITE;
/*!40000 ALTER TABLE `tbl_tipo_documento` DISABLE KEYS */;
INSERT INTO `tbl_tipo_documento` VALUES ('CC','Cedula Ciudadania'),('CE','Cedula Extranjeria'),('PA','Pasaporte'),('RC','Registro Civil'),('TI','Tarjeta de identidad');
/*!40000 ALTER TABLE `tbl_tipo_documento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_usuario`
--

DROP TABLE IF EXISTS `tbl_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_usuario` (
  `Id_usuario` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Nombre` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Contraseña` varchar(225) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Creacion` datetime NOT NULL,
  `Bloqueado` varchar(225) COLLATE utf8mb4_general_ci NOT NULL,
  `Intentos_fallidos` int NOT NULL,
  `fk_rol` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fk_estado` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `2FA` tinyint(1) DEFAULT '0',
  `Secret_Key` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`Id_usuario`),
  KEY `fk_estado` (`fk_estado`),
  KEY `fk_rol` (`fk_rol`),
  CONSTRAINT `tbl_usuario_ibfk_1` FOREIGN KEY (`fk_estado`) REFERENCES `tbl_estado` (`Id_estado`),
  CONSTRAINT `tbl_usuario_ibfk_2` FOREIGN KEY (`fk_rol`) REFERENCES `tbl_rol` (`id_rol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_usuario`
--

LOCK TABLES `tbl_usuario` WRITE;
/*!40000 ALTER TABLE `tbl_usuario` DISABLE KEYS */;
INSERT INTO `tbl_usuario` VALUES ('000USU','Admin','scrypt:32768:8:1$IsYCFyCsYm9HZ9nF$e7cd69ca132be8a5dacd23b895e74f96cd516e558658c8bb5216b22e1ff957c4bfed885f038dc3c501c0420d2f2a5416707c04ebe827c91b9d0663a706f67b15','2025-11-03 00:00:00','NO',0,'admin','usuario_01',1,'FKYBFL5L7U3VAGINVULJ2PY2B4QI4ZSQ'),('002USU','PRUEBA','scrypt:32768:8:1$zndSorxFO96cXY2u$132283451b0052e04e571263287f020f21389e63ba3e205f39569e3fc6b7d68cb9f22b0db55d40a97dfe8c2d74a56c91f32d03d7f5eda089e8db6f6cb4bee13c','2025-11-06 00:00:00','NO',1,'admin','usuario_01',0,NULL),('003USU','Pruebas','scrypt:32768:8:1$L50UUNymeoCOdGak$3cc4b8677002fb2be524970b934a0402a72c5198277cef89bd7e2da7b108457e9663718950c358a500c6a2f19d0499b8d8384e032986105c3324091ea2c0c1e9','2025-11-25 12:31:18','NO',0,'Usu','usuario_01',0,NULL),('004USU','Prueba_Admin','scrypt:32768:8:1$l327hhywfQVKG5QW$9bbef3fd2e1812af8fea88fa4a3dc5f2365f72ff28322e25e061a2b4eb71ce90436d17bf323891af52a990a57abdee3a87e8523683b0094b0d747e03253cce4d','2025-11-25 00:00:00','SI',0,'admin','usuario_01',0,NULL),('005USU','Prueba2','scrypt:32768:8:1$rIXZk4lVYf7jpiHg$43156cbf4fd065082e8a2b1366d2a74963af3c83838ba9b5f022fd2f77288abb6d40955edf94eaf8abcedf26893e965237649f7c4d6e965c99a7234072f44efb','2025-11-27 00:00:00','2025-11-28',2,'admin','usuario_01',0,NULL),('006USU','Prueba3','scrypt:32768:8:1$zJnpAjbvLsbCE3s5$4f3686bfb8573bcca1ad42e0be3b0f7c50fdaea8992f2ed8b6b2c2addc118cfefb5aa460df969605f2769ceb56650078109c21790742f1f4863d9ff618b6cc08','2025-11-27 00:00:00','NO',1,'admin','usuario_01',0,NULL),('007USU','EXITOSA1','scrypt:32768:8:1$b1P7MzVdlVddHr7W$f492a0b9c662801e46e4c1e6f7c4b88d09127867cbde839b12ab13f79731ea99c18d724169886a298b85fb2adc1287ff99d43c03f4063f55646cde9c65645989','2025-11-27 00:00:00','SI',0,'Usu','usuario_01',0,NULL);
/*!40000 ALTER TABLE `tbl_usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-09 20:08:34
