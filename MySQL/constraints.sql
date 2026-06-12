use pallesql;

-- constraints assignment

create table emp
(
eid int primary key,
name varchar(40) not null,
salary int,
bg varchar(10) default 'O+ve',
age int check(age between 18 and 60),
email varchar(40) unique
)

select * from emp
insert into emp values(44, 'vijay', 23000, 'O-ve', 21, 'vvs@gmail.com')
insert into emp(eid, name, salary, age, email) values(30, 'ram', 22000, 21, 'srt@gmail.com')
insert into emp values(19, 'surya', 21000, 'B+ve', 22, null)