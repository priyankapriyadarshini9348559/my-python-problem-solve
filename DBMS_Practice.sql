CREATE DATABASE CompanyDB;
USE CompanyDB;



CREATE TABLE Emplyoees(
        id INT PRIMARY KEY,
        name VARCHAR(50),
        department VARCHAR(50),
        salary INT
	
        );
-- Correct department table
CREATE TABLE department(
    id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

-- Correct employees table with foreign key
CREATE TABLE Emplyoees(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department_id INT,
    salary INT,
    FOREIGN KEY (department_id) REFERENCES department(id)
);

-- Insert data using department_id
INSERT INTO Emplyoees (id, name, department_id, salary)
VALUES
(1,'PRIYANKA',1,50000),
(2,'SMRUTI',2,40000),
(3,'BIKI',3,60000),
(4,'SUDARSAN',1,55000),
(5,'MAMUNI',2,45000);

INSERT INTO Emplyoees (id,name,department,salary)
VALUES(1,'PRIYANKA','IT',50000),
       (2, 'SMRUTI',  'HR', 40000),
       (3, 'BIKI',  'Finance', 60000),
	   (4, 'SUDARSAN',  'IT', 55000),
        (5, 'MAMUNI',  'HR', 45000);
INSERT INTO department(id, Depatment_name)
VALUES(1,'IT'),
	  (2,'HR'),
      (3,'Finance'),
      (4,'Marketing');
        
SELECT * FROM Emplyoees;
SELECT * FROM department;
SHOW TABLES;

INSERT INTO Emplyoees (id, name, department, salary)
VALUES
(6, 'Pallavi', 'IT', 52000),
(7, 'Praveen', 'HR', 48000);

SELECT name,salary FROM Emplyoees;
select * from Emplyoees where salary > 45000;
select * from Emplyoees where department='IT';
select * from Emplyoees where department='HR';
select avg(salary) as avg_salary FROM Emplyoees;
select department ,sum(salary) as total_salary from Emplyoees group by department;
select department ,count(*) as total_employees from Emplyoees group by department;
select department ,max(salary) as max_salary from Emplyoees group by department;
select department ,min(salary) as min_salary from Emplyoees group by department; 
