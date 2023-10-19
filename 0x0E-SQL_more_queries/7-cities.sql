-- Create city table with primary id and FOREIGN KEY
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities`
(
    PRIMARY KEY (`id`),
    `id` int NOT NULL AUTO_INCREMENT,
    `state_id` int NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (`state_id`) REFERENCES `hbtn_0d_usa`.`cities`(`id`)
);
