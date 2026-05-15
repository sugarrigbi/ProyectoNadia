-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: san_mateo_academico
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
-- Table structure for table `academic_periods`
--

DROP TABLE IF EXISTS `academic_periods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `academic_periods` (
  `period_id` int NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `status` enum('OPEN','CLOSED') NOT NULL DEFAULT 'OPEN',
  PRIMARY KEY (`period_id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `academic_periods`
--

LOCK TABLES `academic_periods` WRITE;
/*!40000 ALTER TABLE `academic_periods` DISABLE KEYS */;
INSERT INTO `academic_periods` VALUES (1,'2026-1','2026-02-01','2026-06-15','OPEN'),(2,'2025-2','2025-08-01','2025-12-15','CLOSED');
/*!40000 ALTER TABLE `academic_periods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `assessments`
--

DROP TABLE IF EXISTS `assessments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `assessments` (
  `assessment_id` int NOT NULL AUTO_INCREMENT,
  `section_id` int NOT NULL,
  `name` varchar(80) NOT NULL,
  `weight_pct` decimal(5,2) NOT NULL,
  `due_date` date DEFAULT NULL,
  PRIMARY KEY (`assessment_id`),
  KEY `fk_assessment_section` (`section_id`),
  CONSTRAINT `fk_assessment_section` FOREIGN KEY (`section_id`) REFERENCES `course_sections` (`section_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assessments`
--

LOCK TABLES `assessments` WRITE;
/*!40000 ALTER TABLE `assessments` DISABLE KEYS */;
INSERT INTO `assessments` VALUES (1,1,'Parcial 1',30.00,'2026-03-10'),(2,1,'Parcial 2',30.00,'2026-04-20'),(3,1,'Proyecto Final',40.00,'2026-06-05'),(4,2,'Parcial 1',35.00,'2026-03-12'),(5,2,'Parcial 2',25.00,'2026-04-25'),(6,2,'Proyecto Final',40.00,'2026-06-06');
/*!40000 ALTER TABLE `assessments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course_sections`
--

DROP TABLE IF EXISTS `course_sections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course_sections` (
  `section_id` int NOT NULL AUTO_INCREMENT,
  `course_id` int NOT NULL,
  `period_id` int NOT NULL,
  `teacher_id` int NOT NULL,
  `group_code` varchar(10) NOT NULL,
  `capacity` smallint NOT NULL DEFAULT '30',
  `needs_reassign` tinyint(1) NOT NULL DEFAULT '0',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`section_id`),
  UNIQUE KEY `course_id` (`course_id`,`period_id`,`group_code`),
  KEY `fk_section_period` (`period_id`),
  KEY `fk_section_teacher` (`teacher_id`),
  CONSTRAINT `fk_section_course` FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`),
  CONSTRAINT `fk_section_period` FOREIGN KEY (`period_id`) REFERENCES `academic_periods` (`period_id`),
  CONSTRAINT `fk_section_teacher` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course_sections`
--

LOCK TABLES `course_sections` WRITE;
/*!40000 ALTER TABLE `course_sections` DISABLE KEYS */;
INSERT INTO `course_sections` VALUES (1,1,1,1,'A',35,0,'2026-02-17 12:54:20'),(2,1,1,2,'B',30,0,'2026-02-17 12:54:20'),(3,2,1,2,'A',40,0,'2026-02-17 12:54:20'),(4,4,1,3,'A',45,0,'2026-02-17 12:54:20');
/*!40000 ALTER TABLE `course_sections` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courses` (
  `course_id` int NOT NULL AUTO_INCREMENT,
  `program_id` int NOT NULL,
  `code` varchar(15) NOT NULL,
  `name` varchar(120) NOT NULL,
  `credits` tinyint NOT NULL,
  `hours_week` tinyint NOT NULL,
  PRIMARY KEY (`course_id`),
  UNIQUE KEY `code` (`code`),
  KEY `fk_course_program` (`program_id`),
  CONSTRAINT `fk_course_program` FOREIGN KEY (`program_id`) REFERENCES `programs` (`program_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES (1,1,'BD101','Gestión de Bases de Datos',3,4),(2,1,'PRG101','Programación I',3,4),(3,2,'WEB201','Desarrollo Web II',3,4),(4,3,'ADM110','Fundamentos de Administración',2,3);
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departments` (
  `dept_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`dept_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES (2,'Ciencias Administrativas'),(3,'Diseño'),(1,'Ingeniería');
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enrollment_audit`
--

DROP TABLE IF EXISTS `enrollment_audit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enrollment_audit` (
  `audit_id` int NOT NULL AUTO_INCREMENT,
  `enrollment_id` int NOT NULL,
  `old_status` varchar(20) DEFAULT NULL,
  `new_status` varchar(20) NOT NULL,
  `changed_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `changed_by` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`audit_id`),
  KEY `fk_enroll_audit_enrollment` (`enrollment_id`),
  CONSTRAINT `fk_enroll_audit_enrollment` FOREIGN KEY (`enrollment_id`) REFERENCES `enrollments` (`enrollment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enrollment_audit`
--

LOCK TABLES `enrollment_audit` WRITE;
/*!40000 ALTER TABLE `enrollment_audit` DISABLE KEYS */;
/*!40000 ALTER TABLE `enrollment_audit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enrollments`
--

DROP TABLE IF EXISTS `enrollments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enrollments` (
  `enrollment_id` int NOT NULL AUTO_INCREMENT,
  `student_id` int NOT NULL,
  `section_id` int NOT NULL,
  `enrolled_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` enum('ENROLLED','DROPPED','COMPLETED') NOT NULL DEFAULT 'ENROLLED',
  `final_grade` decimal(4,2) DEFAULT NULL,
  `passed` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`enrollment_id`),
  UNIQUE KEY `student_id` (`student_id`,`section_id`),
  KEY `fk_enroll_section` (`section_id`),
  CONSTRAINT `fk_enroll_section` FOREIGN KEY (`section_id`) REFERENCES `course_sections` (`section_id`),
  CONSTRAINT `fk_enroll_student` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enrollments`
--

LOCK TABLES `enrollments` WRITE;
/*!40000 ALTER TABLE `enrollments` DISABLE KEYS */;
INSERT INTO `enrollments` VALUES (1,1,1,'2026-02-17 12:55:03','ENROLLED',NULL,NULL),(2,2,1,'2026-02-17 12:55:03','ENROLLED',NULL,NULL),(3,3,2,'2026-02-17 12:55:03','ENROLLED',NULL,NULL),(4,1,3,'2026-02-17 12:55:03','ENROLLED',NULL,NULL),(5,5,4,'2026-02-17 12:55:03','ENROLLED',NULL,NULL);
/*!40000 ALTER TABLE `enrollments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grade_audit`
--

DROP TABLE IF EXISTS `grade_audit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grade_audit` (
  `audit_id` int NOT NULL AUTO_INCREMENT,
  `grade_id` int NOT NULL,
  `old_score` decimal(4,2) DEFAULT NULL,
  `new_score` decimal(4,2) NOT NULL,
  `changed_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `changed_by` varchar(120) DEFAULT NULL,
  `action` enum('INSERT','UPDATE','DELETE') NOT NULL,
  PRIMARY KEY (`audit_id`),
  KEY `fk_audit_grade` (`grade_id`),
  CONSTRAINT `fk_audit_grade` FOREIGN KEY (`grade_id`) REFERENCES `grades` (`grade_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grade_audit`
--

LOCK TABLES `grade_audit` WRITE;
/*!40000 ALTER TABLE `grade_audit` DISABLE KEYS */;
/*!40000 ALTER TABLE `grade_audit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grades`
--

DROP TABLE IF EXISTS `grades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grades` (
  `grade_id` int NOT NULL AUTO_INCREMENT,
  `enrollment_id` int NOT NULL,
  `assessment_id` int NOT NULL,
  `score` decimal(4,2) NOT NULL,
  `graded_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`grade_id`),
  UNIQUE KEY `enrollment_id` (`enrollment_id`,`assessment_id`),
  KEY `fk_grade_assessment` (`assessment_id`),
  CONSTRAINT `fk_grade_assessment` FOREIGN KEY (`assessment_id`) REFERENCES `assessments` (`assessment_id`),
  CONSTRAINT `fk_grade_enrollment` FOREIGN KEY (`enrollment_id`) REFERENCES `enrollments` (`enrollment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grades`
--

LOCK TABLES `grades` WRITE;
/*!40000 ALTER TABLE `grades` DISABLE KEYS */;
INSERT INTO `grades` VALUES (1,1,1,4.20,'2026-02-17 12:55:48'),(2,1,2,4.00,'2026-02-17 12:55:48'),(3,1,3,4.50,'2026-02-17 12:55:48'),(4,2,1,3.00,'2026-02-17 12:55:56'),(5,2,2,3.50,'2026-02-17 12:55:56'),(6,2,3,3.80,'2026-02-17 12:55:56');
/*!40000 ALTER TABLE `grades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `programs`
--

DROP TABLE IF EXISTS `programs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `programs` (
  `program_id` int NOT NULL AUTO_INCREMENT,
  `dept_id` int NOT NULL,
  `name` varchar(120) NOT NULL,
  `level` enum('TECNICO','TECNOLOGO','PROFESIONAL','POSGRADO') NOT NULL,
  `modality` enum('PRESENCIAL','VIRTUAL','MIXTA') NOT NULL DEFAULT 'PRESENCIAL',
  PRIMARY KEY (`program_id`),
  KEY `fk_program_dept` (`dept_id`),
  CONSTRAINT `fk_program_dept` FOREIGN KEY (`dept_id`) REFERENCES `departments` (`dept_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `programs`
--

LOCK TABLES `programs` WRITE;
/*!40000 ALTER TABLE `programs` DISABLE KEYS */;
INSERT INTO `programs` VALUES (1,1,'Ingeniería de Sistemas','PROFESIONAL','PRESENCIAL'),(2,1,'Tecnología en Desarrollo de Software','TECNOLOGO','MIXTA'),(3,2,'Administración de Empresas','PROFESIONAL','PRESENCIAL');
/*!40000 ALTER TABLE `programs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_programs`
--

DROP TABLE IF EXISTS `student_programs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_programs` (
  `student_id` int NOT NULL,
  `program_id` int NOT NULL,
  `start_period_id` int NOT NULL,
  `status` enum('ACTIVE','INACTIVE') NOT NULL DEFAULT 'ACTIVE',
  PRIMARY KEY (`student_id`),
  KEY `fk_stprog_program` (`program_id`),
  KEY `fk_stprog_period` (`start_period_id`),
  CONSTRAINT `fk_stprog_period` FOREIGN KEY (`start_period_id`) REFERENCES `academic_periods` (`period_id`),
  CONSTRAINT `fk_stprog_program` FOREIGN KEY (`program_id`) REFERENCES `programs` (`program_id`),
  CONSTRAINT `fk_stprog_student` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_programs`
--

LOCK TABLES `student_programs` WRITE;
/*!40000 ALTER TABLE `student_programs` DISABLE KEYS */;
INSERT INTO `student_programs` VALUES (1,1,1,'ACTIVE'),(2,1,1,'ACTIVE'),(3,2,1,'ACTIVE'),(4,1,1,'INACTIVE'),(5,3,1,'ACTIVE'),(6,2,1,'ACTIVE');
/*!40000 ALTER TABLE `student_programs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `student_id` int NOT NULL AUTO_INCREMENT,
  `doc_type` enum('CC','TI','CE','PP') NOT NULL,
  `doc_number` varchar(30) NOT NULL,
  `first_name` varchar(60) NOT NULL,
  `last_name` varchar(60) NOT NULL,
  `email` varchar(120) NOT NULL,
  `status` enum('ACTIVE','INACTIVE') NOT NULL DEFAULT 'ACTIVE',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`student_id`),
  UNIQUE KEY `doc_number` (`doc_number`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'CC','1010','Ana','Rojas','ana.rojas@correo.com','ACTIVE','2026-02-17 12:54:31'),(2,'TI','2020','Luis','Gómez','luis.gomez@correo.com','ACTIVE','2026-02-17 12:54:31'),(3,'CC','3030','Marta','Ruiz','marta.ruiz@correo.com','ACTIVE','2026-02-17 12:54:31'),(4,'CC','4040','Juan','Díaz','juan.diaz@correo.com','INACTIVE','2026-02-17 12:54:31'),(5,'CC','5050','Paula','Suárez','paula.suarez@correo.com','ACTIVE','2026-02-17 12:54:31'),(6,'TI','6060','Santiago','López','santiago.lopez@correo.com','ACTIVE','2026-02-17 12:54:31');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teachers` (
  `teacher_id` int NOT NULL AUTO_INCREMENT,
  `dept_id` int NOT NULL,
  `full_name` varchar(120) NOT NULL,
  `email` varchar(120) NOT NULL,
  `status` enum('ACTIVE','INACTIVE') NOT NULL DEFAULT 'ACTIVE',
  PRIMARY KEY (`teacher_id`),
  UNIQUE KEY `email` (`email`),
  KEY `fk_teacher_dept` (`dept_id`),
  CONSTRAINT `fk_teacher_dept` FOREIGN KEY (`dept_id`) REFERENCES `departments` (`dept_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
INSERT INTO `teachers` VALUES (1,1,'Carlos Salas','casalass@sanmateo.edu.co','ACTIVE'),(2,1,'Laura Martínez','l.martinez@sanmateo.edu.co','ACTIVE'),(3,2,'Andrés Pérez','a.perez@sanmateo.edu.co','ACTIVE');
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-17 14:12:09
