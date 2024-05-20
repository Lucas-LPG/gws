DROP DATABASE IF EXISTS puhl_gasperin_health;
CREATE DATABASE puhl_gasperin_health;
USE puhl_gasperin_health;
DROP USER IF EXISTS 'lucas'@'%';
CREATE USER lucas IDENTIFIED BY "lucas";
GRANT ALL ON *.* TO lucas WITH GRANT OPTION;
