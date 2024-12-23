query_creacion_bbdd = "CREATE SCHEMA IF NOT EXISTS `estudio_satisfaccion` DEFAULT CHARACTER SET utf8 ;"

query_creacion_tabla_info_personal = """
    CREATE TABLE if not exists `estudio_satisfaccion`.info_personal (
	employeenumber INT NOT NULL,
    age INT NOT NULL,
    gender CHAR(10),
    education INT NULL,
    educationfield VARCHAR(50),
    PRIMARY KEY (employeenumber)
    );"""

query_creacion_tabla_satisfaccion = """CREATE TABLE if not exists `estudio_satisfaccion`.satisfaccion (
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
        ON UPDATE CASCADE );"""

query_creacion_tabla_info_salario = """"CREATE TABLE if not exists `estudio_satisfaccion`.info_salario (
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
        ON UPDATE CASCADE );"""


query_creacion_tabla_info_trabajo = """CREATE TABLE if not exists `estudio_satisfaccion`.info_trabajo (
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
"""