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
  PRIMARY KEY (`ID`),
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
  `First_Name` varchar(50) DEFAULT NULL,
  `Last_Name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_authors`
--

LOCK TABLES `tbl_authors` WRITE;
/*!40000 ALTER TABLE `tbl_authors` DISABLE KEYS */;
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
/*!40000 ALTER TABLE `tbl_book_authors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_book_copies`
--

DROP TABLE IF EXISTS `tbl_book_copies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_book_copies` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Barcode` varchar(50) DEFAULT NULL,
  `Acquisition_Date` timestamp DEFAULT NULL,
  `Location` varchar(50) DEFAULT NULL,
  `Created_At` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `Fk_Status` varchar(20) NOT NULL,
  `Fk_Book` int NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Barcode` (`Barcode`),
  KEY `Fk_Book` (`Fk_Book`),
  KEY `Fk_Status` (`Fk_Status`),
  CONSTRAINT `tbl_book_copies_ibfk_1` FOREIGN KEY (`Fk_Book`) REFERENCES `tbl_books` (`ID`),
  CONSTRAINT `tbl_book_copies_ibfk_2` FOREIGN KEY (`Fk_Status`) REFERENCES `tbl_book_status` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_book_copies`
--

LOCK TABLES `tbl_book_copies` WRITE;
/*!40000 ALTER TABLE `tbl_book_copies` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_book_copies` ENABLE KEYS */;
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
  `Isbn` varchar(20) DEFAULT NULL,
  `Publication_Year` int DEFAULT NULL,
  `Pages` int DEFAULT NULL,
  `Language` varchar(30) DEFAULT NULL,
  `Created_At` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `Fk_Category` int DEFAULT NULL,
  `Fk_Publisher` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Isbn` (`Isbn`),
  KEY `Fk_Category` (`Fk_Category`),
  KEY `Fk_Publisher` (`Fk_Publisher`),
  CONSTRAINT `tbl_books_ibfk_1` FOREIGN KEY (`Fk_Category`) REFERENCES `tbl_categories` (`ID`),
  CONSTRAINT `tbl_books_ibfk_2` FOREIGN KEY (`Fk_Publisher`) REFERENCES `tbl_publishers` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_books`
--

LOCK TABLES `tbl_books` WRITE;
/*!40000 ALTER TABLE `tbl_books` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_categories`
--

DROP TABLE IF EXISTS `tbl_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_categories` (
  `ID` int NOT NULL AUTO_INCREMENT,
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
-- Table structure for table `tbl_fine_history`
--

DROP TABLE IF EXISTS `tbl_fine_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_fine_history` (
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
  CONSTRAINT `tbl_fine_history_ibfk_1` FOREIGN KEY (`Fk_Penalty`) REFERENCES `tbl_penalties` (`ID`),
  CONSTRAINT `tbl_fine_history_ibfk_2` FOREIGN KEY (`Previous_Status`) REFERENCES `tbl_penalties_status` (`ID`),
  CONSTRAINT `tbl_fine_history_ibfk_3` FOREIGN KEY (`New_Status`) REFERENCES `tbl_penalties_status` (`ID`),
  CONSTRAINT `tbl_fine_history_ibfk_4` FOREIGN KEY (`Fk_Performed_By`) REFERENCES `tbl_user` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_fine_history`
--

LOCK TABLES `tbl_fine_history` WRITE;
/*!40000 ALTER TABLE `tbl_fine_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_fine_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_inventory_movements`
--

DROP TABLE IF EXISTS `tbl_inventory_movements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_inventory_movements` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Movement_Date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `Notes` varchar(255) DEFAULT NULL,
  `Fk_Performed_By_User` int DEFAULT NULL,
  `Fk_Book_Copy` int NOT NULL,
  `Fk_Previous_Status` varchar(20) DEFAULT NULL,
  `Fk_New_Status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Fk_Book_Copy` (`Fk_Book_Copy`),
  KEY `Fk_Previous_Status` (`Fk_Previous_Status`),
  KEY `Fk_New_Status` (`Fk_New_Status`),
  KEY `Fk_Performed_By_User` (`Fk_Performed_By_User`),
  CONSTRAINT `tbl_inventory_movements_ibfk_1` FOREIGN KEY (`Fk_Book_Copy`) REFERENCES `tbl_book_copies` (`ID`),
  CONSTRAINT `tbl_inventory_movements_ibfk_2` FOREIGN KEY (`Fk_Previous_Status`) REFERENCES `tbl_book_status` (`ID`),
  CONSTRAINT `tbl_inventory_movements_ibfk_3` FOREIGN KEY (`Fk_New_Status`) REFERENCES `tbl_book_status` (`ID`),
  CONSTRAINT `tbl_inventory_movements_ibfk_4` FOREIGN KEY (`Fk_Performed_By_User`) REFERENCES `tbl_user` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_inventory_movements`
--

LOCK TABLES `tbl_inventory_movements` WRITE;
/*!40000 ALTER TABLE `tbl_inventory_movements` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_inventory_movements` ENABLE KEYS */;
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
  `Due_Date` DATE NOT NULL,
  `Return_Date` timestamp DEFAULT NULL,
  `Fk_Book_Copy` int NOT NULL,
  `Fk_User` int NOT NULL,
  `Fk_Status` varchar(20) NOT NULL,
  `Fk_Created_By` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Fk_Book_Copy` (`Fk_Book_Copy`),
  KEY `Fk_User` (`Fk_User`),
  KEY `Fk_Status` (`Fk_Status`),
  KEY `Fk_Created_By` (`Fk_Created_By`),
  CONSTRAINT `tbl_loans_ibfk_1` FOREIGN KEY (`Fk_Book_Copy`) REFERENCES `tbl_book_copies` (`ID`),
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
  `Birth_Date` DATE DEFAULT NULL,
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
  `ID` int NOT NULL AUTO_INCREMENT,
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
  `Created_At` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `Is_Blocked` tinyint(1) DEFAULT '0',
  `Failed_Attempts` int DEFAULT '0',
  `Active_2FA` tinyint(1) DEFAULT '0',
  `SecretKey_2FA` varchar(255) DEFAULT NULL,
  `Fk_Role` varchar(50) DEFAULT NULL,
  `Fk_State` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Username` (`Username`),
  KEY `Fk_Role` (`Fk_Role`),
  KEY `Fk_State` (`Fk_State`),
  CONSTRAINT `tbl_user_ibfk_1` FOREIGN KEY (`Fk_Role`) REFERENCES `tbl_user_roles` (`ID`),
  CONSTRAINT `tbl_user_ibfk_2` FOREIGN KEY (`Fk_State`) REFERENCES `tbl_user_states` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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

-- Dump completed on 2026-01-15 11:32:09
