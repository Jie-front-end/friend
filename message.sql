# Host: localhost  (Version: 5.7.26)
# Date: 2020-10-22 13:31:08
# Generator: MySQL-Front 5.3  (Build 4.234)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "message"
#

DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `send` varchar(255) DEFAULT NULL,
  `accept` varchar(255) DEFAULT NULL,
  `time` varchar(255) DEFAULT NULL,
  `content` varchar(2550) DEFAULT NULL,
  `status` int(11) DEFAULT '0',
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

#
# Data for table "message"
#

/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,'adminzxz','adminzxz','1602524093.0940566','你好',1),(2,'adminzxz','adminzxz','1603114116.6064827','你好',1),(3,'adminzxz','adminzxz','1603114275.867064','你好',1),(4,'adminzxz','adminzxz','1603116349.9032755','你好',1),(5,'adminzxz','adminzxz','1603119452.583203','你好',1),(6,'adminzxz','adminzxz','1603158525.6599257','你好',1),(7,'adminzxz','adminzxz','1603179127.5394483','你好',1),(8,'adminzxz','adminzxz','1603207917.6194935','你好',1),(9,'adminzxz','adminzxz','1603208003.9838336','你好',1);
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
