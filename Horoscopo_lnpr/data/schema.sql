<--DB script-->
CREATE DATABASE horoscopo_lnpr;
USE horoscopo_lnpr;

CREATE TABLE horoscopos(
    id_signo INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre_signo   VARCHAR(100)    NOT NULL,
    descripcion_signo VARCHAR     NOT NULL
);


CREATE USER 'horoscopo'@'localhost' IDENTIFIED BY 'horoscopo.2019';
GRANT ALL PRIVILEGES ON horoscopo_lnpr.* TO 'horoscopo'@'localhost';
FLUSH PRIVILEGES;
