<--DB script-->
CREATE DATABASE horoscopo_lnpr;
USE horoscopo_lnpr;

CREATE TABLE horoscopos(
    id_signo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_signo   VARCHAR(100)    NOT NULL,
    descripcion_signo VARCHAR(2000)     NOT NULL,
    ruta_img_signo  VARCHAR(100)    NOT NULL
)ENGINE = InnoDB DEFAULT CHARSET = utf8;


CREATE USER 'horoscopo'@'localhost' IDENTIFIED BY 'horoscopo.2019';
GRANT ALL PRIVILEGES ON horoscopo_lnpr.* TO 'horoscopo'@'localhost';
FLUSH PRIVILEGES;
