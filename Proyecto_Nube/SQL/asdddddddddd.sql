-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: biblioteca
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
-- Table structure for table `tbl_add_person`
--

DROP TABLE IF EXISTS `tbl_add_person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_add_person` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Privacy_Terms` tinyint(1) DEFAULT '0',
  `Fk_Person` int DEFAULT NULL,
  `Fk_Contacts` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Fk_Person` (`Fk_Person`),
  KEY `FK_Contacts_2` (`Fk_Contacts`),
  CONSTRAINT `FK_Contacts_2` FOREIGN KEY (`Fk_Contacts`) REFERENCES `tbl_contacts` (`ID`),
  CONSTRAINT `tbl_add_person_ibfk_1` FOREIGN KEY (`Fk_Person`) REFERENCES `tbl_person` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_add_person`
--

LOCK TABLES `tbl_add_person` WRITE;
/*!40000 ALTER TABLE `tbl_add_person` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_add_person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_address`
--

DROP TABLE IF EXISTS `tbl_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_address` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Address` text,
  `Country` varchar(50) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_address`
--

LOCK TABLES `tbl_address` WRITE;
/*!40000 ALTER TABLE `tbl_address` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_authors`
--

DROP TABLE IF EXISTS `tbl_authors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_authors` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `First_Name` varchar(50) NOT NULL,
  `Last_Name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_authors`
--

LOCK TABLES `tbl_authors` WRITE;
/*!40000 ALTER TABLE `tbl_authors` DISABLE KEYS */;
INSERT INTO `tbl_authors` VALUES (1,'Autor1','Apellido1'),(2,'Autor2','Apellido2'),(3,'Autor3','Apellido3'),(4,'Autor4','Apellido4'),(5,'Autor5','Apellido5'),(6,'Autor6','Apellido6'),(7,'Autor7','Apellido7'),(8,'Autor8','Apellido8'),(9,'Autor9','Apellido9'),(10,'Autor10','Apellido10'),(11,'Autor11','Apellido11'),(12,'Autor12','Apellido12'),(13,'Autor13','Apellido13'),(14,'Autor14','Apellido14'),(15,'Autor15','Apellido15'),(16,'Autor16','Apellido16'),(17,'Autor17','Apellido17'),(18,'Autor18','Apellido18'),(19,'Autor19','Apellido19'),(20,'Autor20','Apellido20'),(21,'Autor21','Apellido21'),(22,'Autor22','Apellido22'),(23,'Autor23','Apellido23'),(24,'Autor24','Apellido24'),(25,'Autor25','Apellido25'),(26,'Autor26','Apellido26'),(27,'Autor27','Apellido27'),(28,'Autor28','Apellido28'),(29,'Autor29','Apellido29'),(30,'Autor30','Apellido30'),(31,'Autor31','Apellido31'),(32,'Autor32','Apellido32'),(33,'Autor33','Apellido33'),(34,'Autor34','Apellido34'),(35,'Autor35','Apellido35'),(36,'Autor36','Apellido36'),(37,'Autor37','Apellido37'),(38,'Autor38','Apellido38'),(39,'Autor39','Apellido39'),(40,'Autor40','Apellido40'),(41,'Autor41','Apellido41'),(42,'Autor42','Apellido42'),(43,'Autor43','Apellido43'),(44,'Autor44','Apellido44'),(45,'Autor45','Apellido45'),(46,'Autor46','Apellido46'),(47,'Autor47','Apellido47'),(48,'Autor48','Apellido48'),(49,'Autor49','Apellido49'),(50,'Autor50','Apellido50'),(51,'Autor51','Apellido51'),(52,'Autor52','Apellido52'),(53,'Autor53','Apellido53'),(54,'Autor54','Apellido54'),(55,'Autor55','Apellido55'),(56,'Autor56','Apellido56'),(57,'Autor57','Apellido57'),(58,'Autor58','Apellido58'),(59,'Autor59','Apellido59'),(60,'Autor60','Apellido60'),(61,'Autor61','Apellido61'),(62,'Autor62','Apellido62'),(63,'Autor63','Apellido63'),(64,'Autor64','Apellido64'),(65,'Autor65','Apellido65'),(66,'Autor66','Apellido66'),(67,'Autor67','Apellido67'),(68,'Autor68','Apellido68'),(69,'Autor69','Apellido69'),(70,'Autor70','Apellido70'),(71,'Autor71','Apellido71'),(72,'Autor72','Apellido72'),(73,'Autor73','Apellido73'),(74,'Autor74','Apellido74'),(75,'Autor75','Apellido75'),(76,'Autor76','Apellido76'),(77,'Autor77','Apellido77'),(78,'Autor78','Apellido78'),(79,'Autor79','Apellido79'),(80,'Autor80','Apellido80'),(81,'Autor81','Apellido81'),(82,'Autor82','Apellido82'),(83,'Autor83','Apellido83'),(84,'Autor84','Apellido84'),(85,'Autor85','Apellido85'),(86,'Autor86','Apellido86'),(87,'Autor87','Apellido87'),(88,'Autor88','Apellido88'),(89,'Autor89','Apellido89'),(90,'Autor90','Apellido90'),(91,'Autor91','Apellido91'),(92,'Autor92','Apellido92'),(93,'Autor93','Apellido93'),(94,'Autor94','Apellido94'),(95,'Autor95','Apellido95'),(96,'Autor96','Apellido96'),(97,'Autor97','Apellido97'),(98,'Autor98','Apellido98'),(99,'Autor99','Apellido99'),(100,'Autor100','Apellido100');
/*!40000 ALTER TABLE `tbl_authors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_book_authors`
--

DROP TABLE IF EXISTS `tbl_book_authors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_book_authors` (
  `Fk_Book` int NOT NULL,
  `Fk_Author` int NOT NULL,
  PRIMARY KEY (`Fk_Book`,`Fk_Author`),
  KEY `Fk_Author` (`Fk_Author`),
  CONSTRAINT `tbl_book_authors_ibfk_1` FOREIGN KEY (`Fk_Book`) REFERENCES `tbl_books` (`ID`),
  CONSTRAINT `tbl_book_authors_ibfk_2` FOREIGN KEY (`Fk_Author`) REFERENCES `tbl_authors` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_book_authors`
--

LOCK TABLES `tbl_book_authors` WRITE;
/*!40000 ALTER TABLE `tbl_book_authors` DISABLE KEYS */;
INSERT INTO `tbl_book_authors` VALUES (41,41),(44,44),(45,45),(46,46),(47,47),(48,48),(50,50),(51,51),(52,52),(53,53),(54,54),(55,55),(56,56),(57,57),(58,58),(59,59),(60,60),(61,61),(62,62),(63,63),(64,64),(65,65),(66,66),(67,67),(68,68),(69,69),(70,70),(71,71),(72,72),(73,73),(74,74),(75,75),(76,76),(77,77),(78,78),(79,79),(80,80);
/*!40000 ALTER TABLE `tbl_book_authors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_book_status`
--

DROP TABLE IF EXISTS `tbl_book_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_book_status` (
  `ID` varchar(20) NOT NULL,
  `Status_Name` varchar(30) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Status_Name` (`Status_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_book_status`
--

LOCK TABLES `tbl_book_status` WRITE;
/*!40000 ALTER TABLE `tbl_book_status` DISABLE KEYS */;
INSERT INTO `tbl_book_status` VALUES ('AVAILABLE','AVAILABLE'),('DAMAGED','DAMAGED'),('LOANED','LOANED'),('LOST','LOST');
/*!40000 ALTER TABLE `tbl_book_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_books`
--

DROP TABLE IF EXISTS `tbl_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_books` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Title` varchar(200) NOT NULL,
  `Isbn` varchar(20) CHARACTER SET ascii COLLATE ascii_general_ci NOT NULL,
  `Publication_Year` int NOT NULL,
  `Pages` int NOT NULL,
  `Language` varchar(30) NOT NULL,
  `Created_At` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Fk_Category` varchar(100) NOT NULL,
  `Fk_Publisher` varchar(100) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Isbn` (`Isbn`),
  KEY `tbl_books_ibfk_1_idx` (`Fk_Category`),
  KEY `tbl_books_ibfk_2_idx` (`Fk_Publisher`),
  CONSTRAINT `tbl_books_ibfk_1` FOREIGN KEY (`Fk_Category`) REFERENCES `tbl_categories` (`ID`),
  CONSTRAINT `tbl_books_ibfk_2` FOREIGN KEY (`Fk_Publisher`) REFERENCES `tbl_publishers` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_books`
--

LOCK TABLES `tbl_books` WRITE;
/*!40000 ALTER TABLE `tbl_books` DISABLE KEYS */;
INSERT INTO `tbl_books` VALUES (41,'Libro 1','1001-XYZ',2001,1,'Español','2026-01-21 21:35:04','Ciencia','Editorial Alfa'),(44,'Libro 4','1004-XYZ',2005,534,'Francés','2026-01-21 21:35:04','Ciencia','Editorial Beta'),(45,'Libro 5','1005-XYZ',2012,290,'Español','2026-01-21 21:35:04','Ciencia','Editorial Alfa'),(46,'Libro 6','1006-XYZ',1995,378,'Inglés','2026-01-21 21:35:04','Ciencia','Editorial Beta'),(47,'Libro 7','1007-XYZ',2007,412,'Español','2026-01-21 21:35:04','Ciencia','Editorial Alfa'),(48,'Libro 8','1008-XYZ',2018,250,'Francés','2026-01-21 21:35:04','Ficción','Editorial Beta'),(50,'Libro 10','1010-XYZ',1999,412,'Inglés','2026-01-21 21:35:04','Historia','Editorial Beta'),(51,'Libro 11','1011-XYZ',2003,478,'Español','2026-01-21 21:35:04','Historia','Editorial Alfa'),(52,'Libro 12','1012-XYZ',2006,351,'Francés','2026-01-21 21:35:04','Historia','Editorial Alfa'),(53,'Libro 13','1013-XYZ',2011,422,'Español','2026-01-21 21:35:04','Ficción','Editorial Beta'),(54,'Libro 14','1014-XYZ',1997,298,'Inglés','2026-01-21 21:35:04','Historia','Editorial Alfa'),(55,'Libro 15','1015-XYZ',2015,361,'Español','2026-01-21 21:35:04','Historia','Editorial Beta'),(56,'Libro 16','1016-XYZ',2004,419,'Francés','2026-01-21 21:35:04','Historia','Editorial Alfa'),(57,'Libro 17','1017-XYZ',2009,505,'Español','2026-01-21 21:35:04','Ciencia','Editorial Beta'),(58,'Libro 18','1018-XYZ',2016,387,'Inglés','2026-01-21 21:35:04','Ficción','Editorial Alfa'),(59,'Libro 19','1019-XYZ',2002,268,'Español','2026-01-21 21:35:04','Historia','Editorial Alfa'),(60,'Libro 20','1020-XYZ',1996,312,'Francés','2026-01-21 21:35:04','Ficción','Editorial Alfa'),(61,'Libro 21','1021-XYZ',2013,479,'Español','2026-01-21 21:35:04','Historia','Editorial Alfa'),(62,'Libro 22','1022-XYZ',2008,334,'Inglés','2026-01-21 21:35:04','Ficción','Editorial Alfa'),(63,'Libro 23','1023-XYZ',2017,411,'Español','2026-01-21 21:35:04','Ficción','Editorial Beta'),(64,'Libro 24','1024-XYZ',1994,295,'Francés','2026-01-21 21:35:04','Ciencia','Editorial Alfa'),(65,'Libro 25','1025-XYZ',2001,376,'Español','2026-01-21 21:35:04','Historia','Editorial Beta'),(66,'Libro 26','1026-XYZ',2019,420,'Inglés','2026-01-21 21:35:04','Historia','Editorial Alfa'),(67,'Libro 27','1027-XYZ',2014,350,'Español','2026-01-21 21:35:04','Ciencia','Editorial Beta'),(68,'Libro 28','1028-XYZ',2007,398,'Francés','2026-01-21 21:35:04','Historia','Editorial Alfa'),(69,'Libro 29','1029-XYZ',2012,310,'Español','2026-01-21 21:35:04','Ficción','Editorial Beta'),(70,'Libro 30','1030-XYZ',2000,440,'Inglés','2026-01-21 21:35:04','Ficción','Editorial Beta'),(71,'Libro 31','1031-XYZ',2005,356,'Español','2026-01-21 21:35:04','Ciencia','Editorial Alfa'),(72,'Libro 32','1032-XYZ',2010,322,'Francés','2026-01-21 21:35:04','Historia','Editorial Beta'),(73,'Libro 33','1033-XYZ',2016,399,'Español','2026-01-21 21:35:04','Ficción','Editorial Alfa'),(74,'Libro 34','1034-XYZ',2008,421,'Inglés','2026-01-21 21:35:04','Ciencia','Editorial Beta'),(75,'Libro 35','1035-XYZ',2013,312,'Español','2026-01-21 21:35:04','Historia','Editorial Alfa'),(76,'Libro 36','1036-XYZ',2015,447,'Francés','2026-01-21 21:35:04','Historia','Editorial Alfa'),(77,'Libro 37','1037-XYZ',2006,360,'Español','2026-01-21 21:35:04','Ciencia','Editorial Beta'),(78,'Libro 38','1038-XYZ',2011,391,'Inglés','2026-01-21 21:35:04','Historia','Editorial Alfa'),(79,'Libro 39','1039-XYZ',2018,430,'Español','2026-01-21 21:35:04','Ficción','Editorial Beta'),(80,'Libro 40','1040-XYZ',2003,312,'Francés','2026-01-21 21:35:04','Ciencia','Editorial Alfa');
/*!40000 ALTER TABLE `tbl_books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_categories`
--

DROP TABLE IF EXISTS `tbl_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_categories` (
  `ID` varchar(100) NOT NULL,
  `Category_Name` varchar(100) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Category_Name` (`Category_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_categories`
--

LOCK TABLES `tbl_categories` WRITE;
/*!40000 ALTER TABLE `tbl_categories` DISABLE KEYS */;
INSERT INTO `tbl_categories` VALUES ('Ciencia','Ciencia'),('Ficción','Ficción'),('Historia','Historia');
/*!40000 ALTER TABLE `tbl_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_contacts`
--

DROP TABLE IF EXISTS `tbl_contacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_contacts` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Email` varchar(100) DEFAULT NULL,
  `Phone` varchar(20) DEFAULT NULL,
  `Fk_Add_Person` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Fk_Add_Person` (`Fk_Add_Person`),
  CONSTRAINT `tbl_contacts_ibfk_1` FOREIGN KEY (`Fk_Add_Person`) REFERENCES `tbl_add_person` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_contacts`
--

LOCK TABLES `tbl_contacts` WRITE;
/*!40000 ALTER TABLE `tbl_contacts` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_contacts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_document_type`
--

DROP TABLE IF EXISTS `tbl_document_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_document_type` (
  `ID` varchar(50) NOT NULL,
  `Document_Type` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Document_Type` (`Document_Type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_document_type`
--

LOCK TABLES `tbl_document_type` WRITE;
/*!40000 ALTER TABLE `tbl_document_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_document_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_inventory`
--

DROP TABLE IF EXISTS `tbl_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_inventory` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Barcode` varchar(50) NOT NULL,
  `Quantity` int NOT NULL,
  `Acquisition_Date` date NOT NULL,
  `Created_At` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Fk_Status` varchar(20) NOT NULL,
  `Fk_Book` int NOT NULL,
  `Fk_Location` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Barcode` (`Barcode`),
  KEY `Fk_Book` (`Fk_Book`),
  KEY `Fk_Status` (`Fk_Status`),
  KEY `tbl_inventory_ibfk_3_idx` (`Fk_Location`),
  CONSTRAINT `tbl_inventory_ibfk_1` FOREIGN KEY (`Fk_Book`) REFERENCES `tbl_books` (`ID`),
  CONSTRAINT `tbl_inventory_ibfk_2` FOREIGN KEY (`Fk_Status`) REFERENCES `tbl_book_status` (`ID`),
  CONSTRAINT `tbl_inventory_ibfk_3` FOREIGN KEY (`Fk_Location`) REFERENCES `tbl_inventory_location` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_inventory`
--

LOCK TABLES `tbl_inventory` WRITE;
/*!40000 ALTER TABLE `tbl_inventory` DISABLE KEYS */;
INSERT INTO `tbl_inventory` VALUES (20,'BC-0005',1,'2024-03-01','2026-01-23 13:37:30','DAMAGED',64,'WAREHOUSE'),(21,'BC-0006',1,'2024-03-15','2026-01-23 13:37:30','AVAILABLE',75,'SHELF-A2'),(22,'BC-0007',1,'2024-03-18','2026-01-23 13:37:30','LOST',70,'WAREHOUSE');
/*!40000 ALTER TABLE `tbl_inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_inventory_history`
--

DROP TABLE IF EXISTS `tbl_inventory_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_inventory_history` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Movement_Date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Notes` varchar(255) NOT NULL,
  `Fk_Performed_By_User` int NOT NULL,
  `Fk_Book_Copy` int NOT NULL,
  `Fk_Previous_Status` varchar(20) NOT NULL,
  `Fk_New_Status` varchar(20) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Fk_Book_Copy` (`Fk_Book_Copy`),
  KEY `tbl_inventory_history_ibfk_2` (`Fk_Previous_Status`),
  KEY `tbl_inventory_history_ibfk_3` (`Fk_New_Status`),
  KEY `tbl_inventory_history_ibfk_4` (`Fk_Performed_By_User`),
  CONSTRAINT `tbl_inventory_history_ibfk_1` FOREIGN KEY (`Fk_Book_Copy`) REFERENCES `tbl_inventory` (`ID`),
  CONSTRAINT `tbl_inventory_history_ibfk_2` FOREIGN KEY (`Fk_Previous_Status`) REFERENCES `tbl_book_status` (`ID`),
  CONSTRAINT `tbl_inventory_history_ibfk_3` FOREIGN KEY (`Fk_New_Status`) REFERENCES `tbl_book_status` (`ID`),
  CONSTRAINT `tbl_inventory_history_ibfk_4` FOREIGN KEY (`Fk_Performed_By_User`) REFERENCES `tbl_user` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_inventory_history`
--

LOCK TABLES `tbl_inventory_history` WRITE;
/*!40000 ALTER TABLE `tbl_inventory_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_inventory_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_inventory_location`
--

DROP TABLE IF EXISTS `tbl_inventory_location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_inventory_location` (
  `ID` varchar(50) NOT NULL,
  `Location_Name` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_inventory_location`
--

LOCK TABLES `tbl_inventory_location` WRITE;
/*!40000 ALTER TABLE `tbl_inventory_location` DISABLE KEYS */;
INSERT INTO `tbl_inventory_location` VALUES ('SHELF-A1','SHELF-A1'),('SHELF-A2','SHELF-A2'),('SHELF-B2','SHELF-B2'),('SHELF-C1','SHELF-C1'),('WAREHOUSE','WAREHOUSE');
/*!40000 ALTER TABLE `tbl_inventory_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_loan_history`
--

DROP TABLE IF EXISTS `tbl_loan_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_loan_history` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Change_Date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `Notes` varchar(255) DEFAULT NULL,
  `Fk_Loan` int NOT NULL,
  `Fk_Previous_Status` varchar(20) DEFAULT NULL,
  `Fk_New_Status` varchar(20) DEFAULT NULL,
  `Fk_Performed_By` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Fk_Loan` (`Fk_Loan`),
  KEY `Fk_Previous_Status` (`Fk_Previous_Status`),
  KEY `Fk_New_Status` (`Fk_New_Status`),
  KEY `Fk_Performed_By` (`Fk_Performed_By`),
  CONSTRAINT `tbl_loan_history_ibfk_1` FOREIGN KEY (`Fk_Loan`) REFERENCES `tbl_loans` (`ID`),
  CONSTRAINT `tbl_loan_history_ibfk_2` FOREIGN KEY (`Fk_Previous_Status`) REFERENCES `tbl_loan_status` (`ID`),
  CONSTRAINT `tbl_loan_history_ibfk_3` FOREIGN KEY (`Fk_New_Status`) REFERENCES `tbl_loan_status` (`ID`),
  CONSTRAINT `tbl_loan_history_ibfk_4` FOREIGN KEY (`Fk_Performed_By`) REFERENCES `tbl_user` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_loan_history`
--

LOCK TABLES `tbl_loan_history` WRITE;
/*!40000 ALTER TABLE `tbl_loan_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_loan_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_loan_status`
--

DROP TABLE IF EXISTS `tbl_loan_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_loan_status` (
  `ID` varchar(20) NOT NULL,
  `Status_Name` varchar(30) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Status_Name` (`Status_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_loan_status`
--

LOCK TABLES `tbl_loan_status` WRITE;
/*!40000 ALTER TABLE `tbl_loan_status` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_loan_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_loans`
--

DROP TABLE IF EXISTS `tbl_loans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_loans` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Loan_Date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `Due_Date` date NOT NULL,
  `Return_Date` date DEFAULT NULL,
  `Fk_Book_Copy` int NOT NULL,
  `Fk_User` int NOT NULL,
  `Fk_Status` varchar(20) NOT NULL,
  `Fk_Created_By` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Fk_Book_Copy` (`Fk_Book_Copy`),
  KEY `Fk_User` (`Fk_User`),
  KEY `Fk_Status` (`Fk_Status`),
  KEY `Fk_Created_By` (`Fk_Created_By`),
  CONSTRAINT `tbl_loans_ibfk_1` FOREIGN KEY (`Fk_Book_Copy`) REFERENCES `tbl_inventory` (`ID`),
  CONSTRAINT `tbl_loans_ibfk_2` FOREIGN KEY (`Fk_User`) REFERENCES `tbl_user` (`ID`),
  CONSTRAINT `tbl_loans_ibfk_3` FOREIGN KEY (`Fk_Status`) REFERENCES `tbl_loan_status` (`ID`),
  CONSTRAINT `tbl_loans_ibfk_4` FOREIGN KEY (`Fk_Created_By`) REFERENCES `tbl_user` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_loans`
--

LOCK TABLES `tbl_loans` WRITE;
/*!40000 ALTER TABLE `tbl_loans` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_loans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_notification_history`
--

DROP TABLE IF EXISTS `tbl_notification_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_notification_history` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Event_Date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `Notes` varchar(255) DEFAULT NULL,
  `Fk_Notification` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Fk_Notification` (`Fk_Notification`),
  CONSTRAINT `tbl_notification_history_ibfk_1` FOREIGN KEY (`Fk_Notification`) REFERENCES `tbl_notifications` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_notification_history`
--

LOCK TABLES `tbl_notification_history` WRITE;
/*!40000 ALTER TABLE `tbl_notification_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_notification_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_notification_status`
--

DROP TABLE IF EXISTS `tbl_notification_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_notification_status` (
  `ID` varchar(20) NOT NULL,
  `Status_Name` varchar(30) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Status_Name` (`Status_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_notification_status`
--

LOCK TABLES `tbl_notification_status` WRITE;
/*!40000 ALTER TABLE `tbl_notification_status` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_notification_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_notifications`
--

DROP TABLE IF EXISTS `tbl_notifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_notifications` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Title` varchar(100) DEFAULT NULL,
  `Message` text NOT NULL,
  `Created_At` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `Fk_Status` varchar(20) NOT NULL,
  `Fk_User` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Fk_User` (`Fk_User`),
  KEY `Fk_Status` (`Fk_Status`),
  CONSTRAINT `tbl_notifications_ibfk_1` FOREIGN KEY (`Fk_User`) REFERENCES `tbl_user` (`ID`),
  CONSTRAINT `tbl_notifications_ibfk_2` FOREIGN KEY (`Fk_Status`) REFERENCES `tbl_notification_status` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_notifications`
--

LOCK TABLES `tbl_notifications` WRITE;
/*!40000 ALTER TABLE `tbl_notifications` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_notifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_penalties`
--

DROP TABLE IF EXISTS `tbl_penalties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_penalties` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Amount` decimal(10,2) NOT NULL,
  `Generated_Date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `Fk_Status` varchar(20) NOT NULL,
  `Fk_Loan` int NOT NULL,
  `Fk_User` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Fk_Loan` (`Fk_Loan`),
  KEY `Fk_User` (`Fk_User`),
  KEY `Fk_Status` (`Fk_Status`),
  CONSTRAINT `tbl_penalties_ibfk_1` FOREIGN KEY (`Fk_Loan`) REFERENCES `tbl_loans` (`ID`),
  CONSTRAINT `tbl_penalties_ibfk_2` FOREIGN KEY (`Fk_User`) REFERENCES `tbl_user` (`ID`),
  CONSTRAINT `tbl_penalties_ibfk_3` FOREIGN KEY (`Fk_Status`) REFERENCES `tbl_penalties_status` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_penalties`
--

LOCK TABLES `tbl_penalties` WRITE;
/*!40000 ALTER TABLE `tbl_penalties` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_penalties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_penalties_history`
--

DROP TABLE IF EXISTS `tbl_penalties_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_penalties_history` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Change_Date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `Fk_Performed_By` int DEFAULT NULL,
  `Fk_Penalty` int NOT NULL,
  `Previous_Status` varchar(20) DEFAULT NULL,
  `New_Status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Fk_Penalty` (`Fk_Penalty`),
  KEY `Previous_Status` (`Previous_Status`),
  KEY `New_Status` (`New_Status`),
  KEY `Fk_Performed_By` (`Fk_Performed_By`),
  CONSTRAINT `tbl_penalties_history_ibfk_1` FOREIGN KEY (`Fk_Penalty`) REFERENCES `tbl_penalties` (`ID`),
  CONSTRAINT `tbl_penalties_history_ibfk_2` FOREIGN KEY (`Previous_Status`) REFERENCES `tbl_penalties_status` (`ID`),
  CONSTRAINT `tbl_penalties_history_ibfk_3` FOREIGN KEY (`New_Status`) REFERENCES `tbl_penalties_status` (`ID`),
  CONSTRAINT `tbl_penalties_history_ibfk_4` FOREIGN KEY (`Fk_Performed_By`) REFERENCES `tbl_user` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_penalties_history`
--

LOCK TABLES `tbl_penalties_history` WRITE;
/*!40000 ALTER TABLE `tbl_penalties_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_penalties_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_penalties_payments`
--

DROP TABLE IF EXISTS `tbl_penalties_payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_penalties_payments` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Payment_Date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `Amount` decimal(10,2) NOT NULL,
  `Payment_Method` varchar(30) DEFAULT NULL,
  `Fk_Penalty` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Fk_Penalty` (`Fk_Penalty`),
  CONSTRAINT `tbl_penalties_payments_ibfk_1` FOREIGN KEY (`Fk_Penalty`) REFERENCES `tbl_penalties` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_penalties_payments`
--

LOCK TABLES `tbl_penalties_payments` WRITE;
/*!40000 ALTER TABLE `tbl_penalties_payments` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_penalties_payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_penalties_status`
--

DROP TABLE IF EXISTS `tbl_penalties_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_penalties_status` (
  `ID` varchar(20) NOT NULL,
  `Status_Name` varchar(30) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Status_Name` (`Status_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_penalties_status`
--

LOCK TABLES `tbl_penalties_status` WRITE;
/*!40000 ALTER TABLE `tbl_penalties_status` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_penalties_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_person`
--

DROP TABLE IF EXISTS `tbl_person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_person` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `First_Name` varchar(50) NOT NULL,
  `Second_Name` varchar(50) DEFAULT NULL,
  `First_LastName` varchar(50) NOT NULL,
  `Second_LastName` varchar(50) DEFAULT NULL,
  `Birth_Date` date DEFAULT NULL,
  `Fk_DocumentType` varchar(50) DEFAULT NULL,
  `Fk_User` int DEFAULT NULL,
  `Fk_Address` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Fk_DocumentType` (`Fk_DocumentType`),
  KEY `Fk_User` (`Fk_User`),
  KEY `fk_person_address` (`Fk_Address`),
  CONSTRAINT `fk_person_address` FOREIGN KEY (`Fk_Address`) REFERENCES `tbl_address` (`ID`),
  CONSTRAINT `tbl_person_ibfk_1` FOREIGN KEY (`Fk_DocumentType`) REFERENCES `tbl_document_type` (`ID`),
  CONSTRAINT `tbl_person_ibfk_2` FOREIGN KEY (`Fk_User`) REFERENCES `tbl_user` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_person`
--

LOCK TABLES `tbl_person` WRITE;
/*!40000 ALTER TABLE `tbl_person` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_publishers`
--

DROP TABLE IF EXISTS `tbl_publishers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_publishers` (
  `ID` varchar(100) NOT NULL,
  `Publisher_Name` varchar(100) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Publisher_Name` (`Publisher_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_publishers`
--

LOCK TABLES `tbl_publishers` WRITE;
/*!40000 ALTER TABLE `tbl_publishers` DISABLE KEYS */;
INSERT INTO `tbl_publishers` VALUES ('Editorial Alfa','Editorial Alfa'),('Editorial Beta','Editorial Beta');
/*!40000 ALTER TABLE `tbl_publishers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_refresh_tokens`
--

DROP TABLE IF EXISTS `tbl_refresh_tokens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_refresh_tokens` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Token` varchar(255) NOT NULL,
  `Expires_At` timestamp NOT NULL,
  `Revoked` tinyint(1) DEFAULT '0',
  `Created_At` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `Fk_User` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Fk_User` (`Fk_User`),
  CONSTRAINT `tbl_refresh_tokens_ibfk_1` FOREIGN KEY (`Fk_User`) REFERENCES `tbl_user` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_refresh_tokens`
--

LOCK TABLES `tbl_refresh_tokens` WRITE;
/*!40000 ALTER TABLE `tbl_refresh_tokens` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_refresh_tokens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_reservation_status`
--

DROP TABLE IF EXISTS `tbl_reservation_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_reservation_status` (
  `ID` varchar(20) NOT NULL,
  `Status_Name` varchar(20) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Status_Name` (`Status_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_reservation_status`
--

LOCK TABLES `tbl_reservation_status` WRITE;
/*!40000 ALTER TABLE `tbl_reservation_status` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_reservation_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_reservations`
--

DROP TABLE IF EXISTS `tbl_reservations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_reservations` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Reservation_Date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `Expiration_Date` timestamp NOT NULL,
  `Fk_Book` int NOT NULL,
  `Fk_User` int NOT NULL,
  `Fk_Status` varchar(20) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Fk_User` (`Fk_User`),
  KEY `Fk_Status` (`Fk_Status`),
  KEY `FK_Book2` (`Fk_Book`),
  CONSTRAINT `FK_Book2` FOREIGN KEY (`Fk_Book`) REFERENCES `tbl_books` (`ID`),
  CONSTRAINT `tbl_reservations_ibfk_1` FOREIGN KEY (`Fk_User`) REFERENCES `tbl_user` (`ID`),
  CONSTRAINT `tbl_reservations_ibfk_2` FOREIGN KEY (`Fk_Status`) REFERENCES `tbl_reservation_status` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_reservations`
--

LOCK TABLES `tbl_reservations` WRITE;
/*!40000 ALTER TABLE `tbl_reservations` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_reservations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_reservations_history`
--

DROP TABLE IF EXISTS `tbl_reservations_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_reservations_history` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Action_Date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `Action` varchar(50) NOT NULL,
  `Fk_Performed_By` int DEFAULT NULL,
  `Fk_Reservation` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Fk_reservation` (`Fk_Reservation`),
  KEY `Performed_By` (`Fk_Performed_By`),
  CONSTRAINT `tbl_reservations_history_ibfk_1` FOREIGN KEY (`Fk_Reservation`) REFERENCES `tbl_reservations` (`ID`),
  CONSTRAINT `tbl_reservations_history_ibfk_2` FOREIGN KEY (`Fk_Performed_By`) REFERENCES `tbl_user` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_reservations_history`
--

LOCK TABLES `tbl_reservations_history` WRITE;
/*!40000 ALTER TABLE `tbl_reservations_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_reservations_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user`
--

DROP TABLE IF EXISTS `tbl_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(50) NOT NULL,
  `Password_Hash` varchar(255) NOT NULL,
  `Created_At` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Is_Blocked` tinyint(1) NOT NULL DEFAULT '0',
  `Failed_Attempts` int NOT NULL DEFAULT '0',
  `Active_2FA` tinyint(1) NOT NULL DEFAULT '0',
  `SecretKey_2FA` varchar(255) NOT NULL DEFAULT '0',
  `Fk_Role` varchar(50) NOT NULL,
  `Fk_State` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Username` (`Username`),
  KEY `Fk_Role` (`Fk_Role`),
  KEY `Fk_State` (`Fk_State`),
  CONSTRAINT `tbl_user_ibfk_1` FOREIGN KEY (`Fk_Role`) REFERENCES `tbl_user_roles` (`ID`),
  CONSTRAINT `tbl_user_ibfk_2` FOREIGN KEY (`Fk_State`) REFERENCES `tbl_user_states` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user`
--

LOCK TABLES `tbl_user` WRITE;
/*!40000 ALTER TABLE `tbl_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_roles`
--

DROP TABLE IF EXISTS `tbl_user_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_roles` (
  `ID` varchar(50) NOT NULL,
  `Role_Name` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Role_Name` (`Role_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_roles`
--

LOCK TABLES `tbl_user_roles` WRITE;
/*!40000 ALTER TABLE `tbl_user_roles` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_user_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_states`
--

DROP TABLE IF EXISTS `tbl_user_states`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_states` (
  `ID` varchar(50) NOT NULL,
  `State_Name` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `State_Name` (`State_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_states`
--

LOCK TABLES `tbl_user_states` WRITE;
/*!40000 ALTER TABLE `tbl_user_states` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_user_states` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-01-23 12:51:07
