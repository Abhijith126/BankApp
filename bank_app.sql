-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: May 25, 2018 at 02:52 AM
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
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `account_no` int(13) NOT NULL,
  `payee_acc_no` int(13) NOT NULL,
  `payee_name` varchar(50) NOT NULL,
  `payee_bank` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_no` (`account_no`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `transfers`
--

DROP TABLE IF EXISTS `transfers`;
CREATE TABLE IF NOT EXISTS `transfers` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `account_no` int(13) NOT NULL,
  `payee_acc_no` int(13) NOT NULL,
  `payee_bank` varchar(20) NOT NULL,
  `transfer_amt` float NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_no` (`account_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `account_no` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `balance` float NOT NULL,
  PRIMARY KEY (`account_no`)
) ENGINE=InnoDB AUTO_INCREMENT=1234567891 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`account_no`, `name`, `password`, `balance`) VALUES
(1000001, 'dasqew', 'None', 12),
(1000002, 'admin', 'None', 12312),
(1000003, 'admin', 'None', 2),
(1000004, '12edas', 'None', 324),
(1000005, 'dasqew', 'None', 45);

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
  ADD CONSTRAINT `transfers_ibfk_1` FOREIGN KEY (`account_no`) REFERENCES `users` (`account_no`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
