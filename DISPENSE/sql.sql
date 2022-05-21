CREATE TABLE `product` (
	`id` int unsigned COLLATE utf8mb4_unicode_ci NOT NULL AUTO_INCREMENT,
	`name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	`code` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	`image` text COLLATE utf8mb4_unicode_ci NOT NULL,
	`price` double COLLATE utf8mb4_unicode_ci NOT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;


    
CREATE TABLE `flower` (
	`id` int unsigned COLLATE utf8mb4_unicode_ci NOT NULL AUTO_INCREMENT,
	`strain` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	`type` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `farm` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `weight_in_grams` decimal(4,2) COLLATE utf8mb4_unicode_ci NOT NULL,
    `thc_percent` decimal(4,2) COLLATE utf8mb4_unicode_ci NOT NULL,
    `cbd_percent` decimal(4,2) COLLATE utf8mb4_unicode_ci NOT NULL,
    `harvest date` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `description` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `price` decimal(4,2) COLLATE utf8mb4_unicode_ci NOT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;
    
    
CREATE TABLE `pre_rolls` (
	`id` int unsigned COLLATE utf8mb4_unicode_ci NOT NULL AUTO_INCREMENT,
	`brand` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
	`type` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `strain` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `number_of_joints` int(4) COLLATE utf8mb4_unicode_ci NOT NULL,
    `thc_percent` decimal(4,2) COLLATE utf8mb4_unicode_ci NOT NULL,
    `cbd_percent` decimal(4,2) COLLATE utf8mb4_unicode_ci NOT NULL,
    `harvest date` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `description` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `price` decimal(4,2) COLLATE utf8mb4_unicode_ci NOT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;
    
