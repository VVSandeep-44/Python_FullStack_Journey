use pallesql;
select * from department;
select * from employee;

-- Write an UPDATE query that:

-- Updates the employee table
-- Increases salary by 10%
-- Only affects employees whose job_title is 'Developer'
-- Only affects employees belonging to the IT department
-- Do not hard-code department_id = 1
-- Hint

-- You'll need to think about how to identify the IT department without directly using its ID.
-- This is deliberately testing whether you can combine UPDATE + WHERE + a subquery.

update employee set salary = salary* 1.10 
where 
department_id=(select department_id from department where department_id=1) and job_title="Developer"