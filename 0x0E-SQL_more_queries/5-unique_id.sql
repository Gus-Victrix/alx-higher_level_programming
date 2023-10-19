-- Create a table with unique ID
CREATE TABLE IF NOT EXISTS `unique_id`
(
    `id` int DEFAULT 1 UNIQUE,
    `name` VARCHAR(256)
);