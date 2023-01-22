CREATE DATABASE IF NOT EXISTS `batdb`;
USE `batdb`;

CREATE TABLE IF NOT EXISTS `Quotes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  AUTO_INCREMENT=1 ;



insert into Quotes (content) values ("I am Batman");     
insert into Quotes (content) values ("If youre good at something, never do it for free.");    
insert into Quotes (content) values ("They think I am hiding in the shadows. But I am the shadows."); 
insert into Quotes (content) values ("This city just showed you that it is full of people ready to believe in good.");   
insert into Quotes (content) values ("Bats do not host any more disease-causing (zoonotic) viruses than any other groups of animals (mammals and birds) of similar species diversity");
insert into Quotes (content) values ("Without bats, say goodbye to bananas, avocados and mangoes");
