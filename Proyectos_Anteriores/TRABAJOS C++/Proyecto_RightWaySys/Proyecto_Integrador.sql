-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: proyecto
-- ------------------------------------------------------
-- Server version	8.0.42

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
  `Direccion` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Num_Contact` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `web_site` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Descripción` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fk_entidad` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_Adic_Entidad`),
  KEY `fk_entidad` (`fk_entidad`),
  CONSTRAINT `tbl_adic_entidad_ibfk_1` FOREIGN KEY (`fk_entidad`) REFERENCES `tbl_entidad` (`Id_entidad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_adic_entidad`
--

LOCK TABLES `tbl_adic_entidad` WRITE;
/*!40000 ALTER TABLE `tbl_adic_entidad` DISABLE KEYS */;
INSERT INTO `tbl_adic_entidad` VALUES ('001ENA','Dg sapo','3209813135','www.sapo.com','No','001ENT'),('002ENA','Dg gato','3144048151','www.gato.com','Sea','002ENT'),('003ENA','Dg perro','3228547454','www.perro.com','Sapo','003ENT'),('004ENA','Dg ave','3126988596','www.ave.com','Perro','004ENT');
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
  `fk_dir` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
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
INSERT INTO `tbl_adic_persona` VALUES ('001PAD',17,'Bogota','3144048151','Sugarrigbi@gmail.com','1145224601','001BAR');
/*!40000 ALTER TABLE `tbl_adic_persona` ENABLE KEYS */;
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
INSERT INTO `tbl_barrio` VALUES ('001BAR','Bogota','001LOC');
/*!40000 ALTER TABLE `tbl_barrio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_caso`
--

DROP TABLE IF EXISTS `tbl_caso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_caso` (
  `Id_Caso_Desastre` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Fecha` date NOT NULL,
  `Descripción` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Personas_Afectadas` int NOT NULL,
  `Fk_Usuario` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Fk_incidente` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Fk_Dep` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Fk_Tipo_Caso` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Fk_Estado` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_Caso_Desastre`),
  KEY `Fk_Usuario` (`Fk_Usuario`),
  KEY `Fk_Desastre` (`Fk_incidente`),
  KEY `Fk_Dep` (`Fk_Dep`),
  KEY `Fk_Estado` (`Fk_Estado`),
  KEY `Fk_Tipo_Caso` (`Fk_Tipo_Caso`),
  CONSTRAINT `tbl_caso_ibfk_1` FOREIGN KEY (`Fk_Usuario`) REFERENCES `tbl_usuario` (`Id_usuario`),
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
INSERT INTO `tbl_ciudad` VALUES ('001CIU','Bogota','001DEP');
/*!40000 ALTER TABLE `tbl_ciudad` ENABLE KEYS */;
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
INSERT INTO `tbl_departamento` VALUES ('001DEP','Cundinamarca');
/*!40000 ALTER TABLE `tbl_departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_desastre`
--

DROP TABLE IF EXISTS `tbl_desastre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_desastre` (
  `Id_desastre` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Desastre` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fk_prioridad` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_desastre`),
  KEY `fk_prioridad` (`fk_prioridad`),
  CONSTRAINT `tbl_desastre_ibfk_1` FOREIGN KEY (`fk_prioridad`) REFERENCES `tbl_prioridad` (`Id_prioridad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_desastre`
--

LOCK TABLES `tbl_desastre` WRITE;
/*!40000 ALTER TABLE `tbl_desastre` DISABLE KEYS */;
INSERT INTO `tbl_desastre` VALUES ('Incen','Incendio','Nivel3'),('Inund','Inundaciòn','Nivel3'),('Sismo','Sismo-temblor','Nivel1'),('Terre','Terremoto','Nivel4');
/*!40000 ALTER TABLE `tbl_desastre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_entidad`
--

DROP TABLE IF EXISTS `tbl_entidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_entidad` (
  `Id_entidad` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Nombre_Entidad` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Descripción` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fk_desastre` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_entidad`),
  KEY `fk_desastre` (`fk_desastre`),
  CONSTRAINT `tbl_entidad_ibfk_1` FOREIGN KEY (`fk_desastre`) REFERENCES `tbl_desastre` (`Id_desastre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_entidad`
--

LOCK TABLES `tbl_entidad` WRITE;
/*!40000 ALTER TABLE `tbl_entidad` DISABLE KEYS */;
INSERT INTO `tbl_entidad` VALUES ('001ENT','Cruz roja Colombiana \n','Cruz Roja','Terre'),('002ENT','Dirección Nacional de bomberos\n','Bomberos','Incen'),('003ENT','linea de emergencia de cundinamarca','Emergencias','Inund'),('004ENT','Ministerio de Justicia y del derecho','Justicia','Sismo');
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
  `Estado` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_estado`
--

LOCK TABLES `tbl_estado` WRITE;
/*!40000 ALTER TABLE `tbl_estado` DISABLE KEYS */;
INSERT INTO `tbl_estado` VALUES ('Caso_00','Caso Pendiente'),('Caso_01','Caso Activo'),('Caso_02','Caso Finalizado'),('Caso_03','Caso Eliminado'),('Usuario_00','Usuario Inactivo'),('usuario_01','Usuario Activo');
/*!40000 ALTER TABLE `tbl_estado` ENABLE KEYS */;
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
INSERT INTO `tbl_localidad` VALUES ('001LOC','Bogota','001CIU');
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
  CONSTRAINT `tbl_num_caso_ibfk_1` FOREIGN KEY (`Fk_Caso`) REFERENCES `tbl_caso` (`Id_Caso_Desastre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_num_caso`
--

LOCK TABLES `tbl_num_caso` WRITE;
/*!40000 ALTER TABLE `tbl_num_caso` DISABLE KEYS */;
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
  `Pri_Nom` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Seg_Nom` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Pri_Ape` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Seg_Ape` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
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
INSERT INTO `tbl_persona` VALUES ('1145224601','Kevin','Mauricio','Anzola','Garzon','CC','2007-08-26','001USU');
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
-- Table structure for table `tbl_ticket`
--

DROP TABLE IF EXISTS `tbl_ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_ticket` (
  `Id_Ticket` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Descripción` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fk_usuario` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fk_tipo_caso` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Fk_Estado` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_Ticket`),
  KEY `fk_usuario` (`fk_usuario`),
  KEY `fk_tipo_caso` (`fk_tipo_caso`),
  KEY `Fk_Estado` (`Fk_Estado`),
  CONSTRAINT `tbl_ticket_ibfk_1` FOREIGN KEY (`fk_usuario`) REFERENCES `tbl_usuario` (`Id_usuario`),
  CONSTRAINT `tbl_ticket_ibfk_2` FOREIGN KEY (`fk_tipo_caso`) REFERENCES `tbl_tipo_caso` (`Id_caso`),
  CONSTRAINT `tbl_ticket_ibfk_3` FOREIGN KEY (`Fk_Estado`) REFERENCES `tbl_estado` (`Id_estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_ticket`
--

LOCK TABLES `tbl_ticket` WRITE;
/*!40000 ALTER TABLE `tbl_ticket` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_ticket` ENABLE KEYS */;
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
INSERT INTO `tbl_tipo_caso` VALUES ('Caso','Caso'),('Ticket','Ticket ayuda');
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
  `Nombre` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Contraseña` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fk_rol` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fk_estado` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
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
INSERT INTO `tbl_usuario` VALUES ('001USU','Sugar','1','Admin','usuario_01');
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

-- Dump completed on 2025-05-21 18:41:30
-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: prueba
-- ------------------------------------------------------
-- Server version	8.0.42

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
  `Direccion` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Num_Contact` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `web_site` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `Descripción` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fk_entidad` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_Adic_Entidad`),
  KEY `fk_entidad` (`fk_entidad`),
  CONSTRAINT `tbl_adic_entidad_ibfk_1` FOREIGN KEY (`fk_entidad`) REFERENCES `tbl_entidad` (`Id_entidad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_adic_entidad`
--

LOCK TABLES `tbl_adic_entidad` WRITE;
/*!40000 ALTER TABLE `tbl_adic_entidad` DISABLE KEYS */;
INSERT INTO `tbl_adic_entidad` VALUES ('001ENA',' Avenida Carrera 30 #48-51','(601) 653 1888','http://www.igac.gov.co','es la autoridad nacional de cartografia que realiza el mapa oficial de Colombia la cual elabora el catastro nacional','001ENT'),('002ENA','Carrera 13 N° 52-95','01-8000-911-170','http://www.minjusticia.gov.co','es el organismo encargado de formular políticas públicas relacionadas con el ordenamiento jurídico, la lucha contra la criminalidad, y la promoción de la legalidad en colombia','002ENT'),('003ENA','Carrera 7 No. 32 – 42','01-8000-119-450','http://www.minagricultura.gov.co','ministerio que formula políticas para el desarrollo del sector rural buscando mejora la seguridad y el bienestar de las comunidades rurales además de liderar iniciativas de reformas agrarias','003ENT'),('004ENA','Carrera 10 No. 27-51','(601) 341 2073','http://www.urt.gov.co','entidad que trabaja con el Ministerio de Agricultura , la cual lidera el proceso de restitución de tierras a victimas del despojo y abandono forzado, en el marco de la Ley de Víctimas y Restitución de Tierras.','004ENT');
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
  `fk_dir` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
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
INSERT INTO `tbl_adic_persona` VALUES ('001PAD',17,'Dg 49 sur','3144048152','Sugarrigbi@gmail.com','1145224601','001BAR'),('002PAD',15,'Admin','1234567891','admin@gmial.com','123456789','002BAR');
/*!40000 ALTER TABLE `tbl_adic_persona` ENABLE KEYS */;
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
INSERT INTO `tbl_barrio` VALUES ('001BAR','Santa lucia','001LOC'),('002BAR','Admin','002LOC');
/*!40000 ALTER TABLE `tbl_barrio` ENABLE KEYS */;
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
INSERT INTO `tbl_caso` VALUES ('001CAD','2009-11-11','sapo',4,'001USU','Hurt','001DEP','Caso','Caso_00'),('002CAD','2009-11-11','asd',2,'002USU','Hurt','001DEP','Caso','Caso_03');
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
INSERT INTO `tbl_ciudad` VALUES ('001CIU','Bogota','001DEP'),('002CIU','Admin','001DEP');
/*!40000 ALTER TABLE `tbl_ciudad` ENABLE KEYS */;
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
INSERT INTO `tbl_departamento` VALUES ('001DEP','Cundinamarca');
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
  `Nombre_Entidad` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Descripción` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Fk_Incidente` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_entidad`),
  KEY `Fk_Incidente` (`Fk_Incidente`),
  CONSTRAINT `tbl_entidad_ibfk_1` FOREIGN KEY (`Fk_Incidente`) REFERENCES `tbl_incidente` (`Id_incidente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_entidad`
--

LOCK TABLES `tbl_entidad` WRITE;
/*!40000 ALTER TABLE `tbl_entidad` DISABLE KEYS */;
INSERT INTO `tbl_entidad` VALUES ('001ENT','Instituto Geográfico Agustín Codazzi','Instituto Geográfico Agustín Codazzi','Despl'),('002ENT','Ministerio de Justicia y del Derecho','Ministerio de Justicia y del Derecho','Despo'),('003ENT','Ministerio de Agricultura y Desarrollo Rural','Ministerio de Agricultura y Desarrollo Rural','Expro'),('004ENT','Unidad de Restitución de Tierras (URT)','Unidad de Restitución de Tierras (URT)','Hurt');
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
  `Estado` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_estado`
--

LOCK TABLES `tbl_estado` WRITE;
/*!40000 ALTER TABLE `tbl_estado` DISABLE KEYS */;
INSERT INTO `tbl_estado` VALUES ('Caso_00','Caso Pendiente'),('Caso_01','Caso Activo'),('Caso_02','Caso Finalizado'),('Caso_03','Caso Eliminado'),('Usuario_00','Usuario Inactivo'),('usuario_01','Usuario Activo');
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
INSERT INTO `tbl_localidad` VALUES ('001LOC','Rafael uribe uribe','001CIU'),('002LOC','Admin','002CIU');
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
INSERT INTO `tbl_num_caso` VALUES ('001NUC','000001R','001CAD'),('002NUC','000002R','002CAD');
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
  `Pri_Nom` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Seg_Nom` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Pri_Ape` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Seg_Ape` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
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
INSERT INTO `tbl_persona` VALUES ('1145224601','Kevin','Mauricio','Anzola','Garzon','CC','2007-08-26','001USU'),('123456789','Admin','Admin','Admin','Admin','CC','2009-11-11','002USU');
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
-- Table structure for table `tbl_ticket`
--

DROP TABLE IF EXISTS `tbl_ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_ticket` (
  `Id_Ticket` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Descripción` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fk_usuario` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fk_tipo_caso` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Fk_Estado` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Id_Ticket`),
  KEY `fk_usuario` (`fk_usuario`),
  KEY `fk_tipo_caso` (`fk_tipo_caso`),
  KEY `Fk_Estado` (`Fk_Estado`),
  CONSTRAINT `tbl_ticket_ibfk_1` FOREIGN KEY (`fk_usuario`) REFERENCES `tbl_usuario` (`Id_usuario`),
  CONSTRAINT `tbl_ticket_ibfk_2` FOREIGN KEY (`fk_tipo_caso`) REFERENCES `tbl_tipo_caso` (`Id_caso`),
  CONSTRAINT `tbl_ticket_ibfk_3` FOREIGN KEY (`Fk_Estado`) REFERENCES `tbl_estado` (`Id_estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_ticket`
--

LOCK TABLES `tbl_ticket` WRITE;
/*!40000 ALTER TABLE `tbl_ticket` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_ticket` ENABLE KEYS */;
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
  `Nombre` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Contraseña` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fk_rol` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `fk_estado` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
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
INSERT INTO `tbl_usuario` VALUES ('001USU','Sugar','Holaperro8*','Usu','usuario_01'),('002USU','Admin','Admin','Admin','usuario_01');
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

-- Dump completed on 2025-05-21 18:41:30
