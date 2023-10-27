-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 10, 2023 at 11:16 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1travelblockdbpy`
--

-- --------------------------------------------------------

--
-- Table structure for table `booktb`
--

CREATE TABLE `booktb` (
  `id` bigint(10) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `Bookid` varchar(250) NOT NULL,
  `Qty` varchar(250) NOT NULL,
  `Amount` varchar(250) NOT NULL,
  `CardName` varchar(250) NOT NULL,
  `CardNo` varchar(250) NOT NULL,
  `CvNo` varchar(250) NOT NULL,
  `Date` date NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `booktb`
--

INSERT INTO `booktb` (`id`, `UserName`, `Bookid`, `Qty`, `Amount`, `CardName`, `CardNo`, `CvNo`, `Date`) VALUES
(1, 'san', 'BOOKID1', '4.00', '2448.00', 'MASTERCARD', '1221423634748888', '123', '2023-04-10');

-- --------------------------------------------------------

--
-- Table structure for table `carttb`
--

CREATE TABLE `carttb` (
  `id` bigint(10) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `ProductName` varchar(250) NOT NULL,
  `ProductType` varchar(250) NOT NULL,
  `Price` varchar(250) NOT NULL,
  `Qty` decimal(18,2) NOT NULL,
  `Tprice` decimal(28,2) NOT NULL,
  `Image` varchar(500) NOT NULL,
  `Date` date NOT NULL,
  `Status` varchar(250) NOT NULL,
  `Bookid` varchar(250) NOT NULL,
  `Gst` varchar(20) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `carttb`
--

INSERT INTO `carttb` (`id`, `UserName`, `ProductName`, `ProductType`, `Price`, `Qty`, `Tprice`, `Image`, `Date`, `Status`, `Bookid`, `Gst`) VALUES
(1, 'san', 'TN48AL5535', 'BUS', '600', '2.00', '1224.00', '7221.png', '2023-04-10', '1', 'BOOKID1', '2'),
(2, 'san', '21BH2345AA', 'BUS', '600', '2.00', '1224.00', '5659.png', '2023-04-10', '1', 'BOOKID1', '2');

-- --------------------------------------------------------

--
-- Table structure for table `protb`
--

CREATE TABLE `protb` (
  `id` bigint(10) NOT NULL auto_increment,
  `VehicleNo` varchar(250) NOT NULL,
  `VehicleType` varchar(250) NOT NULL,
  `Price` varchar(250) NOT NULL,
  `Qty` varchar(250) NOT NULL,
  `Info` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `Image` varchar(500) NOT NULL,
  `Gst` varchar(250) NOT NULL,
  `Source` varchar(250) NOT NULL,
  `Destination` varchar(250) NOT NULL,
  `Hash1` varchar(250) NOT NULL,
  `Hash2` varchar(250) NOT NULL,
  `TravelName` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `protb`
--

INSERT INTO `protb` (`id`, `VehicleNo`, `VehicleType`, `Price`, `Qty`, `Info`, `date`, `Image`, `Gst`, `Source`, `Destination`, `Hash1`, `Hash2`, `TravelName`) VALUES
(1, '21BH2345AA', 'BUS', '600', '38.0', 'ac', '2023-04-10', '5659.png', '2', 'trichy', 'Covai', '0', '823CBC6B3136B4A10FF8A9E2301C4EE9A37A50A59E00CC5865BE079836E6BA56', 'selva'),
(2, 'TN48AL5535', 'BUS', '600', '38.0', 'ac', '2023-04-10', '7221.png', '2', 'trichy', 'Covai', '823CBC6B3136B4A10FF8A9E2301C4EE9A37A50A59E00CC5865BE079836E6BA56', '7BBB35D446D59C54BAE763BB36CAA6363E6E0CC6E63409ABCC72A6345AEE765B', 'selva');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `Name` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`Name`, `Email`, `Mobile`, `Address`, `UserName`, `Password`, `Gender`) VALUES
('sangeeth Kumar', 'sangeeth5535@gmail.com', '9486365535', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san', 'Male');

-- --------------------------------------------------------

--
-- Table structure for table `traveltb`
--

CREATE TABLE `traveltb` (
  `Name` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  `registerNo` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `traveltb`
--

INSERT INTO `traveltb` (`Name`, `Email`, `Mobile`, `Address`, `UserName`, `Password`, `registerNo`, `Status`) VALUES
('selva', 'sangeeth5535@gmail.com', '9486365535', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'selva', 'selva', '3474585696709', 'Approved');
