.open salesdb.db

-- DROP TABLE tblagents;
-- DROP TABLE tblSales;


Create table tblagents(
agentno integer primary key,
agentname text not null,
agentcity text CHECK (agentcity in ('pune','mumbai','surat','baroda'))); 

create table tblSales (
salesid integer primary key,
agentno integer references tblagents(agentno),
saledate text not null,
custname text not null,
sales_amount integer,
commission real );

insert into tblagents values (1001 ,'yash','pune'),
(1002 ,'akash','pune'),
(1003 ,'meet','mumbai'),
(1004 ,'shiv','baroda'),
(1005 ,'ajay','surat');

insert into tblSales values (1,1001,'27/10/2006','kano',55000,5500),
(2,1002,'15/6/2020','manoj',null,null),
(3,1005,'20/6/2013','raj',600000,60000),
(4,1005,'10/2/2015','kano',700000,70000),
(5,1004,'27/2/2015','kano',50000,5000);
select * from tblagents;
select * from tblSales;


-- select count(agentno),agentcity from tblagents group by agentcity;

-- select agentname,agentcity from tblagents where agentcity="surat" and (agentname GLOB 'a*' or agentname GLOB 'e*' or agentname GLOB 'i*' or agentname GLOB 'o*' or agentname GLOB 'u*');

-- select a.agentname,s.sales_amount from tblagents a, tblSales s where a.agentno=s.agentno and sales_amount>50000;

-- select * from tblSales where sales_amount=(select min(sales_amount) from tblSales);

-- delete from tblSales where sales_amount is NULL and saledate between "'now','-1 year'" and "now";

-- -- -- --select agentno from tblSales where saledate between '10/2/2013' and '04/09/2014';

-- select a.agentname ,s.commission from tblagents a,tblSales s where a.agentno=s.agentno and a.agentcity="surat" and s.commission>60000;

-- -- -- -- select count(salesid) from tblSales where saledate = "__/2/2015";