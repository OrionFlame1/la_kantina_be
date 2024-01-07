CREATE TABLE IF NOT EXISTS accounts (
  `id` integer NOT NULL AUTO_INCREMENT,
  `name` varchar(255),
  `email` varchar(255),
  `password` varchar(255),
  `type` varchar(255) COMMENT 'customer/admin/(waiter)',
  `points` integer COMMENT 'fidelity points',
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS reservations (
  `id` integer NOT NULL AUTO_INCREMENT,
  `account_id` integer,
  `table_id` integer,
  `start_at` timestamp,
  `end_at` timestamp COMMENT 'optional, used to delimit reservation',
  `status` varchar(255) COMMENT 'pending, confirmed, active, cancelled',
  `feedback` integer COMMENT 'null until feedback arrives, 0 dislike, 1 like',
  `created_at` timestamp COMMENT 'now()',
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS tables (
  `id` integer NOT NULL AUTO_INCREMENT COMMENT 'static table, used only to store tables and slots',
  `slots` integer,
  `x` integer,
  `y` integer,
  PRIMARY KEY (id)
);

ALTER TABLE `reservations` ADD FOREIGN KEY (`account_id`) REFERENCES `accounts` (`id`);
