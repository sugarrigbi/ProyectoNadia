-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: gaialink
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
-- Table structure for table `ayuda`
--

DROP TABLE IF EXISTS `ayuda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ayuda` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Correo` varchar(200) NOT NULL,
  `Soporte` varchar(255) NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  `Tipo_Formulario_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Tipo_Formulario_ID` (`Tipo_Formulario_ID`),
  CONSTRAINT `Fk_Ayuda_Tipo_Formulario_ID` FOREIGN KEY (`Tipo_Formulario_ID`) REFERENCES `tipo_formulario` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ayuda`
--

LOCK TABLES `ayuda` WRITE;
/*!40000 ALTER TABLE `ayuda` DISABLE KEYS */;
INSERT INTO `ayuda` VALUES (1,'Sugarrigbi','Sugarrigbi@gmail.com','Problemas con la aplicación móvil','2026-03-18 03:38:54',2);
/*!40000 ALTER TABLE `ayuda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `barrio`
--

DROP TABLE IF EXISTS `barrio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `barrio` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(70) NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  `Localidad_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `UQ_Nombre_LocalidadID` (`Nombre`,`Localidad_ID`),
  KEY `Localidad_ID` (`Localidad_ID`),
  CONSTRAINT `Fk_Localidad_ID` FOREIGN KEY (`Localidad_ID`) REFERENCES `localidad` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `barrio`
--

LOCK TABLES `barrio` WRITE;
/*!40000 ALTER TABLE `barrio` DISABLE KEYS */;
INSERT INTO `barrio` VALUES (1,'Santa Lucia','2026-03-18 03:38:54',1),(2,'BarrioX','2026-03-20 15:50:24',1),(3,'Las mercedez','2026-03-21 03:13:20',1),(4,'Porvenir','2026-03-21 03:14:59',4),(5,'Recreo','2026-03-21 03:15:19',4),(6,'Suba','2026-03-21 17:38:39',6),(7,'Lologro','2026-03-23 00:20:04',9),(8,'Asdas','2026-03-26 03:16:17',10);
/*!40000 ALTER TABLE `barrio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `calificanos`
--

DROP TABLE IF EXISTS `calificanos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `calificanos` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Pregunta1` varchar(100) NOT NULL,
  `Pregunta2` varchar(100) NOT NULL,
  `Pregunta3` varchar(100) NOT NULL,
  `Pregunta4` varchar(100) NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  `Tipo_Formulario_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Tipo_Formulario_ID` (`Tipo_Formulario_ID`),
  CONSTRAINT `Fk_Calificanos_Tipo_Formulario_ID` FOREIGN KEY (`Tipo_Formulario_ID`) REFERENCES `tipo_formulario` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calificanos`
--

LOCK TABLES `calificanos` WRITE;
/*!40000 ALTER TABLE `calificanos` DISABLE KEYS */;
INSERT INTO `calificanos` VALUES (1,'Admin1_1','Admin1_2','Admin1_3','Admin1_4','2026-03-18 03:38:54',1);
/*!40000 ALTER TABLE `calificanos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `caso`
--

DROP TABLE IF EXISTS `caso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caso` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Creacion` datetime DEFAULT CURRENT_TIMESTAMP,
  `Nombre` varchar(100) NOT NULL,
  `Descripcion` varchar(255) NOT NULL,
  `Afectados` int NOT NULL,
  `Direccion` varchar(60) NOT NULL,
  `Caso_Asociado` varchar(10) NOT NULL DEFAULT 'SI',
  `Actualizado_En` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Usuario_Creador_ID` int NOT NULL,
  `Usuario_Asociado_ID` int NOT NULL,
  `Incidente_ID` int NOT NULL,
  `Estado_Caso_ID` int NOT NULL,
  `Prioridad_ID` int NOT NULL,
  `Barrio_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Usuario_Creador_ID` (`Usuario_Creador_ID`),
  KEY `Usuario_Asociado_ID` (`Usuario_Asociado_ID`),
  KEY `Incidente_ID` (`Incidente_ID`),
  KEY `Estado_Caso_ID` (`Estado_Caso_ID`),
  KEY `Prioridad_ID` (`Prioridad_ID`),
  KEY `Barrio_ID` (`Barrio_ID`),
  CONSTRAINT `Fk_Barrio_Caso_ID` FOREIGN KEY (`Barrio_ID`) REFERENCES `barrio` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Fk_Estado_Caso_ID` FOREIGN KEY (`Estado_Caso_ID`) REFERENCES `estado_caso` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Fk_Incidente_Caso_ID` FOREIGN KEY (`Incidente_ID`) REFERENCES `incidente` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Fk_Prioridad_Caso_ID` FOREIGN KEY (`Prioridad_ID`) REFERENCES `prioridad` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Fk_Usuario_Asociado_ID` FOREIGN KEY (`Usuario_Asociado_ID`) REFERENCES `usuario` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Fk_Usuario_Creador_ID` FOREIGN KEY (`Usuario_Creador_ID`) REFERENCES `usuario` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caso`
--

LOCK TABLES `caso` WRITE;
/*!40000 ALTER TABLE `caso` DISABLE KEYS */;
INSERT INTO `caso` VALUES (1,'2007-08-26 00:00:00','CASO ACTIVO 1','Caso principal MODIFICADO con dos asociados',90,'#sa','SI','2026-03-26 15:42:19',1,1,3,2,3,4),(2,'2026-03-18 03:38:54','Caso2','Caso asociado 1',5,'Calle 8 #12-30','SI','2026-03-23 20:42:00',2,1,1,1,2,1),(3,'2026-03-18 03:38:54','Caso3','Caso asociado 2',7,'Avenida 20 #25-40','SI','2026-03-24 20:32:56',1,1,1,1,3,1),(4,'2026-03-18 03:38:54','Caso4','Caso del mismo usuario 1',12,'Calle 50 #60-70','SI','2026-03-24 20:32:56',1,1,2,6,4,1),(5,'2026-03-18 03:38:54','Caso5','Caso del mismo usuario 2',15,'Carrera 15 #20-25','SI','2026-03-24 20:32:56',1,1,2,5,5,1),(6,'2026-03-18 03:38:54','Caso6','Caso del mismo usuario 3',20,'Diagonal 30 #40-50','SI','2026-03-24 20:32:56',1,2,2,5,5,1),(7,'2026-03-18 03:38:54','Caso7','Caso independiente sin asociados',8,'Transversal 12 #34-56','SI','2026-03-24 20:32:56',1,2,3,4,3,1),(13,'2026-03-22 00:00:00','CASO CREADO POR FRONT','CASO CREADO POR FRONT',69,'Dg sapo','SI','2026-03-24 20:32:56',4,2,3,4,4,6),(14,'2026-03-23 00:00:00','CASO CREADO POR FRONT','CASO CREADO POR FRONT',9,'Dg sapo','SI','2026-03-24 20:32:56',2,2,3,3,1,7),(15,'2026-03-23 00:00:00','CASO ACTIVO 2','Caso creado por html',79,'SAPO23','SI','2026-03-24 20:32:56',4,1,4,2,3,4),(16,'2026-03-23 00:00:00','CASO CREADO POR FRONT','sadasd',4,'Dg sapo','SI','2026-03-24 20:32:56',2,1,2,3,3,4),(17,'2026-03-26 00:00:00','Caso creado por html','kbkjbvkjv',143,'Diagonal 42 Sur 24B','SI','2026-03-26 16:27:24',2,2,1,4,3,8),(18,'2026-03-26 00:00:00','CASO CREADO POR JWT','CASO CREADO POR JWT',21,'Diagonal 42 Sur 24B','SI',NULL,2,4,1,2,2,7);
/*!40000 ALTER TABLE `caso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `caso_auditoria`
--

DROP TABLE IF EXISTS `caso_auditoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caso_auditoria` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Accion` varchar(100) NOT NULL,
  `Anterior` text,
  `Modificado_Por` int NOT NULL,
  `Fecha_Modificacion` datetime DEFAULT CURRENT_TIMESTAMP,
  `Caso_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Caso_ID` (`Caso_ID`),
  KEY `Modificado_Por` (`Modificado_Por`),
  CONSTRAINT `Fk_Caso_Auditoria_ID` FOREIGN KEY (`Caso_ID`) REFERENCES `caso` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Fk_Caso_Modificado_Por` FOREIGN KEY (`Modificado_Por`) REFERENCES `usuario` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caso_auditoria`
--

LOCK TABLES `caso_auditoria` WRITE;
/*!40000 ALTER TABLE `caso_auditoria` DISABLE KEYS */;
INSERT INTO `caso_auditoria` VALUES (13,'Caso modificado','{\"ID\": 1, \"Creacion\": \"2007-08-26T00:00:00\", \"Nombre\": \"Caso Modificado por HTML\", \"Descripcion\": \"Caso principal MODIFICADO con dos asociados\", \"Afectados\": 90, \"Direccion\": \"#sa\", \"Caso_Asociado\": \"SI\", \"Actualizado_En\": \"2026-03-21T14:47:54\", \"Usuario_Creador_ID\": 2, \"Usuario_Asociado_ID\": 2, \"Incidente_ID\": 3, \"Estado_Caso_ID\": 3, \"Prioridad_ID\": 3, \"Barrio_ID\": 4, \"usuario_creador\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"usuario_asociado\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"incidente\": {\"ID\": 3, \"Incidente\": \"Expropiacion\", \"Prioridad_ID\": 4}, \"estado\": {\"ID\": 3, \"Nombre\": \"Resuelto\", \"Creado_En\": \"2026-03-18T03:38:54\"}, \"prioridad\": {\"ID\": 3, \"Prioridad\": \"Media\"}, \"barrio\": {\"ID\": 4, \"Nombre\": \"Porvenir\", \"Localidad\": {\"ID\": 4, \"Nombre\": \"Bosa\", \"Ciudad\": {\"ID\": 1, \"Nombre\": \"Bogota\", \"Departamento\": {\"ID\": 1, \"Nombre\": \"Bogota D.C\"}}}}, \"auditorias\": [], \"radicados\": [{\"ID\": 1, \"Radicado\": \"000001R\", \"Caso_ID\": 1}], \"discusiones\": [{\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 1, \"Mensaje\": \"Este caso requiere seguimiento inmediato.\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 2, \"Mensaje\": \"Se notificó al usuario sobre el cambio de estado.\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-20 10:06:06\", \"ID\": 8, \"Mensaje\": \"Esto quedo una chimba\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:14\", \"ID\": 9, \"Mensaje\": \"PERRITO LO LOGRASTE\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:41\", \"ID\": 10, \"Mensaje\": \"UST ES UN DURO\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 11:32:02\", \"ID\": 11, \"Mensaje\": \"asd\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:42:05\", \"ID\": 13, \"Mensaje\": \"asd\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:46:17\", \"ID\": 14, \"Mensaje\": \"Steven mlp\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:47:55\", \"ID\": 15, \"Mensaje\": \"perrito ust es un mk\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}], \"casos_asociados\": [{\"ID\": 1, \"Caso_Principal_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"Caso_Asociado_ID\": {\"ID\": 2, \"Radicado\": \"000002R\", \"Nombre\": \"Caso2\", \"Actualizado\": \"2026-03-18 18:55:37\", \"Estado\": \"Escalado a supervisor\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}, {\"ID\": 2, \"Caso_Principal_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"Caso_Asociado_ID\": {\"ID\": 3, \"Radicado\": \"000003R\", \"Nombre\": \"Caso3\", \"Actualizado\": \"2026-03-18 18:55:37\", \"Estado\": \"Pendiente\"}, \"Tipo_Relacion_ID\": \"Duplicado\", \"Tipo_Relacion_ID_ID\": 2}], \"casos_principales\": []}',1,'2026-03-21 20:34:50',1),(14,'Relacion Eliminada','{\"ID\": 1, \"Creacion\": \"2007-08-26T00:00:00\", \"Nombre\": \"Caso Modificado por HTML\", \"Descripcion\": \"Caso principal MODIFICADO con dos asociados\", \"Afectados\": 90, \"Direccion\": \"#sa\", \"Caso_Asociado\": \"SI\", \"Actualizado_En\": \"2026-03-21T16:04:38\", \"Usuario_Creador_ID\": 1, \"Usuario_Asociado_ID\": 2, \"Incidente_ID\": 3, \"Estado_Caso_ID\": 3, \"Prioridad_ID\": 3, \"Barrio_ID\": 4, \"usuario_creador\": {\"ID\": 1, \"Nombre\": \"Administrador\", \"Correo\": \"Administrador@gaialink.online\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 1, \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, \"usuario_asociado\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"incidente\": {\"ID\": 3, \"Incidente\": \"Expropiacion\", \"Prioridad_ID\": 4}, \"estado\": {\"ID\": 3, \"Nombre\": \"Resuelto\", \"Creado_En\": \"2026-03-18T03:38:54\"}, \"prioridad\": {\"ID\": 3, \"Prioridad\": \"Media\"}, \"barrio\": {\"ID\": 4, \"Nombre\": \"Porvenir\", \"Localidad\": {\"ID\": 4, \"Nombre\": \"Bosa\", \"Ciudad\": {\"ID\": 1, \"Nombre\": \"Bogota\", \"Departamento\": {\"ID\": 1, \"Nombre\": \"Bogota D.C\"}}}}, \"auditorias\": [{\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:34:50\", \"ID\": 13, \"Modificado_Por\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Accion\": \"Relacion Eliminada\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:35:39\", \"ID\": 14, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso eliminado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:35:57\", \"ID\": 15, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:44:55\", \"ID\": 16, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:45:09\", \"ID\": 17, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:46:52\", \"ID\": 18, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:48:13\", \"ID\": 19, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 21:04:39\", \"ID\": 20, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}], \"radicados\": [{\"ID\": 1, \"Radicado\": \"000001R\", \"Caso_ID\": 1}], \"discusiones\": [{\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 1, \"Mensaje\": \"Este caso requiere seguimiento inmediato.\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 2, \"Mensaje\": \"Se notificó al usuario sobre el cambio de estado.\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-20 10:06:06\", \"ID\": 8, \"Mensaje\": \"Esto quedo una chimba\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:14\", \"ID\": 9, \"Mensaje\": \"PERRITO LO LOGRASTE\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:41\", \"ID\": 10, \"Mensaje\": \"UST ES UN DURO\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 11:32:02\", \"ID\": 11, \"Mensaje\": \"asd\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:42:05\", \"ID\": 13, \"Mensaje\": \"asd\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:46:17\", \"ID\": 14, \"Mensaje\": \"Steven mlp\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:47:55\", \"ID\": 15, \"Mensaje\": \"perrito ust es un mk\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 21:04:39\", \"ID\": 16, \"Mensaje\": \"A tu madre\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}], \"casos_asociados\": [{\"ID\": 1, \"Caso_Principal_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"Caso_Asociado_ID\": {\"ID\": 2, \"Radicado\": \"000002R\", \"Nombre\": \"Caso2\", \"Actualizado\": \"2026-03-18 18:55:37\", \"Estado\": \"Escalado a supervisor\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}, {\"ID\": 8, \"Caso_Principal_ID\": 1, \"Creado_En\": \"2026-03-21 21:04:39\", \"Caso_Asociado_ID\": {\"ID\": 7, \"Radicado\": \"000007R\", \"Nombre\": \"Caso7\", \"Actualizado\": \"2026-03-21 15:34:15\", \"Estado\": \"Resuelto\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}], \"casos_principales\": []}',2,'2026-03-21 20:35:39',1),(15,'Caso eliminado','{\"ID\": 1, \"Creacion\": \"2007-08-26T00:00:00\", \"Nombre\": \"Caso Modificado por HTML\", \"Descripcion\": \"Caso principal MODIFICADO con dos asociados\", \"Afectados\": 90, \"Direccion\": \"#sa\", \"Caso_Asociado\": \"SI\", \"Actualizado_En\": \"2026-03-21T15:34:50\", \"Usuario_Creador_ID\": 2, \"Usuario_Asociado_ID\": 2, \"Incidente_ID\": 3, \"Estado_Caso_ID\": 1, \"Prioridad_ID\": 3, \"Barrio_ID\": 4, \"usuario_creador\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"usuario_asociado\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"incidente\": {\"ID\": 3, \"Incidente\": \"Expropiacion\", \"Prioridad_ID\": 4}, \"estado\": {\"ID\": 1, \"Nombre\": \"Pendiente\", \"Creado_En\": \"2026-03-18T03:38:54\"}, \"prioridad\": {\"ID\": 3, \"Prioridad\": \"Media\"}, \"barrio\": {\"ID\": 4, \"Nombre\": \"Porvenir\", \"Localidad\": {\"ID\": 4, \"Nombre\": \"Bosa\", \"Ciudad\": {\"ID\": 1, \"Nombre\": \"Bogota\", \"Departamento\": {\"ID\": 1, \"Nombre\": \"Bogota D.C\"}}}}, \"auditorias\": [{\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:34:50\", \"ID\": 13, \"Modificado_Por\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Accion\": \"Relacion Eliminada\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:35:39\", \"ID\": 14, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}], \"radicados\": [{\"ID\": 1, \"Radicado\": \"000001R\", \"Caso_ID\": 1}], \"discusiones\": [{\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 1, \"Mensaje\": \"Este caso requiere seguimiento inmediato.\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 2, \"Mensaje\": \"Se notificó al usuario sobre el cambio de estado.\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-20 10:06:06\", \"ID\": 8, \"Mensaje\": \"Esto quedo una chimba\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:14\", \"ID\": 9, \"Mensaje\": \"PERRITO LO LOGRASTE\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:41\", \"ID\": 10, \"Mensaje\": \"UST ES UN DURO\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 11:32:02\", \"ID\": 11, \"Mensaje\": \"asd\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:42:05\", \"ID\": 13, \"Mensaje\": \"asd\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:46:17\", \"ID\": 14, \"Mensaje\": \"Steven mlp\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:47:55\", \"ID\": 15, \"Mensaje\": \"perrito ust es un mk\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}], \"casos_asociados\": [{\"ID\": 1, \"Caso_Principal_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"Caso_Asociado_ID\": {\"ID\": 2, \"Radicado\": \"000002R\", \"Nombre\": \"Caso2\", \"Actualizado\": \"2026-03-18 18:55:37\", \"Estado\": \"Escalado a supervisor\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}], \"casos_principales\": []}',2,'2026-03-21 20:35:57',1),(16,'Caso modificado','{\"ID\": 1, \"Creacion\": \"2007-08-26T00:00:00\", \"Nombre\": \"Caso Modificado por HTML\", \"Descripcion\": \"Caso principal MODIFICADO con dos asociados\", \"Afectados\": 90, \"Direccion\": \"#sa\", \"Caso_Asociado\": \"SI\", \"Actualizado_En\": \"2026-03-21T15:36:11\", \"Usuario_Creador_ID\": 2, \"Usuario_Asociado_ID\": 2, \"Incidente_ID\": 3, \"Estado_Caso_ID\": 1, \"Prioridad_ID\": 3, \"Barrio_ID\": 4, \"usuario_creador\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"usuario_asociado\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"incidente\": {\"ID\": 3, \"Incidente\": \"Expropiacion\", \"Prioridad_ID\": 4}, \"estado\": {\"ID\": 1, \"Nombre\": \"Pendiente\", \"Creado_En\": \"2026-03-18T03:38:54\"}, \"prioridad\": {\"ID\": 3, \"Prioridad\": \"Media\"}, \"barrio\": {\"ID\": 4, \"Nombre\": \"Porvenir\", \"Localidad\": {\"ID\": 4, \"Nombre\": \"Bosa\", \"Ciudad\": {\"ID\": 1, \"Nombre\": \"Bogota\", \"Departamento\": {\"ID\": 1, \"Nombre\": \"Bogota D.C\"}}}}, \"auditorias\": [{\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:34:50\", \"ID\": 13, \"Modificado_Por\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Accion\": \"Relacion Eliminada\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:35:39\", \"ID\": 14, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso eliminado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:35:57\", \"ID\": 15, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}], \"radicados\": [{\"ID\": 1, \"Radicado\": \"000001R\", \"Caso_ID\": 1}], \"discusiones\": [{\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 1, \"Mensaje\": \"Este caso requiere seguimiento inmediato.\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 2, \"Mensaje\": \"Se notificó al usuario sobre el cambio de estado.\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-20 10:06:06\", \"ID\": 8, \"Mensaje\": \"Esto quedo una chimba\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:14\", \"ID\": 9, \"Mensaje\": \"PERRITO LO LOGRASTE\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:41\", \"ID\": 10, \"Mensaje\": \"UST ES UN DURO\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 11:32:02\", \"ID\": 11, \"Mensaje\": \"asd\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:42:05\", \"ID\": 13, \"Mensaje\": \"asd\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:46:17\", \"ID\": 14, \"Mensaje\": \"Steven mlp\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:47:55\", \"ID\": 15, \"Mensaje\": \"perrito ust es un mk\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}], \"casos_asociados\": [{\"ID\": 1, \"Caso_Principal_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"Caso_Asociado_ID\": {\"ID\": 2, \"Radicado\": \"000002R\", \"Nombre\": \"Caso2\", \"Actualizado\": \"2026-03-18 18:55:37\", \"Estado\": \"Escalado a supervisor\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}], \"casos_principales\": []}',2,'2026-03-21 20:44:55',1),(17,'Caso modificado','{\"ID\": 1, \"Creacion\": \"2007-08-26T00:00:00\", \"Nombre\": \"Caso Modificado por HTML\", \"Descripcion\": \"Caso principal MODIFICADO con dos asociados\", \"Afectados\": 90, \"Direccion\": \"#sa\", \"Caso_Asociado\": \"SI\", \"Actualizado_En\": \"2026-03-21T15:44:54\", \"Usuario_Creador_ID\": 2, \"Usuario_Asociado_ID\": 2, \"Incidente_ID\": 3, \"Estado_Caso_ID\": 2, \"Prioridad_ID\": 3, \"Barrio_ID\": 4, \"usuario_creador\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"usuario_asociado\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"incidente\": {\"ID\": 3, \"Incidente\": \"Expropiacion\", \"Prioridad_ID\": 4}, \"estado\": {\"ID\": 2, \"Nombre\": \"Activo\", \"Creado_En\": \"2026-03-18T03:38:54\"}, \"prioridad\": {\"ID\": 3, \"Prioridad\": \"Media\"}, \"barrio\": {\"ID\": 4, \"Nombre\": \"Porvenir\", \"Localidad\": {\"ID\": 4, \"Nombre\": \"Bosa\", \"Ciudad\": {\"ID\": 1, \"Nombre\": \"Bogota\", \"Departamento\": {\"ID\": 1, \"Nombre\": \"Bogota D.C\"}}}}, \"auditorias\": [{\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:34:50\", \"ID\": 13, \"Modificado_Por\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Accion\": \"Relacion Eliminada\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:35:39\", \"ID\": 14, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso eliminado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:35:57\", \"ID\": 15, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:44:55\", \"ID\": 16, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}], \"radicados\": [{\"ID\": 1, \"Radicado\": \"000001R\", \"Caso_ID\": 1}], \"discusiones\": [{\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 1, \"Mensaje\": \"Este caso requiere seguimiento inmediato.\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 2, \"Mensaje\": \"Se notificó al usuario sobre el cambio de estado.\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-20 10:06:06\", \"ID\": 8, \"Mensaje\": \"Esto quedo una chimba\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:14\", \"ID\": 9, \"Mensaje\": \"PERRITO LO LOGRASTE\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:41\", \"ID\": 10, \"Mensaje\": \"UST ES UN DURO\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 11:32:02\", \"ID\": 11, \"Mensaje\": \"asd\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:42:05\", \"ID\": 13, \"Mensaje\": \"asd\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:46:17\", \"ID\": 14, \"Mensaje\": \"Steven mlp\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:47:55\", \"ID\": 15, \"Mensaje\": \"perrito ust es un mk\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}], \"casos_asociados\": [{\"ID\": 1, \"Caso_Principal_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"Caso_Asociado_ID\": {\"ID\": 2, \"Radicado\": \"000002R\", \"Nombre\": \"Caso2\", \"Actualizado\": \"2026-03-18 18:55:37\", \"Estado\": \"Escalado a supervisor\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}], \"casos_principales\": []}',2,'2026-03-21 20:45:09',1),(18,'Caso modificado','{\"ID\": 1, \"Creacion\": \"2007-08-26T00:00:00\", \"Nombre\": \"Caso Modificado por HTML\", \"Descripcion\": \"Caso principal MODIFICADO con dos asociados\", \"Afectados\": 90, \"Direccion\": \"#sa\", \"Caso_Asociado\": \"SI\", \"Actualizado_En\": \"2026-03-21T15:46:30\", \"Usuario_Creador_ID\": 2, \"Usuario_Asociado_ID\": 2, \"Incidente_ID\": 3, \"Estado_Caso_ID\": 2, \"Prioridad_ID\": 3, \"Barrio_ID\": 4, \"usuario_creador\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"usuario_asociado\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"incidente\": {\"ID\": 3, \"Incidente\": \"Expropiacion\", \"Prioridad_ID\": 4}, \"estado\": {\"ID\": 2, \"Nombre\": \"Activo\", \"Creado_En\": \"2026-03-18T03:38:54\"}, \"prioridad\": {\"ID\": 3, \"Prioridad\": \"Media\"}, \"barrio\": {\"ID\": 4, \"Nombre\": \"Porvenir\", \"Localidad\": {\"ID\": 4, \"Nombre\": \"Bosa\", \"Ciudad\": {\"ID\": 1, \"Nombre\": \"Bogota\", \"Departamento\": {\"ID\": 1, \"Nombre\": \"Bogota D.C\"}}}}, \"auditorias\": [{\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:34:50\", \"ID\": 13, \"Modificado_Por\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Accion\": \"Relacion Eliminada\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:35:39\", \"ID\": 14, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso eliminado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:35:57\", \"ID\": 15, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:44:55\", \"ID\": 16, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:45:09\", \"ID\": 17, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}], \"radicados\": [{\"ID\": 1, \"Radicado\": \"000001R\", \"Caso_ID\": 1}], \"discusiones\": [{\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 1, \"Mensaje\": \"Este caso requiere seguimiento inmediato.\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 2, \"Mensaje\": \"Se notificó al usuario sobre el cambio de estado.\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-20 10:06:06\", \"ID\": 8, \"Mensaje\": \"Esto quedo una chimba\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:14\", \"ID\": 9, \"Mensaje\": \"PERRITO LO LOGRASTE\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:41\", \"ID\": 10, \"Mensaje\": \"UST ES UN DURO\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 11:32:02\", \"ID\": 11, \"Mensaje\": \"asd\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:42:05\", \"ID\": 13, \"Mensaje\": \"asd\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:46:17\", \"ID\": 14, \"Mensaje\": \"Steven mlp\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:47:55\", \"ID\": 15, \"Mensaje\": \"perrito ust es un mk\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}], \"casos_asociados\": [{\"ID\": 1, \"Caso_Principal_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"Caso_Asociado_ID\": {\"ID\": 2, \"Radicado\": \"000002R\", \"Nombre\": \"Caso2\", \"Actualizado\": \"2026-03-18 18:55:37\", \"Estado\": \"Escalado a supervisor\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}], \"casos_principales\": []}',2,'2026-03-21 20:46:52',1),(19,'Caso modificado','{\"ID\": 1, \"Creacion\": \"2007-08-26T00:00:00\", \"Nombre\": \"Caso Modificado por HTML\", \"Descripcion\": \"Caso principal MODIFICADO con dos asociados\", \"Afectados\": 90, \"Direccion\": \"#sa\", \"Caso_Asociado\": \"SI\", \"Actualizado_En\": \"2026-03-21T15:47:45\", \"Usuario_Creador_ID\": 2, \"Usuario_Asociado_ID\": 2, \"Incidente_ID\": 3, \"Estado_Caso_ID\": 2, \"Prioridad_ID\": 3, \"Barrio_ID\": 4, \"usuario_creador\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"usuario_asociado\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"incidente\": {\"ID\": 3, \"Incidente\": \"Expropiacion\", \"Prioridad_ID\": 4}, \"estado\": {\"ID\": 2, \"Nombre\": \"Activo\", \"Creado_En\": \"2026-03-18T03:38:54\"}, \"prioridad\": {\"ID\": 3, \"Prioridad\": \"Media\"}, \"barrio\": {\"ID\": 4, \"Nombre\": \"Porvenir\", \"Localidad\": {\"ID\": 4, \"Nombre\": \"Bosa\", \"Ciudad\": {\"ID\": 1, \"Nombre\": \"Bogota\", \"Departamento\": {\"ID\": 1, \"Nombre\": \"Bogota D.C\"}}}}, \"auditorias\": [{\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:34:50\", \"ID\": 13, \"Modificado_Por\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Accion\": \"Relacion Eliminada\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:35:39\", \"ID\": 14, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso eliminado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:35:57\", \"ID\": 15, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:44:55\", \"ID\": 16, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:45:09\", \"ID\": 17, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:46:52\", \"ID\": 18, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}], \"radicados\": [{\"ID\": 1, \"Radicado\": \"000001R\", \"Caso_ID\": 1}], \"discusiones\": [{\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 1, \"Mensaje\": \"Este caso requiere seguimiento inmediato.\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 2, \"Mensaje\": \"Se notificó al usuario sobre el cambio de estado.\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-20 10:06:06\", \"ID\": 8, \"Mensaje\": \"Esto quedo una chimba\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:14\", \"ID\": 9, \"Mensaje\": \"PERRITO LO LOGRASTE\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:41\", \"ID\": 10, \"Mensaje\": \"UST ES UN DURO\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 11:32:02\", \"ID\": 11, \"Mensaje\": \"asd\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:42:05\", \"ID\": 13, \"Mensaje\": \"asd\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:46:17\", \"ID\": 14, \"Mensaje\": \"Steven mlp\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:47:55\", \"ID\": 15, \"Mensaje\": \"perrito ust es un mk\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}], \"casos_asociados\": [{\"ID\": 1, \"Caso_Principal_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"Caso_Asociado_ID\": {\"ID\": 2, \"Radicado\": \"000002R\", \"Nombre\": \"Caso2\", \"Actualizado\": \"2026-03-18 18:55:37\", \"Estado\": \"Escalado a supervisor\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}], \"casos_principales\": []}',2,'2026-03-21 20:48:13',1),(20,'Caso modificado','{\"ID\": 1, \"Creacion\": \"2007-08-26T00:00:00\", \"Nombre\": \"Caso Modificado por HTML\", \"Descripcion\": \"Caso principal MODIFICADO con dos asociados\", \"Afectados\": 90, \"Direccion\": \"#sa\", \"Caso_Asociado\": \"SI\", \"Actualizado_En\": \"2026-03-21T15:48:13\", \"Usuario_Creador_ID\": 2, \"Usuario_Asociado_ID\": 2, \"Incidente_ID\": 3, \"Estado_Caso_ID\": 3, \"Prioridad_ID\": 3, \"Barrio_ID\": 4, \"usuario_creador\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"usuario_asociado\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"incidente\": {\"ID\": 3, \"Incidente\": \"Expropiacion\", \"Prioridad_ID\": 4}, \"estado\": {\"ID\": 3, \"Nombre\": \"Resuelto\", \"Creado_En\": \"2026-03-18T03:38:54\"}, \"prioridad\": {\"ID\": 3, \"Prioridad\": \"Media\"}, \"barrio\": {\"ID\": 4, \"Nombre\": \"Porvenir\", \"Localidad\": {\"ID\": 4, \"Nombre\": \"Bosa\", \"Ciudad\": {\"ID\": 1, \"Nombre\": \"Bogota\", \"Departamento\": {\"ID\": 1, \"Nombre\": \"Bogota D.C\"}}}}, \"auditorias\": [{\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:34:50\", \"ID\": 13, \"Modificado_Por\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Accion\": \"Relacion Eliminada\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:35:39\", \"ID\": 14, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso eliminado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:35:57\", \"ID\": 15, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:44:55\", \"ID\": 16, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:45:09\", \"ID\": 17, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:46:52\", \"ID\": 18, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:48:13\", \"ID\": 19, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}], \"radicados\": [{\"ID\": 1, \"Radicado\": \"000001R\", \"Caso_ID\": 1}], \"discusiones\": [{\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 1, \"Mensaje\": \"Este caso requiere seguimiento inmediato.\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 2, \"Mensaje\": \"Se notificó al usuario sobre el cambio de estado.\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-20 10:06:06\", \"ID\": 8, \"Mensaje\": \"Esto quedo una chimba\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:14\", \"ID\": 9, \"Mensaje\": \"PERRITO LO LOGRASTE\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:41\", \"ID\": 10, \"Mensaje\": \"UST ES UN DURO\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 11:32:02\", \"ID\": 11, \"Mensaje\": \"asd\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:42:05\", \"ID\": 13, \"Mensaje\": \"asd\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:46:17\", \"ID\": 14, \"Mensaje\": \"Steven mlp\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:47:55\", \"ID\": 15, \"Mensaje\": \"perrito ust es un mk\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}], \"casos_asociados\": [{\"ID\": 1, \"Caso_Principal_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"Caso_Asociado_ID\": {\"ID\": 2, \"Radicado\": \"000002R\", \"Nombre\": \"Caso2\", \"Actualizado\": \"2026-03-18 18:55:37\", \"Estado\": \"Escalado a supervisor\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}], \"casos_principales\": []}',2,'2026-03-21 21:04:39',3),(21,'Caso modificado','{\"ID\": 1, \"Creacion\": \"2007-08-26T00:00:00\", \"Nombre\": \"Caso Modificado por HTML\", \"Descripcion\": \"Caso principal MODIFICADO con dos asociados\", \"Afectados\": 90, \"Direccion\": \"#sa\", \"Caso_Asociado\": \"SI\", \"Actualizado_En\": \"2026-03-21T16:04:38\", \"Usuario_Creador_ID\": 1, \"Usuario_Asociado_ID\": 2, \"Incidente_ID\": 3, \"Estado_Caso_ID\": 3, \"Prioridad_ID\": 3, \"Barrio_ID\": 4, \"usuario_creador\": {\"ID\": 1, \"Nombre\": \"Administrador\", \"Correo\": \"Administrador@gaialink.online\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 1, \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, \"usuario_asociado\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"incidente\": {\"ID\": 3, \"Incidente\": \"Expropiacion\", \"Prioridad_ID\": 4}, \"estado\": {\"ID\": 3, \"Nombre\": \"Resuelto\", \"Creado_En\": \"2026-03-18T03:38:54\"}, \"prioridad\": {\"ID\": 3, \"Prioridad\": \"Media\"}, \"barrio\": {\"ID\": 4, \"Nombre\": \"Porvenir\", \"Localidad\": {\"ID\": 4, \"Nombre\": \"Bosa\", \"Ciudad\": {\"ID\": 1, \"Nombre\": \"Bogota\", \"Departamento\": {\"ID\": 1, \"Nombre\": \"Bogota D.C\"}}}}, \"auditorias\": [{\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:34:50\", \"ID\": 13, \"Modificado_Por\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Accion\": \"Relacion Eliminada\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:35:39\", \"ID\": 14, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso eliminado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:35:57\", \"ID\": 15, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:44:55\", \"ID\": 16, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:45:09\", \"ID\": 17, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:46:52\", \"ID\": 18, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:48:13\", \"ID\": 19, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 21:04:39\", \"ID\": 20, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}], \"radicados\": [{\"ID\": 1, \"Radicado\": \"000001R\", \"Caso_ID\": 1}], \"discusiones\": [{\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 1, \"Mensaje\": \"Este caso requiere seguimiento inmediato.\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 2, \"Mensaje\": \"Se notificó al usuario sobre el cambio de estado.\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-20 10:06:06\", \"ID\": 8, \"Mensaje\": \"Esto quedo una chimba\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:14\", \"ID\": 9, \"Mensaje\": \"PERRITO LO LOGRASTE\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:41\", \"ID\": 10, \"Mensaje\": \"UST ES UN DURO\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 11:32:02\", \"ID\": 11, \"Mensaje\": \"asd\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:42:05\", \"ID\": 13, \"Mensaje\": \"asd\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:46:17\", \"ID\": 14, \"Mensaje\": \"Steven mlp\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:47:55\", \"ID\": 15, \"Mensaje\": \"perrito ust es un mk\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 21:04:39\", \"ID\": 16, \"Mensaje\": \"A tu madre\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}], \"casos_asociados\": [{\"ID\": 1, \"Caso_Principal_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"Caso_Asociado_ID\": {\"ID\": 2, \"Radicado\": \"000002R\", \"Nombre\": \"Caso2\", \"Actualizado\": \"2026-03-18 18:55:37\", \"Estado\": \"Escalado a supervisor\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}, {\"ID\": 8, \"Caso_Principal_ID\": 1, \"Creado_En\": \"2026-03-21 21:04:39\", \"Caso_Asociado_ID\": {\"ID\": 7, \"Radicado\": \"000007R\", \"Nombre\": \"Caso7\", \"Actualizado\": \"2026-03-21 15:34:15\", \"Estado\": \"Resuelto\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}], \"casos_principales\": []}',4,'2026-03-21 22:42:06',1),(25,'Caso creado','{\"ID\": 13, \"Creacion\": \"2026-03-22\", \"Nombre\": \"CASO CREADO POR FRONT\", \"Descripcion\": \"CASO CREADO POR FRONT\", \"Afectados\": \"69\", \"Direccion\": \"Dg sapo\", \"Caso_Asociado\": \"SI\", \"Actualizado_En\": null, \"Usuario_Creador_ID\": \"4\", \"Usuario_Asociado_ID\": \"2\", \"Incidente_ID\": \"3\", \"Estado_Caso_ID\": \"1\", \"Prioridad_ID\": \"4\", \"Barrio_ID\": 6, \"usuario_creador\": {\"ID\": 4, \"Nombre\": \"Stmora4123\", \"Correo\": \"smorag@sanmateo.edu.co\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 4, \"Documento\": \"1122334411\", \"Primer_Nombre\": \"Steven\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Mora\", \"Segundo_Apellido\": \"Gomez\"}}, \"usuario_asociado\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"incidente\": {\"ID\": 3, \"Incidente\": \"Expropiacion\", \"Prioridad_ID\": 4}, \"estado\": {\"ID\": 1, \"Nombre\": \"Pendiente\", \"Creado_En\": \"2026-03-18T03:38:54\"}, \"prioridad\": {\"ID\": 4, \"Prioridad\": \"Alta\"}, \"barrio\": {\"ID\": 6, \"Nombre\": \"Suba\", \"Localidad\": {\"ID\": 6, \"Nombre\": \"Suba\", \"Ciudad\": {\"ID\": 5, \"Nombre\": \"Suba\", \"Departamento\": {\"ID\": 4, \"Nombre\": \"Suba\"}}}}, \"auditorias\": [], \"radicados\": [{\"ID\": 9, \"Radicado\": \"000008R\", \"Caso_ID\": 13}], \"discusiones\": [], \"casos_asociados\": [], \"casos_principales\": []}',2,'2026-03-23 05:17:25',13),(26,'Caso creado','{\"ID\": 14, \"Creacion\": \"2026-03-23\", \"Nombre\": \"CASO CREADO POR FRONT\", \"Descripcion\": \"CASO CREADO POR FRONT\", \"Afectados\": \"9\", \"Direccion\": \"Dg sapo\", \"Caso_Asociado\": \"SI\", \"Actualizado_En\": null, \"Usuario_Creador_ID\": \"2\", \"Usuario_Asociado_ID\": \"2\", \"Incidente_ID\": \"3\", \"Estado_Caso_ID\": \"7\", \"Prioridad_ID\": \"1\", \"Barrio_ID\": 7, \"usuario_creador\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"usuario_asociado\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"incidente\": {\"ID\": 3, \"Incidente\": \"Expropiacion\", \"Prioridad_ID\": 4}, \"estado\": {\"ID\": 7, \"Nombre\": \"Reabierto\", \"Creado_En\": \"2026-03-18T03:38:54\"}, \"prioridad\": {\"ID\": 1, \"Prioridad\": \"Muy Baja\"}, \"barrio\": {\"ID\": 7, \"Nombre\": \"Lologro\", \"Localidad\": {\"ID\": 9, \"Nombre\": \"Lologro\", \"Ciudad\": {\"ID\": 6, \"Nombre\": \"Lologro\", \"Departamento\": {\"ID\": 7, \"Nombre\": \"Lologro\"}}}}, \"auditorias\": [], \"radicados\": [{\"ID\": 10, \"Radicado\": \"000009R\", \"Caso_ID\": 14}], \"discusiones\": [], \"casos_asociados\": [{\"ID\": 9, \"Caso_Principal_ID\": 14, \"Creado_En\": \"2026-03-23 05:20:04.565906\", \"Caso_Asociado_ID\": {\"ID\": 1, \"Radicado\": \"000001R\", \"Nombre\": \"Caso Modificado por HTML\", \"Actualizado\": \"2026-03-21 17:42:06\", \"Estado\": \"Resuelto\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}], \"casos_principales\": []}',2,'2026-03-23 05:20:05',14),(27,'Caso creado','{\"ID\": 15, \"Creacion\": \"2026-03-23\", \"Nombre\": \"Caso creado por html\", \"Descripcion\": \"Caso creado por html\", \"Afectados\": \"79\", \"Direccion\": \"SAPO23\", \"Caso_Asociado\": \"SI\", \"Actualizado_En\": null, \"Usuario_Creador_ID\": \"4\", \"Usuario_Asociado_ID\": \"2\", \"Incidente_ID\": \"4\", \"Estado_Caso_ID\": \"2\", \"Prioridad_ID\": \"3\", \"Barrio_ID\": 4, \"usuario_creador\": {\"ID\": 4, \"Nombre\": \"Stmora4123\", \"Correo\": \"smorag@sanmateo.edu.co\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 4, \"Documento\": \"1122334411\", \"Primer_Nombre\": \"Steven\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Mora\", \"Segundo_Apellido\": \"Gomez\"}}, \"usuario_asociado\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"incidente\": {\"ID\": 4, \"Incidente\": \"Hurto\", \"Prioridad_ID\": 3}, \"estado\": {\"ID\": 2, \"Nombre\": \"Activo\", \"Creado_En\": \"2026-03-18T03:38:54\"}, \"prioridad\": {\"ID\": 3, \"Prioridad\": \"Media\"}, \"barrio\": {\"ID\": 4, \"Nombre\": \"Porvenir\", \"Localidad\": {\"ID\": 4, \"Nombre\": \"Bosa\", \"Ciudad\": {\"ID\": 1, \"Nombre\": \"Bogota\", \"Departamento\": {\"ID\": 1, \"Nombre\": \"Bogota D.C\"}}}}, \"auditorias\": [], \"radicados\": [{\"ID\": 11, \"Radicado\": \"000010R\", \"Caso_ID\": 15}], \"discusiones\": [], \"casos_asociados\": [{\"ID\": 10, \"Caso_Principal_ID\": 15, \"Creado_En\": \"2026-03-23 05:23:11.548809\", \"Caso_Asociado_ID\": {\"ID\": 14, \"Radicado\": \"000009R\", \"Nombre\": \"CASO CREADO POR FRONT\", \"Actualizado\": null, \"Estado\": \"Reabierto\"}, \"Tipo_Relacion_ID\": \"Duplicado\", \"Tipo_Relacion_ID_ID\": 2}], \"casos_principales\": []}',2,'2026-03-23 05:23:12',15),(28,'Caso creado','{\"ID\": 16, \"Creacion\": \"2026-03-23\", \"Nombre\": \"CASO CREADO POR FRONT\", \"Descripcion\": \"sadasd\", \"Afectados\": \"4\", \"Direccion\": \"Dg sapo\", \"Caso_Asociado\": \"SI\", \"Actualizado_En\": null, \"Usuario_Creador_ID\": \"2\", \"Usuario_Asociado_ID\": \"2\", \"Incidente_ID\": \"2\", \"Estado_Caso_ID\": \"5\", \"Prioridad_ID\": \"3\", \"Barrio_ID\": 4, \"usuario_creador\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"usuario_asociado\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"incidente\": {\"ID\": 2, \"Incidente\": \"Predios Despojados\", \"Prioridad_ID\": 5}, \"estado\": {\"ID\": 5, \"Nombre\": \"En espera del usuario\", \"Creado_En\": \"2026-03-18T03:38:54\"}, \"prioridad\": {\"ID\": 3, \"Prioridad\": \"Media\"}, \"barrio\": {\"ID\": 4, \"Nombre\": \"Porvenir\", \"Localidad\": {\"ID\": 4, \"Nombre\": \"Bosa\", \"Ciudad\": {\"ID\": 1, \"Nombre\": \"Bogota\", \"Departamento\": {\"ID\": 1, \"Nombre\": \"Bogota D.C\"}}}}, \"auditorias\": [], \"radicados\": [{\"ID\": 12, \"Radicado\": \"000011R\", \"Caso_ID\": 16}], \"discusiones\": [], \"casos_asociados\": [{\"ID\": 11, \"Caso_Principal_ID\": 16, \"Creado_En\": \"2026-03-23 05:28:03.303589\", \"Caso_Asociado_ID\": {\"ID\": 3, \"Radicado\": \"000003R\", \"Nombre\": \"Caso3\", \"Actualizado\": \"2026-03-18 18:55:37\", \"Estado\": \"Pendiente\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}], \"casos_principales\": []}',2,'2026-03-23 05:28:03',16),(29,'Caso modificado','{\"ID\": 1, \"Creacion\": \"2007-08-26T00:00:00\", \"Nombre\": \"Caso Modificado por HTML\", \"Descripcion\": \"Caso principal MODIFICADO con dos asociados\", \"Afectados\": 90, \"Direccion\": \"#sa\", \"Caso_Asociado\": \"SI\", \"Actualizado_En\": \"2026-03-21T17:42:06\", \"Usuario_Creador_ID\": 2, \"Usuario_Asociado_ID\": 2, \"Incidente_ID\": 3, \"Estado_Caso_ID\": 3, \"Prioridad_ID\": 3, \"Barrio_ID\": 4, \"usuario_creador\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"usuario_asociado\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"incidente\": {\"ID\": 3, \"Incidente\": \"Expropiacion\", \"Prioridad_ID\": 4}, \"estado\": {\"ID\": 3, \"Nombre\": \"Resuelto\", \"Creado_En\": \"2026-03-18T03:38:54\"}, \"prioridad\": {\"ID\": 3, \"Prioridad\": \"Media\"}, \"barrio\": {\"ID\": 4, \"Nombre\": \"Porvenir\", \"Localidad\": {\"ID\": 4, \"Nombre\": \"Bosa\", \"Ciudad\": {\"ID\": 1, \"Nombre\": \"Bogota\", \"Departamento\": {\"ID\": 1, \"Nombre\": \"Bogota D.C\"}}}}, \"auditorias\": [{\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:34:50\", \"ID\": 13, \"Modificado_Por\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Accion\": \"Caso eliminado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:35:57\", \"ID\": 15, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:44:55\", \"ID\": 16, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:45:09\", \"ID\": 17, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:46:52\", \"ID\": 18, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:48:13\", \"ID\": 19, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 22:42:06\", \"ID\": 21, \"Modificado_Por\": {\"ID\": 4, \"Documento\": \"1122334411\", \"Primer_Nombre\": \"Steven\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Mora\", \"Segundo_Apellido\": \"Gomez\"}}], \"radicados\": [{\"ID\": 1, \"Radicado\": \"000001R\", \"Caso_ID\": 1}], \"discusiones\": [{\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 1, \"Mensaje\": \"Este caso requiere seguimiento inmediato.\", \"Nombre\": \"Administrador\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 2, \"Mensaje\": \"Se notificó al usuario sobre el cambio de estado.\", \"Nombre\": \"Administrador\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-20 10:06:06\", \"ID\": 8, \"Mensaje\": \"Esto quedo una chimba\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:14\", \"ID\": 9, \"Mensaje\": \"PERRITO LO LOGRASTE\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:41\", \"ID\": 10, \"Mensaje\": \"UST ES UN DURO\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 11:32:02\", \"ID\": 11, \"Mensaje\": \"asd\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:42:05\", \"ID\": 13, \"Mensaje\": \"asd\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:46:17\", \"ID\": 14, \"Mensaje\": \"Steven mlp\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:47:55\", \"ID\": 15, \"Mensaje\": \"perrito ust es un mk\", \"Nombre\": \"Administrador\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 21:04:39\", \"ID\": 16, \"Mensaje\": \"A tu madre\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 22:42:06\", \"ID\": 17, \"Mensaje\": \"Que chimba el vicio\", \"Nombre\": \"Stmora4123\", \"Persona\": {\"ID\": 4, \"Documento\": \"1122334411\", \"Primer_Nombre\": \"Steven\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Mora\", \"Segundo_Apellido\": \"Gomez\"}}], \"casos_asociados\": [{\"ID\": 1, \"Caso_Principal_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"Caso_Asociado_ID\": {\"ID\": 2, \"Radicado\": \"000002R\", \"Nombre\": \"Caso2\", \"Actualizado\": \"2026-03-18 18:55:37\", \"Estado\": \"Escalado a supervisor\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}, {\"ID\": 8, \"Caso_Principal_ID\": 1, \"Creado_En\": \"2026-03-21 21:04:39\", \"Caso_Asociado_ID\": {\"ID\": 7, \"Radicado\": \"000007R\", \"Nombre\": \"Caso7\", \"Actualizado\": \"2026-03-21 15:34:15\", \"Estado\": \"Resuelto\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}], \"casos_principales\": [{\"ID\": 9, \"Caso_Principal_ID\": 14, \"Creado_En\": \"2026-03-23 05:20:05\", \"Caso_Asociado_ID\": {\"ID\": 1, \"Radicado\": \"000001R\", \"Nombre\": \"Caso Modificado por HTML\", \"Actualizado\": \"2026-03-21 17:42:06\", \"Estado\": \"Resuelto\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}]}',2,'2026-03-23 12:10:43',1),(30,'Caso modificado','{\"ID\": 1, \"Creacion\": \"2007-08-26T00:00:00\", \"Nombre\": \"Caso Modificado por HTML\", \"Descripcion\": \"Caso principal MODIFICADO con dos asociados\", \"Afectados\": 90, \"Direccion\": \"#sa\", \"Caso_Asociado\": \"SI\", \"Actualizado_En\": \"2026-03-23T07:10:42\", \"Usuario_Creador_ID\": 2, \"Usuario_Asociado_ID\": 2, \"Incidente_ID\": 3, \"Estado_Caso_ID\": 9, \"Prioridad_ID\": 3, \"Barrio_ID\": 4, \"usuario_creador\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"usuario_asociado\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 2, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"incidente\": {\"ID\": 3, \"Incidente\": \"Expropiacion\", \"Prioridad_ID\": 4}, \"estado\": {\"ID\": 9, \"Nombre\": \"Tomando desicion \", \"Creado_En\": \"2026-03-23T00:46:58\"}, \"prioridad\": {\"ID\": 3, \"Prioridad\": \"Media\"}, \"barrio\": {\"ID\": 4, \"Nombre\": \"Porvenir\", \"Localidad\": {\"ID\": 4, \"Nombre\": \"Bosa\", \"Ciudad\": {\"ID\": 1, \"Nombre\": \"Bogota\", \"Departamento\": {\"ID\": 1, \"Nombre\": \"Bogota D.C\"}}}}, \"auditorias\": [{\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:34:50\", \"ID\": 13, \"Modificado_Por\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Accion\": \"Caso eliminado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:35:57\", \"ID\": 15, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:44:55\", \"ID\": 16, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:45:09\", \"ID\": 17, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:46:52\", \"ID\": 18, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:48:13\", \"ID\": 19, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 22:42:06\", \"ID\": 21, \"Modificado_Por\": {\"ID\": 4, \"Documento\": \"1122334411\", \"Primer_Nombre\": \"Steven\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Mora\", \"Segundo_Apellido\": \"Gomez\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-23 12:10:43\", \"ID\": 29, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}], \"radicados\": [{\"ID\": 1, \"Radicado\": \"000001R\", \"Caso_ID\": 1}], \"discusiones\": [{\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 1, \"Mensaje\": \"Este caso requiere seguimiento inmediato.\", \"Nombre\": \"Administrador\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 2, \"Mensaje\": \"Se notificó al usuario sobre el cambio de estado.\", \"Nombre\": \"Administrador\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-20 10:06:06\", \"ID\": 8, \"Mensaje\": \"Esto quedo una chimba\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:14\", \"ID\": 9, \"Mensaje\": \"PERRITO LO LOGRASTE\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:41\", \"ID\": 10, \"Mensaje\": \"UST ES UN DURO\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 11:32:02\", \"ID\": 11, \"Mensaje\": \"asd\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:42:05\", \"ID\": 13, \"Mensaje\": \"asd\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:46:17\", \"ID\": 14, \"Mensaje\": \"Steven mlp\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:47:55\", \"ID\": 15, \"Mensaje\": \"perrito ust es un mk\", \"Nombre\": \"Administrador\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 21:04:39\", \"ID\": 16, \"Mensaje\": \"A tu madre\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 22:42:06\", \"ID\": 17, \"Mensaje\": \"Que chimba el vicio\", \"Nombre\": \"Stmora4123\", \"Persona\": {\"ID\": 4, \"Documento\": \"1122334411\", \"Primer_Nombre\": \"Steven\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Mora\", \"Segundo_Apellido\": \"Gomez\"}}], \"casos_asociados\": [{\"ID\": 1, \"Caso_Principal_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"Caso_Asociado_ID\": {\"ID\": 2, \"Radicado\": \"000002R\", \"Nombre\": \"Caso2\", \"Actualizado\": \"2026-03-18 18:55:37\", \"Estado\": \"Escalado a supervisor\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}, {\"ID\": 8, \"Caso_Principal_ID\": 1, \"Creado_En\": \"2026-03-21 21:04:39\", \"Caso_Asociado_ID\": {\"ID\": 7, \"Radicado\": \"000007R\", \"Nombre\": \"Caso7\", \"Actualizado\": \"2026-03-21 15:34:15\", \"Estado\": \"Resuelto\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}], \"casos_principales\": [{\"ID\": 9, \"Caso_Principal_ID\": 14, \"Creado_En\": \"2026-03-23 05:20:05\", \"Caso_Asociado_ID\": {\"ID\": 1, \"Radicado\": \"000001R\", \"Nombre\": \"Caso Modificado por HTML\", \"Actualizado\": \"2026-03-23 07:10:42\", \"Estado\": \"Tomando desicion \"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}]}',2,'2026-03-23 12:11:16',1),(31,'Caso creado','{\"ID\": 17, \"Creacion\": \"2026-03-26\", \"Nombre\": \"Caso creado por html\", \"Descripcion\": \"kbkjbvkjv\", \"Afectados\": \"143\", \"Direccion\": \"Diagonal 42 Sur 24B\", \"Caso_Asociado\": \"SI\", \"Actualizado_En\": null, \"Usuario_Creador_ID\": 2, \"Usuario_Asociado_ID\": \"2\", \"Incidente_ID\": \"1\", \"Estado_Caso_ID\": \"3\", \"Prioridad_ID\": \"3\", \"Barrio_ID\": 8, \"usuario_creador\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 1, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"usuario_asociado\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 1, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"incidente\": {\"ID\": 1, \"Incidente\": \"Desplazamiento\", \"Prioridad_ID\": 5}, \"estado\": {\"ID\": 3, \"Nombre\": \"Resuelto\", \"Creado_En\": \"2026-03-18T03:38:54\"}, \"prioridad\": {\"ID\": 3, \"Prioridad\": \"Media\"}, \"barrio\": {\"ID\": 8, \"Nombre\": \"Asdas\", \"Localidad\": {\"ID\": 10, \"Nombre\": \"Bogotá, d.c.\", \"Ciudad\": {\"ID\": 7, \"Nombre\": \"Bogotá, d.c.\", \"Departamento\": {\"ID\": 8, \"Nombre\": \"Asda\"}}}}, \"auditorias\": [], \"radicados\": [{\"ID\": 13, \"Radicado\": \"000012R\", \"Caso_ID\": 17}], \"discusiones\": [], \"casos_asociados\": [], \"casos_principales\": []}',2,'2026-03-26 08:16:18',17),(32,'Caso modificado','{\"ID\": 1, \"Creacion\": \"2007-08-26T00:00:00\", \"Nombre\": \"CASO ACTIVO 1\", \"Descripcion\": \"Caso principal MODIFICADO con dos asociados\", \"Afectados\": 90, \"Direccion\": \"#sa\", \"Caso_Asociado\": \"SI\", \"Actualizado_En\": \"2026-03-23T23:13:48\", \"Usuario_Creador_ID\": 2, \"Usuario_Asociado_ID\": 1, \"Incidente_ID\": 3, \"Estado_Caso_ID\": 2, \"Prioridad_ID\": 3, \"Barrio_ID\": 4, \"usuario_creador\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 1, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"usuario_asociado\": {\"ID\": 1, \"Nombre\": \"Administrador\", \"Correo\": \"Administrador@gaialink.online\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 1, \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, \"incidente\": {\"ID\": 3, \"Incidente\": \"Expropiacion\", \"Prioridad_ID\": 4}, \"estado\": {\"ID\": 2, \"Nombre\": \"Activo\", \"Creado_En\": \"2026-03-18T03:38:54\"}, \"prioridad\": {\"ID\": 3, \"Prioridad\": \"Media\"}, \"barrio\": {\"ID\": 4, \"Nombre\": \"Porvenir\", \"Localidad\": {\"ID\": 4, \"Nombre\": \"Bosa\", \"Ciudad\": {\"ID\": 1, \"Nombre\": \"Bogota\", \"Departamento\": {\"ID\": 1, \"Nombre\": \"Bogota D.C\"}}}}, \"auditorias\": [{\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:34:50\", \"ID\": 13, \"Modificado_Por\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Accion\": \"Relacion Eliminada\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:35:39\", \"ID\": 14, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso eliminado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:35:57\", \"ID\": 15, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:44:55\", \"ID\": 16, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:45:09\", \"ID\": 17, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:46:52\", \"ID\": 18, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 20:48:13\", \"ID\": 19, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-21 22:42:06\", \"ID\": 21, \"Modificado_Por\": {\"ID\": 4, \"Documento\": \"1122334411\", \"Primer_Nombre\": \"Steven\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Mora\", \"Segundo_Apellido\": \"Gomez\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-23 12:10:43\", \"ID\": 29, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Accion\": \"Caso modificado\", \"Caso_ID\": 1, \"Fecha_Modificacion\": \"2026-03-23 12:11:16\", \"ID\": 30, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}], \"radicados\": [{\"ID\": 1, \"Radicado\": \"000001R\", \"Caso_ID\": 1}], \"discusiones\": [{\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 1, \"Mensaje\": \"Este caso requiere seguimiento inmediato.\", \"Nombre\": \"Administrador\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"ID\": 2, \"Mensaje\": \"Se notificó al usuario sobre el cambio de estado.\", \"Nombre\": \"Administrador\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-20 10:06:06\", \"ID\": 8, \"Mensaje\": \"Esto quedo una chimba\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:14\", \"ID\": 9, \"Mensaje\": \"PERRITO LO LOGRASTE\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 08:03:41\", \"ID\": 10, \"Mensaje\": \"UST ES UN DURO\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 11:32:02\", \"ID\": 11, \"Mensaje\": \"asd\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:42:05\", \"ID\": 13, \"Mensaje\": \"asd\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:46:17\", \"ID\": 14, \"Mensaje\": \"Steven mlp\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 19:47:55\", \"ID\": 15, \"Mensaje\": \"perrito ust es un mk\", \"Nombre\": \"Administrador\", \"Persona\": {\"ID\": 1, \"Documento\": \"1111111111\", \"Primer_Nombre\": \"Admin\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Admin\", \"Segundo_Apellido\": \"Admin\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 21:04:39\", \"ID\": 16, \"Mensaje\": \"A tu madre\", \"Nombre\": \"Sugarrigbi\", \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, {\"Caso_ID\": 1, \"Creado_En\": \"2026-03-21 22:42:06\", \"ID\": 17, \"Mensaje\": \"Que chimba el vicio\", \"Nombre\": \"Stmora4123\", \"Persona\": {\"ID\": 4, \"Documento\": \"1122334411\", \"Primer_Nombre\": \"Steven\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Mora\", \"Segundo_Apellido\": \"Gomez\"}}], \"casos_asociados\": [{\"ID\": 1, \"Caso_Principal_ID\": 1, \"Creado_En\": \"2026-03-18 03:38:54\", \"Caso_Asociado_ID\": {\"ID\": 2, \"Radicado\": \"000002R\", \"Nombre\": \"Caso2\", \"Actualizado\": \"2026-03-23 20:42:00\", \"Estado\": \"Pendiente\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}, {\"ID\": 8, \"Caso_Principal_ID\": 1, \"Creado_En\": \"2026-03-21 21:04:39\", \"Caso_Asociado_ID\": {\"ID\": 7, \"Radicado\": \"000007R\", \"Nombre\": \"Caso7\", \"Actualizado\": \"2026-03-24 20:32:56\", \"Estado\": \"Eliminado\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}], \"casos_principales\": [{\"ID\": 9, \"Caso_Principal_ID\": 14, \"Creado_En\": \"2026-03-23 05:20:05\", \"Caso_Asociado_ID\": {\"ID\": 1, \"Radicado\": \"000001R\", \"Nombre\": \"CASO ACTIVO 1\", \"Actualizado\": \"2026-03-23 23:13:48\", \"Estado\": \"Activo\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}]}',2,'2026-03-26 20:42:20',1),(33,'Caso creado','{\"ID\": 18, \"Creacion\": \"2026-03-26\", \"Nombre\": \"CASO CREADO POR JWT\", \"Descripcion\": \"CASO CREADO POR JWT\", \"Afectados\": \"21\", \"Direccion\": \"Diagonal 42 Sur 24B\", \"Caso_Asociado\": \"SI\", \"Actualizado_En\": null, \"Usuario_Creador_ID\": 2, \"Usuario_Asociado_ID\": \"4\", \"Incidente_ID\": \"1\", \"Estado_Caso_ID\": \"2\", \"Prioridad_ID\": \"2\", \"Barrio_ID\": 7, \"usuario_creador\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 1, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"usuario_asociado\": {\"ID\": 4, \"Nombre\": \"Stmora4123\", \"Correo\": \"smorag@sanmateo.edu.co\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 6, \"Persona\": {\"ID\": 4, \"Documento\": \"1122334411\", \"Primer_Nombre\": \"Steven\", \"Segundo_Nombre\": \"\", \"Primer_Apellido\": \"Mora\", \"Segundo_Apellido\": \"Gomez\"}}, \"incidente\": {\"ID\": 1, \"Incidente\": \"Desplazamiento\", \"Prioridad_ID\": 5}, \"estado\": {\"ID\": 2, \"Nombre\": \"Activo\", \"Creado_En\": \"2026-03-18T03:38:54\"}, \"prioridad\": {\"ID\": 2, \"Prioridad\": \"Baja\"}, \"barrio\": {\"ID\": 7, \"Nombre\": \"Lologro\", \"Localidad\": {\"ID\": 9, \"Nombre\": \"Lologro\", \"Ciudad\": {\"ID\": 6, \"Nombre\": \"Lologro\", \"Departamento\": {\"ID\": 7, \"Nombre\": \"Lologro\"}}}}, \"auditorias\": [], \"radicados\": [{\"ID\": 14, \"Radicado\": \"000013R\", \"Caso_ID\": 18}], \"discusiones\": [], \"casos_asociados\": [{\"ID\": 13, \"Caso_Principal_ID\": 18, \"Creado_En\": \"2026-03-26 20:43:07.638637\", \"Caso_Asociado_ID\": {\"ID\": 1, \"Radicado\": \"000001R\", \"Nombre\": \"CASO ACTIVO 1\", \"Actualizado\": \"2026-03-26 15:42:19\", \"Estado\": \"Activo\"}, \"Tipo_Relacion_ID\": \"Relacionado\", \"Tipo_Relacion_ID_ID\": 1}], \"casos_principales\": []}',2,'2026-03-26 20:43:08',18),(34,'Caso eliminado','{\"ID\": 17, \"Creacion\": \"2026-03-26T00:00:00\", \"Nombre\": \"Caso creado por html\", \"Descripcion\": \"kbkjbvkjv\", \"Afectados\": 143, \"Direccion\": \"Diagonal 42 Sur 24B\", \"Caso_Asociado\": \"SI\", \"Actualizado_En\": null, \"Usuario_Creador_ID\": 2, \"Usuario_Asociado_ID\": 2, \"Incidente_ID\": 1, \"Estado_Caso_ID\": 3, \"Prioridad_ID\": 3, \"Barrio_ID\": 8, \"usuario_creador\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 1, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"usuario_asociado\": {\"ID\": 2, \"Nombre\": \"Sugarrigbi\", \"Correo\": \"sugarrigbi@gmail.com\", \"Estado_Usuario_ID\": 1, \"Rol_ID\": 1, \"Persona\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}, \"incidente\": {\"ID\": 1, \"Incidente\": \"Desplazamiento\", \"Prioridad_ID\": 5}, \"estado\": {\"ID\": 3, \"Nombre\": \"Resuelto\", \"Creado_En\": \"2026-03-18T03:38:54\"}, \"prioridad\": {\"ID\": 3, \"Prioridad\": \"Media\"}, \"barrio\": {\"ID\": 8, \"Nombre\": \"Asdas\", \"Localidad\": {\"ID\": 10, \"Nombre\": \"Bogotá, d.c.\", \"Ciudad\": {\"ID\": 7, \"Nombre\": \"Bogotá, d.c.\", \"Departamento\": {\"ID\": 8, \"Nombre\": \"Asda\"}}}}, \"auditorias\": [{\"Accion\": \"Caso creado\", \"Caso_ID\": 17, \"Fecha_Modificacion\": \"2026-03-26 08:16:18\", \"ID\": 31, \"Modificado_Por\": {\"ID\": 2, \"Documento\": \"1145224601\", \"Primer_Nombre\": \"Kevin\", \"Segundo_Nombre\": \"Mauricio\", \"Primer_Apellido\": \"Anzola\", \"Segundo_Apellido\": \"Garzon\"}}], \"radicados\": [{\"ID\": 13, \"Radicado\": \"000012R\", \"Caso_ID\": 17}], \"discusiones\": [], \"casos_asociados\": [], \"casos_principales\": []}',2,'2026-03-26 21:27:24',17);
/*!40000 ALTER TABLE `caso_auditoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `caso_discusion`
--

DROP TABLE IF EXISTS `caso_discusion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caso_discusion` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Caso_ID` int NOT NULL,
  `Usuario_ID` int NOT NULL,
  `MENSAJE` text NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  KEY `Caso_ID` (`Caso_ID`),
  KEY `Usuario_ID` (`Usuario_ID`),
  CONSTRAINT `Fk_Caso_Discucion_ID` FOREIGN KEY (`Caso_ID`) REFERENCES `caso` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Fk_Usuario_Discucion_ID` FOREIGN KEY (`Usuario_ID`) REFERENCES `usuario` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caso_discusion`
--

LOCK TABLES `caso_discusion` WRITE;
/*!40000 ALTER TABLE `caso_discusion` DISABLE KEYS */;
INSERT INTO `caso_discusion` VALUES (1,1,1,'Este caso requiere seguimiento inmediato.','2026-03-18 03:38:54'),(2,1,1,'Se notificó al usuario sobre el cambio de estado.','2026-03-18 03:38:54'),(3,2,1,'El afectado reportó más detalles sobre la dirección.','2026-03-18 03:38:54'),(4,3,1,'Este caso parece duplicado del principal.','2026-03-18 03:38:54'),(5,4,1,'El usuario solicitó actualización del estado.','2026-03-18 03:38:54'),(6,4,1,'Se notificó al usuario vía correo.','2026-03-18 03:38:54'),(7,7,1,'Este caso no tiene relación con otros, pero requiere validación.','2026-03-18 03:38:54'),(8,1,2,'Esto quedo una chimba','2026-03-20 10:06:06'),(9,1,2,'PERRITO LO LOGRASTE','2026-03-21 08:03:14'),(10,1,2,'UST ES UN DURO','2026-03-21 08:03:41'),(11,1,2,'asd','2026-03-21 11:32:02'),(13,1,2,'asd','2026-03-21 19:42:05'),(14,1,2,'Steven mlp','2026-03-21 19:46:17'),(15,1,1,'perrito ust es un mk','2026-03-21 19:47:55'),(16,1,2,'A tu madre','2026-03-21 21:04:39'),(17,1,4,'Que chimba el vicio','2026-03-21 22:42:06'),(18,14,2,'CASO CREADO POR FRONT PERRITO','2026-03-23 05:20:05'),(19,15,2,'Caso creado por html','2026-03-23 05:23:12'),(20,16,2,'asdasda','2026-03-23 05:28:03'),(21,18,2,'CASO CREADO POR JWT','2026-03-26 20:43:08');
/*!40000 ALTER TABLE `caso_discusion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `casos_a_casos`
--

DROP TABLE IF EXISTS `casos_a_casos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `casos_a_casos` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Caso_Principal_ID` int NOT NULL,
  `Caso_Asociado_ID` int NOT NULL,
  `Tipo_Relacion_ID` int NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  KEY `Caso_Principal_ID` (`Caso_Principal_ID`),
  KEY `Caso_Asociado_ID` (`Caso_Asociado_ID`),
  KEY `Tipo_Relacion_ID` (`Tipo_Relacion_ID`),
  CONSTRAINT `Fk_Caso_Asociado_ID` FOREIGN KEY (`Caso_Asociado_ID`) REFERENCES `caso` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Fk_Caso_Principal_ID` FOREIGN KEY (`Caso_Principal_ID`) REFERENCES `caso` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Fk_Tipo_Relacion_ID` FOREIGN KEY (`Tipo_Relacion_ID`) REFERENCES `tipo_relacion` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `casos_a_casos`
--

LOCK TABLES `casos_a_casos` WRITE;
/*!40000 ALTER TABLE `casos_a_casos` DISABLE KEYS */;
INSERT INTO `casos_a_casos` VALUES (1,1,2,1,'2026-03-18 03:38:54'),(8,1,7,1,'2026-03-21 21:04:39'),(9,14,1,1,'2026-03-23 05:20:05'),(10,15,14,2,'2026-03-23 05:23:12'),(11,16,3,1,'2026-03-23 05:28:03'),(12,1,4,3,'2026-03-26 20:42:20'),(13,18,1,1,'2026-03-26 20:43:08');
/*!40000 ALTER TABLE `casos_a_casos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ciudad`
--

DROP TABLE IF EXISTS `ciudad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ciudad` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(70) NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  `Departamento_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `UQ_NombreDepartamento_ID` (`Nombre`,`Departamento_ID`),
  KEY `Departamento_ID` (`Departamento_ID`),
  CONSTRAINT `Fk_Departamento_ID` FOREIGN KEY (`Departamento_ID`) REFERENCES `departamento` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ciudad`
--

LOCK TABLES `ciudad` WRITE;
/*!40000 ALTER TABLE `ciudad` DISABLE KEYS */;
INSERT INTO `ciudad` VALUES (1,'Bogota','2026-03-18 03:38:54',1),(2,'Cali','2026-03-20 15:58:35',1),(3,'Medellin','2026-03-21 03:17:25',1),(4,'Medellin2','2026-03-21 03:17:51',3),(5,'Suba','2026-03-21 17:38:39',4),(6,'Lologro','2026-03-23 00:20:04',7),(7,'Bogotá, d.c.','2026-03-26 03:16:17',8);
/*!40000 ALTER TABLE `ciudad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contactanos`
--

DROP TABLE IF EXISTS `contactanos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contactanos` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Telefono` varchar(12) NOT NULL,
  `Correo` varchar(100) NOT NULL,
  `Mensaje` varchar(255) NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  `Tipo_Formulario_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Tipo_Formulario_ID` (`Tipo_Formulario_ID`),
  CONSTRAINT `Fk_Contactanos_Tipo_Formulario_ID` FOREIGN KEY (`Tipo_Formulario_ID`) REFERENCES `tipo_formulario` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contactanos`
--

LOCK TABLES `contactanos` WRITE;
/*!40000 ALTER TABLE `contactanos` DISABLE KEYS */;
INSERT INTO `contactanos` VALUES (1,'Juan Perez','3011234567','juan@email.com','Deseo más información sobre el servicio.','2026-03-18 03:38:54',3);
/*!40000 ALTER TABLE `contactanos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departamento`
--

DROP TABLE IF EXISTS `departamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departamento` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(70) NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  `Pais_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `UQ_Nombre_PaisID` (`Nombre`,`Pais_ID`),
  KEY `Pais_ID` (`Pais_ID`),
  CONSTRAINT `Fk_Pais_ID` FOREIGN KEY (`Pais_ID`) REFERENCES `pais` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departamento`
--

LOCK TABLES `departamento` WRITE;
/*!40000 ALTER TABLE `departamento` DISABLE KEYS */;
INSERT INTO `departamento` VALUES (1,'Bogota D.C','2026-03-18 03:38:54',1),(2,'Bogotá','2026-03-18 16:48:35',1),(3,'Cauca','2026-03-21 03:17:40',1),(4,'Suba','2026-03-21 17:38:39',1),(6,'Dsa','2026-03-22 23:51:37',1),(7,'Lologro','2026-03-23 00:20:04',1),(8,'Asda','2026-03-26 03:16:17',1);
/*!40000 ALTER TABLE `departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dispositivos`
--

DROP TABLE IF EXISTS `dispositivos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dispositivos` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `IP` varchar(15) NOT NULL,
  `Token` varchar(255) NOT NULL,
  `Navegador` varchar(120) NOT NULL,
  `Sistema` varchar(50) NOT NULL,
  `Dispositivo` varchar(120) NOT NULL,
  `Fecha_Conexion` datetime DEFAULT CURRENT_TIMESTAMP,
  `Ultimo_Uso` datetime NOT NULL,
  `Estado_Dispositivo_ID` int NOT NULL,
  `Usuario_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Token` (`Token`),
  KEY `Estado_Dispositivo_ID` (`Estado_Dispositivo_ID`),
  KEY `Usuario_ID` (`Usuario_ID`),
  CONSTRAINT `Fk_Estado_Dispositivo_ID` FOREIGN KEY (`Estado_Dispositivo_ID`) REFERENCES `estado_dispositivo` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Fk_Usuario_Dispositivo_ID` FOREIGN KEY (`Usuario_ID`) REFERENCES `usuario` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dispositivos`
--

LOCK TABLES `dispositivos` WRITE;
/*!40000 ALTER TABLE `dispositivos` DISABLE KEYS */;
INSERT INTO `dispositivos` VALUES (1,'192.168.0.1','AS73Uj4$j58kY789kIy89','Brave','Android 16','Tablet','2026-03-18 03:38:54','1999-09-09 00:00:00',1,1),(2,'201.244.139.61','8a30da11fafe39ca7cc82928da5ef03b54ec16f8b8412af40568ae4b0dd80b8b','Opera 128.0.0','Windows','Computador','2026-03-18 16:56:43','2026-03-26 16:28:35',1,2),(3,'201.244.139.61','673e11d1ff14bb35274776429735ad1e62ca281609ae67bd1e5855bad15265e6','Chrome Mobile 146.0.0','Android','Móvil','2026-03-21 14:45:54','2026-03-23 23:46:01',1,2),(4,'186.102.101.163','80bde4e2da9fd28008ef1ebf146a5ad3eabfba07aba1dc3e95e849839bea196b','Mobile Safari 26.3','iOS 18.7','Móvil','2026-03-21 17:39:08','2026-03-21 17:39:08',1,4),(5,'190.26.141.171','cebbc52ba3746289c1b2a12fe1ab8ace77ec640ba0a088e13e3d402dd6337cc9','Chrome 146.0.0','Windows','Computador','2026-03-26 00:14:37','2026-03-26 00:14:38',1,3);
/*!40000 ALTER TABLE `dispositivos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dispositivos_auditoria`
--

DROP TABLE IF EXISTS `dispositivos_auditoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dispositivos_auditoria` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Accion` varchar(100) NOT NULL,
  `Modificado_Por` int NOT NULL,
  `Fecha_Modificacion` datetime DEFAULT CURRENT_TIMESTAMP,
  `Dispositivos_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Dispositivos_ID` (`Dispositivos_ID`),
  KEY `Modificado_Por` (`Modificado_Por`),
  CONSTRAINT `Fk_Dispositivos_Auditoria_ID` FOREIGN KEY (`Dispositivos_ID`) REFERENCES `dispositivos` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Fk_Dispositivos_Modificado_Por` FOREIGN KEY (`Modificado_Por`) REFERENCES `usuario` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dispositivos_auditoria`
--

LOCK TABLES `dispositivos_auditoria` WRITE;
/*!40000 ALTER TABLE `dispositivos_auditoria` DISABLE KEYS */;
INSERT INTO `dispositivos_auditoria` VALUES (1,'Creacion de DDispositivo',1,'2026-03-18 03:38:54',1);
/*!40000 ALTER TABLE `dispositivos_auditoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `entidad`
--

DROP TABLE IF EXISTS `entidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `entidad` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Direccion` varchar(70) NOT NULL,
  `Telefono` varchar(15) NOT NULL,
  `Website` varchar(50) NOT NULL,
  `Descripcion` varchar(255) NOT NULL,
  `Incidente_ID` int NOT NULL,
  `Estado_Entidad_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Incidente_ID` (`Incidente_ID`),
  KEY `Estado_Entidad_ID` (`Estado_Entidad_ID`),
  CONSTRAINT `Fk_Estado_Entidad_ID` FOREIGN KEY (`Estado_Entidad_ID`) REFERENCES `estado_entidad` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Fk_Incidente_ID` FOREIGN KEY (`Incidente_ID`) REFERENCES `incidente` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `entidad`
--

LOCK TABLES `entidad` WRITE;
/*!40000 ALTER TABLE `entidad` DISABLE KEYS */;
INSERT INTO `entidad` VALUES (1,'Empresa de Acueducto','Av. Central #45-10','6011234567','www.acueducto.com','Entidad encargada del suministro de agua.',1,1);
/*!40000 ALTER TABLE `entidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `entidad_auditoria`
--

DROP TABLE IF EXISTS `entidad_auditoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `entidad_auditoria` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Accion` varchar(100) NOT NULL,
  `Modificado_Por` int NOT NULL,
  `Fecha_Modificacion` datetime DEFAULT CURRENT_TIMESTAMP,
  `Entidad_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Entidad_ID` (`Entidad_ID`),
  KEY `Modificado_Por` (`Modificado_Por`),
  CONSTRAINT `Fk_Entidad_Auditoria_ID` FOREIGN KEY (`Entidad_ID`) REFERENCES `entidad` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Fk_Entidad_Modificado_Por` FOREIGN KEY (`Modificado_Por`) REFERENCES `usuario` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `entidad_auditoria`
--

LOCK TABLES `entidad_auditoria` WRITE;
/*!40000 ALTER TABLE `entidad_auditoria` DISABLE KEYS */;
INSERT INTO `entidad_auditoria` VALUES (1,'Creacion de entidad',1,'2026-03-18 03:38:54',1);
/*!40000 ALTER TABLE `entidad_auditoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado_caso`
--

DROP TABLE IF EXISTS `estado_caso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estado_caso` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Nombre` (`Nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado_caso`
--

LOCK TABLES `estado_caso` WRITE;
/*!40000 ALTER TABLE `estado_caso` DISABLE KEYS */;
INSERT INTO `estado_caso` VALUES (1,'Pendiente','2026-03-18 03:38:54'),(2,'Activo','2026-03-18 03:38:54'),(3,'Resuelto','2026-03-18 03:38:54'),(4,'Eliminado','2026-03-18 03:38:54'),(5,'En espera del usuario','2026-03-18 03:38:54'),(6,'Escalado a supervisor','2026-03-18 03:38:54'),(7,'Reabierto','2026-03-18 03:38:54'),(8,'En espera del asesor','2026-03-23 00:46:50'),(9,'Tomando desicion ','2026-03-23 00:46:58');
/*!40000 ALTER TABLE `estado_caso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado_dispositivo`
--

DROP TABLE IF EXISTS `estado_dispositivo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estado_dispositivo` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Nombre` (`Nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado_dispositivo`
--

LOCK TABLES `estado_dispositivo` WRITE;
/*!40000 ALTER TABLE `estado_dispositivo` DISABLE KEYS */;
INSERT INTO `estado_dispositivo` VALUES (1,'Activo','2026-03-18 03:38:54'),(2,'Inactivo','2026-03-18 03:38:54'),(3,'Eliminado','2026-03-18 03:38:54');
/*!40000 ALTER TABLE `estado_dispositivo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado_entidad`
--

DROP TABLE IF EXISTS `estado_entidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estado_entidad` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Nombre` (`Nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado_entidad`
--

LOCK TABLES `estado_entidad` WRITE;
/*!40000 ALTER TABLE `estado_entidad` DISABLE KEYS */;
INSERT INTO `estado_entidad` VALUES (1,'Activa','2026-03-18 03:38:54'),(2,'Inactiva','2026-03-18 03:38:54'),(3,'Suspendida','2026-03-18 03:38:54'),(4,'Eliminada','2026-03-18 03:38:54');
/*!40000 ALTER TABLE `estado_entidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado_usuario`
--

DROP TABLE IF EXISTS `estado_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estado_usuario` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Nombre` (`Nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado_usuario`
--

LOCK TABLES `estado_usuario` WRITE;
/*!40000 ALTER TABLE `estado_usuario` DISABLE KEYS */;
INSERT INTO `estado_usuario` VALUES (1,'Activo','2026-03-18 03:38:54'),(2,'Inactivo','2026-03-18 03:38:54'),(3,'Suspendido','2026-03-18 03:38:54'),(4,'Bloqueado','2026-03-18 03:38:54'),(5,'Eliminado','2026-03-18 03:38:54');
/*!40000 ALTER TABLE `estado_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `incidente`
--

DROP TABLE IF EXISTS `incidente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `incidente` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Incidente` varchar(40) NOT NULL,
  `Prioridad_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Prioridad_ID` (`Prioridad_ID`),
  CONSTRAINT `Fk_Prioridad_ID` FOREIGN KEY (`Prioridad_ID`) REFERENCES `prioridad` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `incidente`
--

LOCK TABLES `incidente` WRITE;
/*!40000 ALTER TABLE `incidente` DISABLE KEYS */;
INSERT INTO `incidente` VALUES (1,'Desplazamiento',5),(2,'Predios Despojados',5),(3,'Expropiacion',4),(4,'Hurto',3);
/*!40000 ALTER TABLE `incidente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `localidad`
--

DROP TABLE IF EXISTS `localidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `localidad` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(70) NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  `Ciudad_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `UQ_Nombre_CiudadID` (`Nombre`,`Ciudad_ID`),
  KEY `Ciudad_ID` (`Ciudad_ID`),
  CONSTRAINT `Fk_Ciudad_ID` FOREIGN KEY (`Ciudad_ID`) REFERENCES `ciudad` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `localidad`
--

LOCK TABLES `localidad` WRITE;
/*!40000 ALTER TABLE `localidad` DISABLE KEYS */;
INSERT INTO `localidad` VALUES (1,'Rafael Uribe Uribe','2026-03-18 03:38:54',1),(2,'Sapo','2026-03-20 15:54:59',1),(3,'Usme','2026-03-21 03:14:22',1),(4,'Bosa','2026-03-21 03:14:59',1),(5,'Santa','2026-03-21 03:15:42',1),(6,'Suba','2026-03-21 17:38:39',5),(8,'Asd','2026-03-22 23:51:37',4),(9,'Lologro','2026-03-23 00:20:04',6),(10,'Bogotá, d.c.','2026-03-26 03:16:17',7);
/*!40000 ALTER TABLE `localidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pais`
--

DROP TABLE IF EXISTS `pais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pais` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(70) NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pais`
--

LOCK TABLES `pais` WRITE;
/*!40000 ALTER TABLE `pais` DISABLE KEYS */;
INSERT INTO `pais` VALUES (1,'Colombia','2026-03-18 03:38:54');
/*!40000 ALTER TABLE `pais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permiso`
--

DROP TABLE IF EXISTS `permiso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `permiso` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Permiso` varchar(50) NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Permiso` (`Permiso`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permiso`
--

LOCK TABLES `permiso` WRITE;
/*!40000 ALTER TABLE `permiso` DISABLE KEYS */;
INSERT INTO `permiso` VALUES (1,'caso_crear','2026-03-25 22:55:21'),(2,'caso_ver','2026-03-25 22:55:21'),(3,'caso_editar','2026-03-25 22:55:21'),(4,'caso_eliminar','2026-03-25 22:55:21'),(5,'caso_ver_propio','2026-03-25 22:55:21'),(6,'caso_relacionar','2026-03-25 22:55:21'),(7,'caso_desrelacionar','2026-03-25 22:55:21'),(8,'caso_modificar_estado','2026-03-25 22:55:21'),(9,'caso_modificar_direccion','2026-03-25 22:55:21'),(10,'caso_asignar_usuario','2026-03-25 22:55:21'),(11,'caso_ver_linea_tiempo','2026-03-25 22:55:21'),(12,'caso_comentar','2026-03-25 22:55:21');
/*!40000 ALTER TABLE `permiso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `persona`
--

DROP TABLE IF EXISTS `persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `persona` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Tipo_Documento_ID` int NOT NULL,
  `Documento` varchar(20) NOT NULL,
  `Primer_Nombre` varchar(50) NOT NULL,
  `Segundo_Nombre` varchar(50) DEFAULT NULL,
  `Primer_Apellido` varchar(50) NOT NULL,
  `Segundo_Apellido` varchar(50) DEFAULT NULL,
  `Direccion` varchar(255) NOT NULL,
  `Telefono` varchar(15) NOT NULL,
  `Terminos_Condiciones` tinyint NOT NULL,
  `Fecha_Nacimiento` date NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  `Actualizado_En` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `Usuario_ID` int NOT NULL,
  `Barrio_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Usuario_ID` (`Usuario_ID`),
  UNIQUE KEY `UQ_TipoDocumento_Documento` (`Tipo_Documento_ID`,`Documento`),
  KEY `Tipo_Documento_ID` (`Tipo_Documento_ID`),
  KEY `Usuario_ID_2` (`Usuario_ID`),
  KEY `Barrio_ID` (`Barrio_ID`),
  CONSTRAINT `Fk_Barrio_ID` FOREIGN KEY (`Barrio_ID`) REFERENCES `barrio` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Fk_Tipo_Documento_ID` FOREIGN KEY (`Tipo_Documento_ID`) REFERENCES `tipo_documento` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Fk_Usuario_ID` FOREIGN KEY (`Usuario_ID`) REFERENCES `usuario` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persona`
--

LOCK TABLES `persona` WRITE;
/*!40000 ALTER TABLE `persona` DISABLE KEYS */;
INSERT INTO `persona` VALUES (1,1,'1111111111','Admin','','Admin','Admin','Dg Admin #13-20','3011111111',1,'1999-09-09','2026-03-18 03:38:54','2026-03-20 09:57:32',1,1),(2,1,'1145224601','Kevin','Mauricio','Anzola','Garzon','Dg 49 sur#13h-20','3144048151',1,'2007-08-26','2026-03-18 16:48:36',NULL,2,1),(3,1,'1014193459','Diana','Breayeth','Anzola','Garzon','Dg 49 sur#13h-20','3144048151',1,'2007-08-26','2026-03-18 21:57:09',NULL,3,1),(4,1,'1122334411','Steven','','Mora','Gomez','Carrera 7','3028293399',1,'1989-03-21','2026-03-21 17:38:39',NULL,4,6);
/*!40000 ALTER TABLE `persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `persona_auditoria`
--

DROP TABLE IF EXISTS `persona_auditoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `persona_auditoria` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Accion` varchar(100) NOT NULL,
  `Modificado_Por` int NOT NULL,
  `Fecha_Modificacion` datetime DEFAULT CURRENT_TIMESTAMP,
  `Persona_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Persona_ID` (`Persona_ID`),
  KEY `Modificado_Por` (`Modificado_Por`),
  CONSTRAINT `Fk_Persona_Auditoria_ID` FOREIGN KEY (`Persona_ID`) REFERENCES `persona` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Fk_Persona_Modificado_Por` FOREIGN KEY (`Modificado_Por`) REFERENCES `usuario` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persona_auditoria`
--

LOCK TABLES `persona_auditoria` WRITE;
/*!40000 ALTER TABLE `persona_auditoria` DISABLE KEYS */;
INSERT INTO `persona_auditoria` VALUES (1,'Creacion de Persona',1,'2026-03-18 03:38:54',1);
/*!40000 ALTER TABLE `persona_auditoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prioridad`
--

DROP TABLE IF EXISTS `prioridad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prioridad` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Prioridad` varchar(30) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prioridad`
--

LOCK TABLES `prioridad` WRITE;
/*!40000 ALTER TABLE `prioridad` DISABLE KEYS */;
INSERT INTO `prioridad` VALUES (1,'Muy Baja'),(2,'Baja'),(3,'Media'),(4,'Alta'),(5,'Critica');
/*!40000 ALTER TABLE `prioridad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `radicado_caso`
--

DROP TABLE IF EXISTS `radicado_caso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `radicado_caso` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Radicado` varchar(40) NOT NULL,
  `Caso_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Radicado` (`Radicado`),
  KEY `Caso_ID` (`Caso_ID`),
  CONSTRAINT `Fk_Caso_ID` FOREIGN KEY (`Caso_ID`) REFERENCES `caso` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `radicado_caso`
--

LOCK TABLES `radicado_caso` WRITE;
/*!40000 ALTER TABLE `radicado_caso` DISABLE KEYS */;
INSERT INTO `radicado_caso` VALUES (1,'000001R',1),(2,'000002R',2),(3,'000003R',3),(4,'000004R',4),(5,'000005R',5),(6,'000006R',6),(7,'000007R',7),(9,'000008R',13),(10,'000009R',14),(11,'000010R',15),(12,'000011R',16),(13,'000012R',17),(14,'000013R',18);
/*!40000 ALTER TABLE `radicado_caso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rol`
--

DROP TABLE IF EXISTS `rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rol` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Nombre` (`Nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rol`
--

LOCK TABLES `rol` WRITE;
/*!40000 ALTER TABLE `rol` DISABLE KEYS */;
INSERT INTO `rol` VALUES (1,'Administrador','2026-03-25 22:56:19'),(2,'Lider','2026-03-25 22:56:19'),(3,'Analista','2026-03-25 22:56:19'),(4,'Auxiliar','2026-03-25 22:56:19'),(5,'Revisor','2026-03-25 22:56:19'),(6,'Usuario','2026-03-25 22:56:19');
/*!40000 ALTER TABLE `rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rol_a_permiso`
--

DROP TABLE IF EXISTS `rol_a_permiso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rol_a_permiso` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Rol_ID` int NOT NULL,
  `Permiso_ID` int NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  KEY `Rol_ID` (`Rol_ID`),
  KEY `Permiso_ID` (`Permiso_ID`),
  CONSTRAINT `Fk_Rol_Permiso1` FOREIGN KEY (`Rol_ID`) REFERENCES `rol` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Fk_Rol_Permiso2` FOREIGN KEY (`Permiso_ID`) REFERENCES `permiso` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rol_a_permiso`
--

LOCK TABLES `rol_a_permiso` WRITE;
/*!40000 ALTER TABLE `rol_a_permiso` DISABLE KEYS */;
INSERT INTO `rol_a_permiso` VALUES (1,1,1,'2026-03-26 00:43:42'),(2,1,2,'2026-03-26 00:43:42'),(3,1,3,'2026-03-26 00:43:42'),(4,1,4,'2026-03-26 00:43:42'),(5,1,6,'2026-03-26 00:43:42'),(6,1,7,'2026-03-26 00:43:42'),(7,1,8,'2026-03-26 00:43:42'),(8,1,9,'2026-03-26 00:43:42'),(9,1,10,'2026-03-26 00:43:42'),(10,1,11,'2026-03-26 00:43:42'),(11,1,12,'2026-03-26 00:43:42'),(12,2,1,'2026-03-26 00:43:42'),(13,2,2,'2026-03-26 00:43:42'),(14,2,3,'2026-03-26 00:43:42'),(15,2,4,'2026-03-26 00:43:42'),(16,2,6,'2026-03-26 00:43:42'),(17,2,7,'2026-03-26 00:43:42'),(18,2,8,'2026-03-26 00:43:42'),(19,2,10,'2026-03-26 00:43:42'),(20,2,11,'2026-03-26 00:43:42'),(21,2,12,'2026-03-26 00:43:42'),(22,3,1,'2026-03-26 00:43:42'),(23,3,2,'2026-03-26 00:43:42'),(24,3,3,'2026-03-26 00:43:42'),(25,3,6,'2026-03-26 00:43:42'),(26,3,7,'2026-03-26 00:43:42'),(27,3,8,'2026-03-26 00:43:42'),(28,3,10,'2026-03-26 00:43:42'),(29,3,11,'2026-03-26 00:43:42'),(30,3,12,'2026-03-26 00:43:42'),(31,4,1,'2026-03-26 00:43:42'),(32,4,2,'2026-03-26 00:43:42'),(33,4,3,'2026-03-26 00:43:42'),(34,4,6,'2026-03-26 00:43:42'),(35,4,7,'2026-03-26 00:43:42'),(36,4,11,'2026-03-26 00:43:42'),(37,4,12,'2026-03-26 00:43:42'),(38,5,2,'2026-03-26 00:43:42'),(39,5,11,'2026-03-26 00:43:42'),(40,6,1,'2026-03-26 00:43:42'),(41,6,5,'2026-03-26 00:43:42');
/*!40000 ALTER TABLE `rol_a_permiso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_documento`
--

DROP TABLE IF EXISTS `tipo_documento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_documento` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Abreviatura` varchar(10) NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Nombre` (`Nombre`),
  UNIQUE KEY `Abreviatura` (`Abreviatura`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_documento`
--

LOCK TABLES `tipo_documento` WRITE;
/*!40000 ALTER TABLE `tipo_documento` DISABLE KEYS */;
INSERT INTO `tipo_documento` VALUES (1,'Cedula de Ciudadania','CC','2026-03-18 03:38:54'),(2,'Cedula de Extranjeria','CE','2026-03-18 03:38:54'),(3,'Pasaporte','PA','2026-03-18 03:38:54'),(4,'Tarjeta de Identidad','TI','2026-03-18 03:38:54'),(5,'Registro Civil','RC','2026-03-18 03:38:54');
/*!40000 ALTER TABLE `tipo_documento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_formulario`
--

DROP TABLE IF EXISTS `tipo_formulario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_formulario` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_formulario`
--

LOCK TABLES `tipo_formulario` WRITE;
/*!40000 ALTER TABLE `tipo_formulario` DISABLE KEYS */;
INSERT INTO `tipo_formulario` VALUES (1,'Calificanos','2026-03-18 03:38:54'),(2,'Ayuda','2026-03-18 03:38:54'),(3,'Contactanos','2026-03-18 03:38:54');
/*!40000 ALTER TABLE `tipo_formulario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_relacion`
--

DROP TABLE IF EXISTS `tipo_relacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_relacion` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Nombre` (`Nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_relacion`
--

LOCK TABLES `tipo_relacion` WRITE;
/*!40000 ALTER TABLE `tipo_relacion` DISABLE KEYS */;
INSERT INTO `tipo_relacion` VALUES (1,'Relacionado','2026-03-18 03:38:54'),(2,'Duplicado','2026-03-18 03:38:54'),(3,'Dependiente','2026-03-18 03:38:54'),(4,'Eliminado','2026-03-21 04:46:37');
/*!40000 ALTER TABLE `tipo_relacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Correo` varchar(100) NOT NULL,
  `Contraseña` varchar(255) NOT NULL,
  `Intentos_Fallidos` int NOT NULL DEFAULT '0',
  `Bloqueado_Hasta` datetime DEFAULT NULL,
  `Creado_En` datetime DEFAULT CURRENT_TIMESTAMP,
  `Actualizado_En` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `Autenticador` tinyint NOT NULL DEFAULT '0',
  `Autenticador_Secreto` varchar(255) DEFAULT NULL,
  `Estado_Usuario_ID` int NOT NULL,
  `Rol_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Nombre` (`Nombre`),
  UNIQUE KEY `Correo` (`Correo`),
  KEY `Rol_ID` (`Rol_ID`),
  KEY `Estado_Usuario_ID` (`Estado_Usuario_ID`),
  CONSTRAINT `FK_Estado_Usuario_ID` FOREIGN KEY (`Estado_Usuario_ID`) REFERENCES `estado_usuario` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `FK_Rol_ID` FOREIGN KEY (`Rol_ID`) REFERENCES `rol` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Administrador','Administrador@gaialink.online','$2b$12$oQdxiCVMY9AioqBK4BPQZ.lsoVN86442m4weat7OvnXE/B42YVzPS',0,NULL,'2026-03-18 03:38:54','2026-03-21 14:46:55',0,NULL,1,1),(2,'Sugarrigbi','sugarrigbi@gmail.com','$2b$12$oQdxiCVMY9AioqBK4BPQZ.lsoVN86442m4weat7OvnXE/B42YVzPS',0,NULL,'2026-03-18 16:48:36','2026-03-26 16:28:23',0,NULL,1,5),(3,'Sugarrigbi2','kevinanzgarz26@gmail.com','$2b$12$oQdxiCVMY9AioqBK4BPQZ.lsoVN86442m4weat7OvnXE/B42YVzPS',0,NULL,'2026-03-18 21:57:09','2026-03-25 20:20:00',0,NULL,1,6),(4,'Stmora4123','smorag@sanmateo.edu.co','$2b$12$MJTl2nO7Gf1zb6oOvMX.tefO24TjS56HYY4VAbY.fRqy2Y9CAH5cO',0,NULL,'2026-03-21 17:38:39','2026-03-25 20:20:00',0,NULL,1,6);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_auditoria`
--

DROP TABLE IF EXISTS `usuario_auditoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario_auditoria` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Accion` varchar(100) NOT NULL,
  `Modificado_Por` int NOT NULL,
  `Fecha_Modificacion` datetime DEFAULT CURRENT_TIMESTAMP,
  `Usuario_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Usuario_ID` (`Usuario_ID`),
  KEY `Modificado_Por` (`Modificado_Por`),
  CONSTRAINT `Fk_Usuario_Auditoria_ID` FOREIGN KEY (`Usuario_ID`) REFERENCES `usuario` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Fk_Usuario_Modificado_Por` FOREIGN KEY (`Modificado_Por`) REFERENCES `usuario` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_auditoria`
--

LOCK TABLES `usuario_auditoria` WRITE;
/*!40000 ALTER TABLE `usuario_auditoria` DISABLE KEYS */;
INSERT INTO `usuario_auditoria` VALUES (1,'Creacion de Usuario',1,'2026-03-18 03:38:54',1);
/*!40000 ALTER TABLE `usuario_auditoria` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-26 16:42:47
