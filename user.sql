# Host: localhost  (Version: 5.7.26)
# Date: 2020-10-22 13:31:18
# Generator: MySQL-Front 5.3  (Build 4.234)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "user"
#

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `login_name` varchar(255) DEFAULT '',
  `pwd` varchar(255) DEFAULT NULL,
  `nickname` varchar(255) DEFAULT NULL,
  `sex` varchar(4) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `os` varchar(255) DEFAULT NULL,
  `ip` varchar(255) DEFAULT NULL,
  `advantage` varchar(255) DEFAULT NULL,
  `disadvantage` varchar(255) DEFAULT NULL,
  `birthday` varchar(11) DEFAULT NULL,
  `status` varchar(255) NOT NULL DEFAULT '1',
  `five_element` varchar(255) DEFAULT NULL,
  `sign` varchar(255) DEFAULT NULL,
  `career` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

#
# Data for table "user"
#

/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'adminzxz','45790b92f0e671b630ae45732c5ac059','啊啊啊','男','天津','iphone','100.100.1.1','偏财','食神','1988-8-6-9','1','火',NULL,NULL),(2,'rrrrrr','73882ab1fa529d7273da0db6b49cc4f3','ttttt','女','ttttt','windows','127.0.0.1','比肩','伤官','2020-10-1-1','1','火',NULL,NULL),(3,'yyyyyy','5b1b68a9abf4d2cd155c81a9225fd158','dffff','女','yyyyy','windows','127.0.0.1','官','伤官','2020-10-5-1','1','火',NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
