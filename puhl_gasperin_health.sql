DROP DATABASE IF EXISTS puhl_gasperin_health;
CREATE DATABASE puhl_gasperin_health;
USE puhl_gasperin_health;
DROP USER IF EXISTS 'lucas'@'%';
CREATE USER lucas IDENTIFIED BY "lucas";
GRANT ALL ON *.* TO lucas WITH GRANT OPTION;
-- SELECT * FROM users;
-- SELECT * FROM kits;
-- SELECT * FROM actuators;
-- SELECT * FROM sensors;
-- SELECT * FROM historic;

DELIMITER $$

CREATE TRIGGER populate_historic
AFTER INSERT ON devices
FOR EACH ROW
BEGIN
	INSERT INTO historic(value, datetime, device_id) VALUES(NULL, NOW(), NEW.id);
END$$

DELIMITER ;
