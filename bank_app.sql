-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: May 25, 2018 at 03:40 PM
-- Server version: 5.7.21
-- PHP Version: 5.6.35

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
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `account_no` int(13) UNSIGNED NOT NULL,
  `payee_acc_no` bigint(13) UNSIGNED NOT NULL,
  `name` varchar(50) NOT NULL,
  `bank_name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_no` (`account_no`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `payee`
--

INSERT INTO `payee` (`id`, `account_no`, `payee_acc_no`, `name`, `bank_name`) VALUES
(5, 1000000, 23242342342, 'Jane doe', 'ICICI Bank');

-- --------------------------------------------------------

--
-- Table structure for table `transfers`
--

DROP TABLE IF EXISTS `transfers`;
CREATE TABLE IF NOT EXISTS `transfers` (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `from_acc_no` int(11) UNSIGNED NOT NULL,
  `to_acc_no` bigint(11) UNSIGNED NOT NULL,
  `bank_name` varchar(50) NOT NULL,
  `amount` float UNSIGNED ZEROFILL NOT NULL,
  PRIMARY KEY (`id`),
  KEY `from_acc_no` (`from_acc_no`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transfers`
--

INSERT INTO `transfers` (`id`, `from_acc_no`, `to_acc_no`, `bank_name`, `amount`) VALUES
(8, 1000000, 12221212211, 'ads', 000000000011);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `account_no` int(13) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `balance` float UNSIGNED ZEROFILL NOT NULL DEFAULT '000000000000',
  PRIMARY KEY (`account_no`)
) ENGINE=InnoDB AUTO_INCREMENT=100002136 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`account_no`, `name`, `password`, `balance`) VALUES
(1000000, 'Abhijith P', 'admin', 000000000489);

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
