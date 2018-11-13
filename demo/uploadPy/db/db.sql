CREATE TABLE `ot_bingimage` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`url` VARCHAR(255) NULL DEFAULT NULL,
	`fid` VARCHAR(255) NULL DEFAULT NULL,
	`img_file_name` VARCHAR(255) NULL DEFAULT NULL,
	`img_type` INT(11) NULL DEFAULT NULL,
	`create_time` TIMESTAMP NULL DEFAULT '',
	PRIMARY KEY (`id`)
)
COMMENT='bing每日图片'
COLLATE='utf8_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=2890
;

create view randombingimage
as
select * from ot_bingimage order by rand() limit 1 
;
