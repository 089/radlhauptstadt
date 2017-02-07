-- one_vehicle(provider, vehiclenumber)
DELIMITER //
CREATE PROCEDURE one_vehicle
(IN prov VARCHAR(16), num INT(11))
BEGIN
	SELECT * FROM `vehicle` 
	WHERE 
	(SELECT MAX(id) FROM loaderiteration) = iteration_id
	AND provider = prov AND number_of_vehicle = num;
END //
DELIMITER ;

-- all_vehicles(provider)
DELIMITER //
CREATE PROCEDURE all_vehicles
(IN prov VARCHAR(16))
BEGIN
	SELECT * FROM `vehicle` 
	WHERE 
	(SELECT MAX(id) FROM loaderiteration) = iteration_id
	AND provider = prov;
END //
DELIMITER ;

-- one_station(provider, stationnumber)
DELIMITER //
CREATE PROCEDURE one_station
(IN prov VARCHAR(16), num INT(11))
BEGIN
	SELECT * FROM `station` 
	WHERE 
	(SELECT MAX(id) FROM loaderiteration) = iteration_id
	AND provider = prov AND number_of_station = num;
END //
DELIMITER ;

-- all_stations(provider)
DELIMITER //
CREATE PROCEDURE all_stations
(IN prov VARCHAR(16))
BEGIN
	SELECT * FROM `station` 
	WHERE 
	(SELECT MAX(id) FROM loaderiteration) = iteration_id
	AND provider = prov;
END //
DELIMITER ;

