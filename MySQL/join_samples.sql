use pallesql

create DATABASE join_samples
use join_samples

create table T1( C1 int, C2 varchar(10), C3 int)
create table T2( C4 int, C5 varchar(10))

select * from T2

insert into T1 values (10, 'AA', 6), (20, 'BB', 80), (30, 'CC', 260), (4, 'DD', -60)
insert into T2 values (1, 'RR'), (20, 'JJ'), (60, 'KL'), (4, 'NM')


select t1.*, t2.* from T1 t1 inner join T2 t2 on t1.c3>t2.c4

select t1.*, t2.* from T1 t1 inner join T2 t2 on t1.c1 != t2.c4