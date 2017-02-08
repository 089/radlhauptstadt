CREATE DATABASE IF NOT EXISTS `radlhauptstadt` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `radlhauptstadt`;

DELIMITER $$
DROP PROCEDURE IF EXISTS `all_stations`$$
CREATE PROCEDURE `all_stations`(IN prov VARCHAR(16))
BEGIN
	SELECT * FROM `station` 
	WHERE 
	(SELECT MAX(id) FROM loaderiteration) = iteration_id
	AND provider = prov;
END$$

DROP PROCEDURE IF EXISTS `all_vehicles`$$
CREATE PROCEDURE `all_vehicles`(IN prov VARCHAR(16))
BEGIN
	SELECT * FROM `vehicle` 
	WHERE 
	(SELECT MAX(id) FROM loaderiteration) = iteration_id
	AND provider = prov;
END$$

DROP PROCEDURE IF EXISTS `one_station`$$
CREATE PROCEDURE `one_station`(IN prov VARCHAR(16), num INT(11))
BEGIN
	SELECT * FROM `station` 
	WHERE 
	(SELECT MAX(id) FROM loaderiteration) = iteration_id
	AND provider = prov AND number_of_station = num;
END$$

DROP PROCEDURE IF EXISTS `one_vehicle`$$
CREATE PROCEDURE `one_vehicle`(IN prov VARCHAR(16), num INT(11))
BEGIN
	SELECT * FROM `vehicle` 
	WHERE 
	(SELECT MAX(id) FROM loaderiteration) = iteration_id
	AND provider = prov AND number_of_vehicle = num;
END$$

DELIMITER ;

DROP TABLE IF EXISTS `loaderiteration`;
CREATE TABLE IF NOT EXISTS `loaderiteration` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `timestmp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=7 ;

DROP TABLE IF EXISTS `station`;
CREATE TABLE IF NOT EXISTS `station` (
  `iteration_id` int(11) NOT NULL,
  `provider` varchar(16) COLLATE utf8_unicode_ci NOT NULL,
  `latitude` double NOT NULL,
  `longitude` double NOT NULL,
  `name` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `number_of_station` int(11) NOT NULL,
  `free_bikes` int(11) NOT NULL,
  PRIMARY KEY (`iteration_id`,`provider`,`number_of_station`),
  KEY `iteration_id` (`iteration_id`,`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

DROP TABLE IF EXISTS `vehicle`;
CREATE TABLE IF NOT EXISTS `vehicle` (
  `iteration_id` int(11) NOT NULL,
  `provider` varchar(16) COLLATE utf8_unicode_ci NOT NULL,
  `latitude` double NOT NULL,
  `longitude` double NOT NULL,
  `type` varchar(16) COLLATE utf8_unicode_ci NOT NULL,
  `number_of_vehicle` int(11) NOT NULL,
  PRIMARY KEY (`iteration_id`,`provider`,`number_of_vehicle`),
  KEY `iteration_id` (`iteration_id`),
  KEY `type` (`type`),
  KEY `provider` (`provider`),
  KEY `number_of_vehicle` (`number_of_vehicle`),
  KEY `iteration_id_2` (`iteration_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
