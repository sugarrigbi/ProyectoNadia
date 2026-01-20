-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: proyecto
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
-- Table structure for table `tbl_adic_persona`
--

DROP TABLE IF EXISTS `tbl_adic_persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_adic_persona` (
  `Id_Adic_Persona` varchar(20) NOT NULL,
  `Edad` int NOT NULL,
  `Direccion` varchar(20) NOT NULL,
  `Num_Contact` varchar(10) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `fk_persona` varchar(10) NOT NULL,
  PRIMARY KEY (`Id_Adic_Persona`),
  KEY `fk_persona` (`fk_persona`),
  CONSTRAINT `tbl_adic_persona_ibfk_1` FOREIGN KEY (`fk_persona`) REFERENCES `tbl_persona` (`Id_Persona`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_adic_persona`
--

LOCK TABLES `tbl_adic_persona` WRITE;
/*!40000 ALTER TABLE `tbl_adic_persona` DISABLE KEYS */;
INSERT INTO `tbl_adic_persona` VALUES ('10235645-1',20,'cra676','32165','gda@gmail.com','10235645'),('1025-1',45,'cra56','32015','dan@gma','1025'),('102563-1',58,'cra67','320158','danie@gmail','102563'),('120563-1',21,'cra76','32165','dsanm@gmail','120563'),('1225-1',25,'cra56','3158','da@gma','1225'),('13546-1',12,'vd2v','32165','sad@gma','13546');
/*!40000 ALTER TABLE `tbl_adic_persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_barrio`
--

DROP TABLE IF EXISTS `tbl_barrio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_barrio` (
  `Id_barrio` varchar(10) NOT NULL,
  `Barrio` varchar(20) NOT NULL,
  `fk_local` varchar(10) NOT NULL,
  PRIMARY KEY (`Id_barrio`),
  KEY `fk_local` (`fk_local`),
  CONSTRAINT `tbl_barrio_ibfk_1` FOREIGN KEY (`fk_local`) REFERENCES `tbl_localidad` (`Id_local`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_barrio`
--

LOCK TABLES `tbl_barrio` WRITE;
/*!40000 ALTER TABLE `tbl_barrio` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_barrio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_caso`
--

DROP TABLE IF EXISTS `tbl_caso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_caso` (
  `Id_Caso_Desastre` int unsigned NOT NULL AUTO_INCREMENT,
  `Fecha` date NOT NULL,
  `Descripción` text NOT NULL,
  `Personas_Afectadas` int NOT NULL,
  `Fk_Usuario` int unsigned NOT NULL,
  `Fk_Desastre` varchar(10) NOT NULL,
  `Fk_Dep` varchar(10) NOT NULL,
  `Fk_Tipo_Caso` varchar(10) NOT NULL,
  `Fk_Estado` varchar(10) NOT NULL,
  PRIMARY KEY (`Id_Caso_Desastre`),
  KEY `Fk_Usuario` (`Fk_Usuario`),
  KEY `Fk_Desastre` (`Fk_Desastre`),
  KEY `Fk_Dep` (`Fk_Dep`),
  KEY `Fk_Tipo_Caso` (`Fk_Tipo_Caso`),
  KEY `Fk_Estado` (`Fk_Estado`),
  CONSTRAINT `tbl_caso_ibfk_1` FOREIGN KEY (`Fk_Usuario`) REFERENCES `tbl_usuario` (`Id_usuario`),
  CONSTRAINT `tbl_caso_ibfk_2` FOREIGN KEY (`Fk_Desastre`) REFERENCES `tbl_desastre` (`Id_desastre`),
  CONSTRAINT `tbl_caso_ibfk_3` FOREIGN KEY (`Fk_Dep`) REFERENCES `tbl_departamento` (`Id_dep`),
  CONSTRAINT `tbl_caso_ibfk_4` FOREIGN KEY (`Fk_Tipo_Caso`) REFERENCES `tbl_tipo_caso` (`Id_caso`),
  CONSTRAINT `tbl_caso_ibfk_5` FOREIGN KEY (`Fk_Estado`) REFERENCES `tbl_estado` (`Id_estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
  `Id_ciudad` varchar(10) NOT NULL,
  `Nom_ciudad` varchar(20) NOT NULL,
  `Fk_Dep` varchar(10) NOT NULL,
  PRIMARY KEY (`Id_ciudad`),
  KEY `Fk_Dep` (`Fk_Dep`),
  CONSTRAINT `tbl_ciudad_ibfk_1` FOREIGN KEY (`Fk_Dep`) REFERENCES `tbl_departamento` (`Id_dep`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_ciudad`
--

LOCK TABLES `tbl_ciudad` WRITE;
/*!40000 ALTER TABLE `tbl_ciudad` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_ciudad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_departamento`
--

DROP TABLE IF EXISTS `tbl_departamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_departamento` (
  `Id_dep` varchar(10) NOT NULL,
  `Nom_departamento` varchar(15) NOT NULL,
  PRIMARY KEY (`Id_dep`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_departamento`
--

LOCK TABLES `tbl_departamento` WRITE;
/*!40000 ALTER TABLE `tbl_departamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_desastre`
--

DROP TABLE IF EXISTS `tbl_desastre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_desastre` (
  `Id_desastre` varchar(10) NOT NULL,
  `Desastre` varchar(20) NOT NULL,
  `fk_prioridad` varchar(10) NOT NULL,
  PRIMARY KEY (`Id_desastre`),
  KEY `fk_prioridad` (`fk_prioridad`),
  CONSTRAINT `tbl_desastre_ibfk_1` FOREIGN KEY (`fk_prioridad`) REFERENCES `tbl_prioridad` (`Id_prioridad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_desastre`
--

LOCK TABLES `tbl_desastre` WRITE;
/*!40000 ALTER TABLE `tbl_desastre` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_desastre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_entidad`
--

DROP TABLE IF EXISTS `tbl_entidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_entidad` (
  `Id_entidad` varchar(10) NOT NULL,
  `Nombre_Entidad` varchar(50) NOT NULL,
  `Descripción` text NOT NULL,
  `fk_desastre` varchar(10) NOT NULL,
  PRIMARY KEY (`Id_entidad`),
  KEY `fk_desastre` (`fk_desastre`),
  CONSTRAINT `tbl_entidad_ibfk_1` FOREIGN KEY (`fk_desastre`) REFERENCES `tbl_desastre` (`Id_desastre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_entidad`
--

LOCK TABLES `tbl_entidad` WRITE;
/*!40000 ALTER TABLE `tbl_entidad` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_entidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_estado`
--

DROP TABLE IF EXISTS `tbl_estado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_estado` (
  `Id_estado` varchar(10) NOT NULL,
  `Estado` varchar(20) NOT NULL,
  PRIMARY KEY (`Id_estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_estado`
--

LOCK TABLES `tbl_estado` WRITE;
/*!40000 ALTER TABLE `tbl_estado` DISABLE KEYS */;
INSERT INTO `tbl_estado` VALUES ('00','Inactivo'),('01','Activo'),('P','pendiente');
/*!40000 ALTER TABLE `tbl_estado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_localidad`
--

DROP TABLE IF EXISTS `tbl_localidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_localidad` (
  `Id_local` varchar(10) NOT NULL,
  `Localidad` varchar(20) NOT NULL,
  `fk_ciudad` varchar(10) NOT NULL,
  PRIMARY KEY (`Id_local`),
  KEY `fk_ciudad` (`fk_ciudad`),
  CONSTRAINT `tbl_localidad_ibfk_1` FOREIGN KEY (`fk_ciudad`) REFERENCES `tbl_ciudad` (`Id_ciudad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_localidad`
--

LOCK TABLES `tbl_localidad` WRITE;
/*!40000 ALTER TABLE `tbl_localidad` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_localidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_num_caso`
--

DROP TABLE IF EXISTS `tbl_num_caso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_num_caso` (
  `Id_num_caso` int unsigned NOT NULL AUTO_INCREMENT,
  `Radicado` varchar(20) DEFAULT NULL,
  `Fk_Caso` int unsigned NOT NULL,
  PRIMARY KEY (`Id_num_caso`),
  KEY `Fk_Caso` (`Fk_Caso`),
  CONSTRAINT `tbl_num_caso_ibfk_1` FOREIGN KEY (`Fk_Caso`) REFERENCES `tbl_caso` (`Id_Caso_Desastre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
  `Id_Persona` varchar(10) NOT NULL,
  `Pri_Nom` varchar(10) NOT NULL,
  `Seg_Nom` varchar(10) NOT NULL,
  `Pri_Ape` varchar(10) NOT NULL,
  `Seg_Ape` varchar(10) NOT NULL,
  `fk_Tipo_documento` varchar(10) NOT NULL,
  `Fecha_nacimiento` date NOT NULL,
  `fk_Usuario` int unsigned NOT NULL,
  PRIMARY KEY (`Id_Persona`),
  KEY `fk_Tipo_documento` (`fk_Tipo_documento`),
  KEY `fk_Usuario` (`fk_Usuario`),
  CONSTRAINT `tbl_persona_ibfk_1` FOREIGN KEY (`fk_Tipo_documento`) REFERENCES `tbl_tipo_documento` (`Id_Documento`),
  CONSTRAINT `tbl_persona_ibfk_2` FOREIGN KEY (`fk_Usuario`) REFERENCES `tbl_usuario` (`Id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_persona`
--

LOCK TABLES `tbl_persona` WRITE;
/*!40000 ALTER TABLE `tbl_persona` DISABLE KEYS */;
INSERT INTO `tbl_persona` VALUES ('10235645','sebas','fg','sfg','sfg','CC','2009-05-12',12),('1025','juan','die','tru','sa','CC','2008-08-15',8),('120563','seb','hg','sg','df','CC','2009-05-12',10),('13546','sf','d','sd','sd','CC','2009-05-12',11);
/*!40000 ALTER TABLE `tbl_persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_prioridad`
--

DROP TABLE IF EXISTS `tbl_prioridad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_prioridad` (
  `Id_prioridad` varchar(10) NOT NULL,
  `Prioridad` varchar(10) NOT NULL,
  PRIMARY KEY (`Id_prioridad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_prioridad`
--

LOCK TABLES `tbl_prioridad` WRITE;
/*!40000 ALTER TABLE `tbl_prioridad` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_prioridad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_rol`
--

DROP TABLE IF EXISTS `tbl_rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_rol` (
  `id_rol` varchar(10) NOT NULL,
  `Rol` varchar(15) NOT NULL,
  PRIMARY KEY (`id_rol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_rol`
--

LOCK TABLES `tbl_rol` WRITE;
/*!40000 ALTER TABLE `tbl_rol` DISABLE KEYS */;
INSERT INTO `tbl_rol` VALUES ('Admin','Administrador'),('User','Usuario');
/*!40000 ALTER TABLE `tbl_rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_ticket`
--

DROP TABLE IF EXISTS `tbl_ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_ticket` (
  `Id_Ticket` int unsigned NOT NULL AUTO_INCREMENT,
  `Descripción` text NOT NULL,
  `fk_usuario` int unsigned NOT NULL,
  `fk_tipo_caso` varchar(10) NOT NULL,
  `Fk_Estado` varchar(10) NOT NULL,
  PRIMARY KEY (`Id_Ticket`),
  KEY `fk_usuario` (`fk_usuario`),
  KEY `fk_tipo_caso` (`fk_tipo_caso`),
  KEY `Fk_Estado` (`Fk_Estado`),
  CONSTRAINT `tbl_ticket_ibfk_1` FOREIGN KEY (`fk_usuario`) REFERENCES `tbl_usuario` (`Id_usuario`),
  CONSTRAINT `tbl_ticket_ibfk_2` FOREIGN KEY (`fk_tipo_caso`) REFERENCES `tbl_tipo_caso` (`Id_caso`),
  CONSTRAINT `tbl_ticket_ibfk_3` FOREIGN KEY (`Fk_Estado`) REFERENCES `tbl_estado` (`Id_estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
  `Id_caso` varchar(10) NOT NULL,
  `Tipo_Caso` varchar(20) NOT NULL,
  PRIMARY KEY (`Id_caso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_tipo_caso`
--

LOCK TABLES `tbl_tipo_caso` WRITE;
/*!40000 ALTER TABLE `tbl_tipo_caso` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_tipo_caso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_tipo_documento`
--

DROP TABLE IF EXISTS `tbl_tipo_documento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_tipo_documento` (
  `Id_Documento` varchar(10) NOT NULL,
  `Tipo_documento` varchar(20) NOT NULL,
  PRIMARY KEY (`Id_Documento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_tipo_documento`
--

LOCK TABLES `tbl_tipo_documento` WRITE;
/*!40000 ALTER TABLE `tbl_tipo_documento` DISABLE KEYS */;
INSERT INTO `tbl_tipo_documento` VALUES ('CC','Cedula Ciudadania'),('CE','Cedula Extranjeria'),('PA','Pasaporte'),('TI','Tarjeta de identidad');
/*!40000 ALTER TABLE `tbl_tipo_documento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_usuario`
--

DROP TABLE IF EXISTS `tbl_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_usuario` (
  `Id_usuario` int unsigned NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(10) NOT NULL,
  `Contraseña` varchar(15) NOT NULL,
  `fk_rol` varchar(10) NOT NULL,
  `fk_estado` varchar(10) NOT NULL,
  PRIMARY KEY (`Id_usuario`),
  UNIQUE KEY `Nombre` (`Nombre`),
  KEY `fk_rol` (`fk_rol`),
  KEY `fk_estado` (`fk_estado`),
  CONSTRAINT `tbl_usuario_ibfk_1` FOREIGN KEY (`fk_rol`) REFERENCES `tbl_rol` (`id_rol`),
  CONSTRAINT `tbl_usuario_ibfk_2` FOREIGN KEY (`fk_estado`) REFERENCES `tbl_estado` (`Id_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_usuario`
--

LOCK TABLES `tbl_usuario` WRITE;
/*!40000 ALTER TABLE `tbl_usuario` DISABLE KEYS */;
INSERT INTO `tbl_usuario` VALUES (1,'Karoll','1234*','Admin','01'),(8,'Juan','123','User','01'),(10,'Sebas','12345*','User','01'),(11,'Diego','234','User','01'),(12,'sebastian','12345*','User','01');
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

-- Dump completed on 2025-09-26 16:00:32
