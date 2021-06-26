CREATE SCHEMA IF NOT EXISTS `todo_app` DEFAULT CHARACTER SET utf8;
USE `todo_app`;

CREATE TABLE IF NOT EXISTS `todo_app`.`users` (
  `id`         INTEGER   UNSIGNED NOT NULL AUTO_INCREMENT,
  `username`   VARCHAR(255) NOT NULL UNIQUE,
  `password`   VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `todo_app`.`tasks` (
  `id`              INTEGER   UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id`         INTEGER UNSIGNED NOT NULL,
  `limit_at`        DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_at`      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `task`            VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_tasks_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `todo_app`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `todo_app`.`sub_tasks` (
  `id`              INTEGER  UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id`         INTEGER  UNSIGNED NOT NULL,
  `task_id`         INTEGER  UNSIGNED NOT NULL,
  `created_at`      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `sub_task`        VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_sub_tasks_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `todo_app`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_sub_tasks_task_id`
    FOREIGN KEY (`task_id`)
    REFERENCES `todo_app`.`tasks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)
ENGINE = InnoDB;
