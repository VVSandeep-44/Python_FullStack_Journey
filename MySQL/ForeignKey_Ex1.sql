use pallesql;

-- Normalization (using foreign key)
-- Example-1
create table state
(
state_id int primary key,
state_name varchar(40)
)
select * from state
insert into state values(1,'Karnataka'),(2,'Andhra'),(3,'Tamilnadu')

create table normstudent
(
sid int primary key,
name varchar(40),
state_id int,
foreign key(state_id) references state(state_id)
)
select * from normstudent
insert into normstudent values(1,'vijay',1)
insert into normstudent values(2,'Sandeep',2)
insert into normstudent values(2,'Ram',3) # duplicate data error
insert into normstudent values(3,'Sandeep',4) # foreign key error

