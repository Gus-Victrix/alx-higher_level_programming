-- Create usa database | states table with primary id
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states`
(
    PRIMARY KEY (`id`),
    `id` int NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);
