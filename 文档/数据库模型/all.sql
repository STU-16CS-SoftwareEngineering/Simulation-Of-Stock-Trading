CREATE DATABASE  IF NOT EXISTS `market` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `market`;
-- MySQL dump 10.13  Distrib 5.6.13, for Win32 (x86)
--
-- Host: 127.0.0.1    Database: market
-- ------------------------------------------------------
-- Server version	5.7.4-m14

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `blacklist_db`
--

DROP TABLE IF EXISTS `blacklist_db`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blacklist_db` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wxid` text NOT NULL,
  `reason` text NOT NULL,
  `op_time` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blacklist_db`
--

LOCK TABLES `blacklist_db` WRITE;
/*!40000 ALTER TABLE `blacklist_db` DISABLE KEYS */;
INSERT INTO `blacklist_db` VALUES (1,'1234','111',1568044800);
/*!40000 ALTER TABLE `blacklist_db` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_db`
--

DROP TABLE IF EXISTS `log_db`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log_db` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `op_type` text,
  `op_time` int(11) DEFAULT NULL,
  `op_detail` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log_db`
--

LOCK TABLES `log_db` WRITE;
/*!40000 ALTER TABLE `log_db` DISABLE KEYS */;
INSERT INTO `log_db` VALUES (1,'arg:admin|arg:123456|arg:org.apache.catalina.connector.ResponseFacade@5a12a205|',1568103911,NULL),(2,'arg:admin|arg:123456|arg:org.apache.catalina.connector.ResponseFacade@434f9ba8|',1568104108,NULL),(3,'arg:admin|arg:123456|arg:org.apache.catalina.connector.ResponseFacade@206c999c|',1568104191,NULL),(4,'login',1568104296,'arg:admin | arg:123456 | arg:org.apache.catalina.connector.ResponseFacade@15e5d355 | '),(5,'getAccount',1568104317,'arg:58d1acbfb2a1400e8c9fa35aa493bc5b | '),(6,'login',1568105965,'arg:admin | arg:123456 | arg:org.apache.catalina.connector.ResponseFacade@3f5a82ff | '),(7,'addBlackListUser',1568105973,'arg:{\"reason\":\"111\",\"op_time\":\"1568044800\",\"wxid\":\"1234\"} | '),(8,'login',1568106026,'arg:admin | arg:123456 | arg:org.apache.catalina.connector.ResponseFacade@62221a91 | '),(9,'addBlackListUser',1568106034,'arg:{\"reason\":\"111\",\"op_time\":\"1568044800\",\"wxid\":\"1234\"} | '),(10,'getBlackList',1568106073,'arg:1 | '),(11,'addBlackListUser',1568106125,'arg:{\"reason\":\"111\",\"op_time\":\"1568044800\",\"wxid\":\"5678\"} | '),(12,'getBlackList',1568106127,'arg:1 | '),(13,'deleteBlackListUser',1568106159,'arg:2 | '),(14,'getBlackList',1568106162,'arg:1 | '),(15,'login',1568106673,'arg:admin | arg:123456 | arg:org.apache.catalina.connector.ResponseFacade@2559c778 | '),(16,'getMatch',1568106680,'arg:测试1 | '),(17,'getMatch',1568106715,'arg:1234 | '),(18,'login',1568107113,'arg:admin | arg:12345 | arg:org.apache.catalina.connector.ResponseFacade@468fe194 | '),(19,'getAccount',1568108251,'arg:1d0decc7b13445fcbf8508f197bdaa7d | '),(20,'login',1568108493,'arg:admin | arg:12345 | arg:org.apache.catalina.connector.ResponseFacade@375bd552 | '),(21,'login',1568108500,'arg:admin | arg:123456 | arg:org.apache.catalina.connector.ResponseFacade@375bd552 | '),(22,'getAccount',1568108504,'arg:04a3de86f0ec4b7f949a93136c4b60d0 | '),(23,'login',1568108551,'arg:admin | arg:123456 | arg:org.apache.catalina.connector.ResponseFacade@5690ecea | '),(24,'getAccount',1568108558,'arg:5dc5f60c2dbe41cca2643db9ae3c975f | '),(25,'login',1568108852,'arg:admin | arg:123456 | arg:org.apache.catalina.connector.ResponseFacade@3ad58329 | '),(26,'logout',1568108939,'arg:e66b57fda359481dae1e9593438bfd27 | arg:org.apache.catalina.connector.ResponseFacade@123ee505 | '),(27,'login',1568109280,'arg:admin | arg:123456 | arg:org.apache.catalina.connector.ResponseFacade@123ee505 | '),(28,'addMatch',1568109284,'arg:{\"start_time\":\"1568044800\",\"init_money\":\"10000\",\"match_detail\":\"测试细节\",\"end_time\":\"1568044800\",\"match_rule\":\"测试规则\",\"sign_time\":\"1568044800\",\"match_name\":\"测试13\"} | '),(29,'addMatch',1568109313,'arg:{\"start_time\":\"1568044800\",\"init_money\":\"10000\",\"match_detail\":\"测试细节\",\"end_time\":\"1568044800\",\"match_rule\":\"测试规则\",\"sign_time\":\"1568044800\",\"match_name\":\"测试12\"} | '),(30,'addMatch',1568109316,'arg:{\"start_time\":\"1568044800\",\"init_money\":\"10000\",\"match_detail\":\"测试细节\",\"end_time\":\"1568044800\",\"match_rule\":\"测试规则\",\"sign_time\":\"1568044800\",\"match_name\":\"测试12\"} | '),(31,'getAllMatch',1568109587,'arg:1 | '),(32,'updateMatch',1568109679,'arg:{\"start_time\":\"1568044800\",\"init_money\":\"10000\",\"match_detail\":\"测试细节0\",\"end_time\":\"1568044800\",\"match_rule\":\"测试规则0\",\"id\":\"1\",\"sign_time\":\"1568044800\",\"match_name\":\"测试0\"} | '),(33,'updateMatch',1568109707,'arg:{\"start_time\":\"1568044800\",\"init_money\":\"10000\",\"match_detail\":\"测试细节0\",\"end_time\":\"1568044800\",\"match_rule\":\"测试规则0\",\"id\":\"15\",\"sign_time\":\"1568044800\",\"match_name\":\"测试0\"} | '),(34,'updateMatch',1568109812,'arg:{\"start_time\":\"1568044800\",\"init_money\":\"10000\",\"match_detail\":\"测试细节0\",\"end_time\":\"1568044800\",\"match_rule\":\"测试规则0\",\"id\":\"17\",\"sign_time\":\"1568044800\",\"match_name\":\"测试0\"} | '),(35,'deleteMatch',1568109917,'arg:13 | '),(36,'deleteMatch',1568109959,'arg:15 | '),(37,'getMatch',1568110040,'arg:测试1 | '),(38,'getMatch',1568110068,'arg:测试19 | '),(39,'login',1568110295,'arg:admin | arg:123456 | arg:org.apache.catalina.connector.ResponseFacade@2cf6cebd | '),(40,'addBlackListUser',1568110304,'arg:{\"reason\":\"111\",\"op_time\":\"1568044800\",\"wxid\":\"5678\"} | '),(41,'addBlackListUser',1568110324,'arg:{\"reason\":\"111\",\"op_time\":\"1568044800\",\"wxid\":\"5678\"} | '),(42,'getAllBlackList',1568110405,'arg:1 | '),(43,'deleteBlackListUser',1568110615,'arg:2 | '),(44,'deleteBlackListUser',1568110638,'arg:3 | '),(45,'getMatch',1568110739,'arg:43241 | ');
/*!40000 ALTER TABLE `log_db` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager_db`
--

DROP TABLE IF EXISTS `manager_db`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manager_db` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account` text NOT NULL,
  `password` text NOT NULL,
  `salt` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager_db`
--

LOCK TABLES `manager_db` WRITE;
/*!40000 ALTER TABLE `manager_db` DISABLE KEYS */;
INSERT INTO `manager_db` VALUES (2,'admin','4E613AA956CF8C5EABA1A3AA409C38F2','29b2d');
/*!40000 ALTER TABLE `manager_db` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `match_db`
--

DROP TABLE IF EXISTS `match_db`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `match_db` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `match_name` text NOT NULL,
  `match_detail` text,
  `match_rule` text,
  `start_time` int(11) DEFAULT NULL,
  `sign_time` int(11) DEFAULT NULL,
  `end_time` int(11) DEFAULT NULL,
  `init_money` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match_db`
--

LOCK TABLES `match_db` WRITE;
/*!40000 ALTER TABLE `match_db` DISABLE KEYS */;
INSERT INTO `match_db` VALUES (1,'测试0','测试细节0','测试规则0',1568044800,1568044800,1568044800,10000),(2,'测试1','测试细节1','测试规则1',1568044800,1568044800,1568044800,10000),(3,'测试2','测试细节','测试规则',1568044800,1568044800,1568044800,10000),(4,'测试3','测试细节','测试规则',1568044800,1568044800,1568044800,10000),(5,'测试4','测试细节','测试规则',1568044800,1568044800,1568044800,10000),(6,'测试5','测试细节','测试规则',1568044800,1568044800,1568044800,10000),(7,'测试6','测试细节','测试规则',1568044800,1568044800,1568044800,10000),(8,'测试7','测试细节','测试规则',1568044800,1568044800,1568044800,10000),(9,'测试8','测试细节','测试规则',1568044800,1568044800,1568044800,10000),(10,'测试9','测试细节','测试规则',1568044800,1568044800,1568044800,10000),(11,'测试10','测试细节','测试规则',1568044800,1568044800,1568044800,10000),(12,'测试11','测试细节','测试规则',1568044800,1568044800,1568044800,10000),(14,'测试13','测试细节','测试规则',1568044800,1568044800,1568044800,10000);
/*!40000 ALTER TABLE `match_db` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-09-10 19:12:28

/*
 Date: 12/09/2019 13:18:40
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for competitor_db
-- ----------------------------
DROP TABLE IF EXISTS `competitor_db`;
CREATE TABLE `competitor_db`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '数据项id',
  `match_id` int(11) NOT NULL COMMENT '比赛id',
  `wxid` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '微信id',
  `balance` double NOT NULL COMMENT '余额',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;


-- ----------------------------
-- Table structure for order_db
-- ----------------------------
DROP TABLE IF EXISTS `order_db`;
CREATE TABLE `order_db`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '数据项id',
  `order_type` int(11) NOT NULL COMMENT '订单类型，1 买入，2 售出',
  `wxid` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '微信id',
  `create_time` int(11) NOT NULL COMMENT '创建时间',
  `order_status` int(11) NOT NULL COMMENT '订单状态, 1 进行中、2 完成、3 撤销',
  `stock_id` int(11) NOT NULL COMMENT '股票id',
  `order_num` int(11) NOT NULL COMMENT '数量',
  `price` int(11) NOT NULL COMMENT '价格',
  `match_id` int(11) NOT NULL COMMENT '比赛id',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;


-- ----------------------------
-- Table structure for stock_cache
-- ----------------------------
DROP TABLE IF EXISTS `stock_cache`;
CREATE TABLE `stock_cache`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '数据项id',
  `stock_id` int(11) NOT NULL COMMENT '股票id',
  `stock_price` double NOT NULL COMMENT '股票单价',
  `get_time` int(11) NOT NULL COMMENT '获取时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;


-- ----------------------------
-- Table structure for storage_db
-- ----------------------------
DROP TABLE IF EXISTS `storage_db`;
CREATE TABLE `storage_db`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '数据项id',
  `wxid` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '微信id',
  `match_id` int(11) NOT NULL COMMENT '比赛id',
  `stock_id` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '股票id',
  `own_num` int(11) NOT NULL COMMENT '持仓数量',
  `ave_price` double NOT NULL COMMENT '买入价格',
  `lock_num` int(11) NOT NULL COMMENT '冻结数量',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;


-- ----------------------------
-- Table structure for user_db
-- ----------------------------
DROP TABLE IF EXISTS `user_db`;
CREATE TABLE `user_db`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '数据项id',
  `wxid` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '微信id',
  `heading` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '头像',
  `regist_time` int(11) NOT NULL COMMENT '注册时间',
  `token` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'token',
  `nickName` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '昵称',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;

-- ----------------------------
-- Table structure for news_db
-- ----------------------------

CREATE TABLE `news_db` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` text,
  `content` text,
  `lv` int(11) DEFAULT NULL,
  `source` varchar(255) DEFAULT NULL,
  `newstype` varchar(255) DEFAULT NULL,
  `sendtime` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
