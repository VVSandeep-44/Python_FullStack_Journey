use pallesql

-- Normalization (using foreign key)
-- Example-2 (Practice)

-- blood group table 
create table fkbg
(
bg_id int primary key,
bg varchar(10)
 )
select * from fkbg
insert into fkbg values(1,'O+ve'), (2,'O-ve'),(3,'A+ve'),(4,'A-ve')


-- state table 
create table fkstate
(
state_id int primary key,
state_name varchar(40)
)
select * from fkstate
insert into fkstate values(1,'Karnataka'),(2,'Andhra'),(3,'Tamilnadu')


-- employee table (bg_id & state_id as foreign keys)
create table fkemp
(
eid int primary key,
ename varchar(40),
age int,
bg_id int,
state_id int,
foreign key(bg_id) references fkbg(bg_id),
foreign key(state_id) references fkstate(state_id)
)
select * from fkemp
insert into fkemp values(544,'Vijay',21,1,2)
insert into fkemp values(530,'Ram',21,4, 1)
insert into fkemp values(519,'Surya',21,3,3)