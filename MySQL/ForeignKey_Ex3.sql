use pallesql

-- Normalization (using foreign key)
-- Example-3 (Practice)

create table fkeycountry
(
country_id int primary key,
country_name varchar(40)
)
select * from fkeycountry
insert into fkeycountry values(1,'INDIA'),(2,'US')

create table fkeystate
(
state_id int primary key,
state_name varchar(40),
country_id int,
foreign key(country_id) references fkeycountry(country_id)
)
select * from fkeystate
insert into fkeystate values(1,'Karnataka',1),(2,'AP',1),(3,'Tamilnadu',1),(4,'California',2)


create table fkeycity
(
city_id int primary key,
city_name varchar(40),
state_id int,
foreign key(state_id) references fkeystate(state_id)
)
select * from fkeycity
insert into fkeycity values(1,'Bengaluru',1),(2,'kakinada',2),(3,'Vizag',2),(4,'chennai',3),(5,'San Francisco',4)


create table fkeystudent
(
sid int primary key,
sname varchar(40),
city_id int,
foreign key(city_id) references fkeycity(city_id)
)
select * from fkeystudent
insert into fkeystudent values(1,'vijay',2),(2,'sandeep',1),(3,'Raj',3)