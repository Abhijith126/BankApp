-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: May 25, 2018 at 12:19 PM
-- Server version: 5.7.19
-- PHP Version: 5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bank_app`
--

-- --------------------------------------------------------

--
-- Table structure for table `payee`
--

DROP TABLE IF EXISTS `payee`;
CREATE TABLE IF NOT EXISTS `payee` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `account_no` int(13) NOT NULL,
  `payee_acc_no` int(13) NOT NULL,
  `name` varchar(50) NOT NULL,
  `bank_name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_no` (`account_no`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `transfers`
--

DROP TABLE IF EXISTS `transfers`;
CREATE TABLE IF NOT EXISTS `transfers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_acc_no` int(11) NOT NULL,
  `to_acc_no` int(11) NOT NULL,
  `bank_name` varchar(50) NOT NULL,
  `amount` float NOT NULL,
  PRIMARY KEY (`id`),
  KEY `from_acc_no` (`from_acc_no`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `account_no` int(13) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `balance` float NOT NULL,
  PRIMARY KEY (`account_no`)
) ENGINE=InnoDB AUTO_INCREMENT=100002136 DEFAULT CHARSET=latin1;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `payee`
--
ALTER TABLE `payee`
  ADD CONSTRAINT `payee_ibfk_1` FOREIGN KEY (`account_no`) REFERENCES `users` (`account_no`);

--
-- Constraints for table `transfers`
--
ALTER TABLE `transfers`
  ADD CONSTRAINT `transfers_ibfk_1` FOREIGN KEY (`from_acc_no`) REFERENCES `users` (`account_no`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
