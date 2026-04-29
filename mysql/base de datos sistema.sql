-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema SistemaDB
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema SistemaDB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `SistemaDB` DEFAULT CHARACTER SET utf8 ;
USE `SistemaDB` ;

-- -----------------------------------------------------
-- Table `SistemaDB`.`Departamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SistemaDB`.`Departamento` (
  `idDepartamento` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `gerente` VARCHAR(45) NULL,
  UNIQUE INDEX `idDepartamento_UNIQUE` (`idDepartamento` ASC) VISIBLE,
  PRIMARY KEY (`idDepartamento`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SistemaDB`.`Empleado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SistemaDB`.`Empleado` (
  `idEmpleado` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `rut` VARCHAR(45) NULL,
  `correo` VARCHAR(45) NULL,
  `contrasena` VARCHAR(45) NULL,
  `rol` VARCHAR(45) NULL,
  `telefono` VARCHAR(45) NULL,
  `salario` INT NULL,
  `inicio_contrato` VARCHAR(45) NULL,
  `Departamento_idDepartamento` INT NOT NULL,
  PRIMARY KEY (`idEmpleado`, `Departamento_idDepartamento`),
  UNIQUE INDEX `idEmpleado_UNIQUE` (`idEmpleado` ASC) VISIBLE,
  INDEX `fk_Empleado_Departamento_idx` (`Departamento_idDepartamento` ASC) VISIBLE,
  CONSTRAINT `fk_Empleado_Departamento`
    FOREIGN KEY (`Departamento_idDepartamento`)
    REFERENCES `SistemaDB`.`Departamento` (`idDepartamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SistemaDB`.`Administrador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SistemaDB`.`Administrador` (
  `idAdministrador` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `rut` VARCHAR(45) NULL,
  `correo` VARCHAR(45) NULL,
  `contrasena` VARCHAR(45) NULL,
  `rol` VARCHAR(45) NULL,
  PRIMARY KEY (`idAdministrador`),
  UNIQUE INDEX `idAdministrador_UNIQUE` (`idAdministrador` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SistemaDB`.`Proyecto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SistemaDB`.`Proyecto` (
  `idProyecto` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `descripcion` VARCHAR(45) NULL,
  `fecha_inicio` VARCHAR(45) NULL,
  PRIMARY KEY (`idProyecto`),
  UNIQUE INDEX `idProyecto_UNIQUE` (`idProyecto` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SistemaDB`.`Registro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SistemaDB`.`Registro` (
  `idRegistro` INT NOT NULL AUTO_INCREMENT,
  `fecha` VARCHAR(45) NULL,
  `hora` VARCHAR(45) NULL,
  `descripcion` VARCHAR(45) NULL,
  `Empleado_idEmpleado` INT NOT NULL,
  `Proyecto_idProyecto` INT NOT NULL,
  PRIMARY KEY (`idRegistro`, `Empleado_idEmpleado`, `Proyecto_idProyecto`),
  UNIQUE INDEX `idRegistro_UNIQUE` (`idRegistro` ASC) VISIBLE,
  INDEX `fk_Registro_Empleado1_idx` (`Empleado_idEmpleado` ASC) VISIBLE,
  INDEX `fk_Registro_Proyecto1_idx` (`Proyecto_idProyecto` ASC) VISIBLE,
  CONSTRAINT `fk_Registro_Empleado1`
    FOREIGN KEY (`Empleado_idEmpleado`)
    REFERENCES `SistemaDB`.`Empleado` (`idEmpleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Registro_Proyecto1`
    FOREIGN KEY (`Proyecto_idProyecto`)
    REFERENCES `SistemaDB`.`Proyecto` (`idProyecto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
