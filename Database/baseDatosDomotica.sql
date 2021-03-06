USE [master]
GO

/****** Object:  Database [Domotica]    Script Date: 04/07/2019 0:51:59 ******/
CREATE DATABASE [Domotica]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Domotica', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\DATA\Domotica.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'Domotica_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\DATA\Domotica_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
GO

ALTER DATABASE [Domotica] SET COMPATIBILITY_LEVEL = 140
GO

IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Domotica].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO

ALTER DATABASE [Domotica] SET ANSI_NULL_DEFAULT OFF 
GO

ALTER DATABASE [Domotica] SET ANSI_NULLS OFF 
GO

ALTER DATABASE [Domotica] SET ANSI_PADDING OFF 
GO

ALTER DATABASE [Domotica] SET ANSI_WARNINGS OFF 
GO

ALTER DATABASE [Domotica] SET ARITHABORT OFF 
GO

ALTER DATABASE [Domotica] SET AUTO_CLOSE OFF 
GO

ALTER DATABASE [Domotica] SET AUTO_SHRINK OFF 
GO

ALTER DATABASE [Domotica] SET AUTO_UPDATE_STATISTICS ON 
GO

ALTER DATABASE [Domotica] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO

ALTER DATABASE [Domotica] SET CURSOR_DEFAULT  GLOBAL 
GO

ALTER DATABASE [Domotica] SET CONCAT_NULL_YIELDS_NULL OFF 
GO

ALTER DATABASE [Domotica] SET NUMERIC_ROUNDABORT OFF 
GO

ALTER DATABASE [Domotica] SET QUOTED_IDENTIFIER OFF 
GO

ALTER DATABASE [Domotica] SET RECURSIVE_TRIGGERS OFF 
GO

ALTER DATABASE [Domotica] SET  DISABLE_BROKER 
GO

ALTER DATABASE [Domotica] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO

ALTER DATABASE [Domotica] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO

ALTER DATABASE [Domotica] SET TRUSTWORTHY OFF 
GO

ALTER DATABASE [Domotica] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO

ALTER DATABASE [Domotica] SET PARAMETERIZATION SIMPLE 
GO

ALTER DATABASE [Domotica] SET READ_COMMITTED_SNAPSHOT OFF 
GO

ALTER DATABASE [Domotica] SET HONOR_BROKER_PRIORITY OFF 
GO

ALTER DATABASE [Domotica] SET RECOVERY FULL 
GO

ALTER DATABASE [Domotica] SET  MULTI_USER 
GO

ALTER DATABASE [Domotica] SET PAGE_VERIFY CHECKSUM  
GO

ALTER DATABASE [Domotica] SET DB_CHAINING OFF 
GO

ALTER DATABASE [Domotica] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO

ALTER DATABASE [Domotica] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO

ALTER DATABASE [Domotica] SET DELAYED_DURABILITY = DISABLED 
GO

ALTER DATABASE [Domotica] SET QUERY_STORE = OFF
GO

ALTER DATABASE [Domotica] SET  READ_WRITE 
GO


USE [Domotica]
GO

/****** Object:  Table [dbo].[Alarma]    Script Date: 04/07/2019 0:59:58 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Alarma](
	[Estado] [varchar](50) NULL
) ON [PRIMARY]
GO



USE [Domotica]
GO

/****** Object:  Table [dbo].[Fuego]    Script Date: 04/07/2019 1:00:11 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Fuego](
	[Estado] [varchar](50) NULL
) ON [PRIMARY]
GO


USE [Domotica]
GO

/****** Object:  Table [dbo].[Luces]    Script Date: 04/07/2019 1:00:35 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Luces](
	[Luz] [nchar](10) NULL,
	[Estado] [varchar](50) NULL
) ON [PRIMARY]
GO


USE [Domotica]
GO

/****** Object:  Table [dbo].[Temperatura]    Script Date: 04/07/2019 1:00:46 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Temperatura](
	[Humedad] [varchar](50) NULL,
	[Temperatura] [varchar](50) NULL,
	[IndiceCalor] [varchar](50) NULL
) ON [PRIMARY]
GO

