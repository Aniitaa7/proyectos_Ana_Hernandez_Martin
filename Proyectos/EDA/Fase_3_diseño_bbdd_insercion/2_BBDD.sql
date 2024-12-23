CREATE SCHEMA `estudio_satisfaccion`;
USE `estudio_satisfaccion`;

CREATE TABLE info_personal (
	employeenumber INT NOT NULL,
    age INT NOT NULL,
    gender CHAR(10),
    education INT NULL,
    educationfield VARCHAR(50),
    PRIMARY KEY (employeenumber)
    );
SELECT * FROM info_personal

CREATE TABLE satisfaccion (
	employeenumber INT NOT NULL,
    environmentsatisfaction INT NULL DEFAULT NULL,
    relationshipsatisfaction INT NULL DEFAULT NULL, 
    jobsatisfaction INT NULL DEFAULT NULL,
    jobinvolvement INT NULL DEFAULT NULL,
    performancerating INT NULL DEFAULT NULL,
    worklifebalance INT NULL DEFAULT NULL,
    PRIMARY KEY (employeenumber),
    CONSTRAINT fk_satisfaccion_personal
		FOREIGN KEY (employeenumber)
        REFERENCES info_personal(employeenumber)
        ON DELETE CASCADE 
        ON UPDATE CASCADE );
        
SELECT * FROM satisfaccion
        
        
CREATE TABLE info_salario (
	employeenumber INT NOT NULL,
    monthlyincome FLOAT NULL DEFAULT NULL,
    monthlyrate FLOAT NULL DEFAULT NULL,
    percentsalaryhike INT NULL DEFAULT NULL, 
    salary FLOAT NULL DEFAULT NULL, 
    PRIMARY KEY (employeenumber),
    CONSTRAINT fk_salario_personal
		FOREIGN KEY (employeenumber)
        REFERENCES info_personal(employeenumber)
        ON DELETE CASCADE 
        ON UPDATE CASCADE );
        
SELECT * FROM info_salario
        
CREATE TABLE info_trabajo (
	employeenumber INT NOT NULL,
    attrition CHAR(10) NULL DEFAULT NULL, 
    businesstravel VARCHAR(50) NULL DEFAULT NULL, 
    jobrole VARCHAR(50) NULL DEFAULT NULL, 
    department VARCHAR(50) NULL DEFAULT NULL, 
    joblevel INT NULL DEFAULT NULL,
    overtime CHAR(10) NULL DEFAULT NULL,
    remotework CHAR(10) NULL DEFAULT NULL,
    distancefromhome INT NULL DEFAULT NULL,
    numcompaniesworked INT NULL DEFAULT NULL,
    trainingtimeslastyear INT NULL DEFAULT NULL,
    yearsatcompany INT NULL DEFAULT NULL,
    yearssincelastpromotion INT NULL DEFAULT NULL,
    yearswithcurrmanager INT NULL DEFAULT NULL,
    stockoptionlevel INT NULL DEFAULT NULL,
	PRIMARY KEY (employeenumber),
    CONSTRAINT fk_trabajo_personal
		FOREIGN KEY (employeenumber)
        REFERENCES info_personal(employeenumber)
        ON DELETE CASCADE 
        ON UPDATE CASCADE );
        
SELECT * FROM info_trabajo