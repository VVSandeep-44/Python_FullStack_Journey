use pallesql;

show tables;

CREATE TABLE department(
    department_id INT PRIMARY KEY,
    department_name VARCHAR(20) UNIQUE,
    location VARCHAR(20) NOT NULL
);

select * from department;

CREATE TABLE employee(
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10,2) NOT NULL,
    job_title VARCHAR(50),
    department_id INT NOT NULL,
    FOREIGN KEY(department_id) REFERENCES department(department_id),
    hire_date DATE,
    manager_id INT
);

select * from employee;


INSERT INTO department (department_id, department_name, location)
VALUES
(1, 'IT', 'Bangalore'),
(2, 'HR', 'Hyderabad'),
(3, 'Finance', 'Mumbai'),
(4, 'Marketing', 'Chennai'),
(5, 'Sales', 'Pune');


INSERT INTO employee
(employee_id, employee_name, email, salary, job_title, department_id, hire_date, manager_id)
VALUES
(101, 'Ravi', 'ravi@gmail.com', 55000, 'Developer', 1, '2023-01-15', NULL),
(102, 'Priya', 'priya@gmail.com', 65000, 'Developer', 1, '2022-06-10', 101),
(103, 'Arjun', 'arjun@gmail.com', 75000, 'Analyst', 3, '2021-03-20', NULL),
(104, 'Sneha', 'sneha@gmail.com', 50000, 'HR Executive', 2, '2024-02-05', NULL),
(105, 'Kiran', 'kiran@gmail.com', 90000, 'Manager', 1, '2020-08-05', 101);


