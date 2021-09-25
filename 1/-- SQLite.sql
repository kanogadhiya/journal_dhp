-- -- SQLite
-- Create table tblagents(
-- agentno integer primary key,
-- agentname text not null,
-- agentcity text CHECK (agentcity in ('pune','mumbai','surat','baroda'))); 

-- create table tblSales (
-- salesid integer primary key,
-- agentno integer references tblagents(agentno),
-- saledate text not null,
-- custname text not null,
-- sales_amount integer,
-- commission real );

-- insert into tblagents values (1001 ,'yash','pune'),
-- (1002 ,'akash','pune'),
-- (1005 ,'meet','mumbai'),
-- (1004 ,'shiv','baroda'),
-- (1005 ,'ajay','surat');

-- insert into tblSales values (1,1001,'27/10/2006','kano',55000,5500),
-- (2,1002,'15/6/2020','manoj',null,null),
-- (3,1003,'20/6/2013','raj',600000,60000),
-- (4,1005,'10/2/2015','kano',700000,70000),
-- (5,1004,'27/2/2015','kano',50000,5000);

select * from tblagents;
select * from tblSales;

-- -- -- --select * from tblSales where saledate = "*2/2015";

UPDATE tblSales set commission=commission+(commission/2) WHERE commission= (SELECT commission FROM tblSales GROUP by agentno);

-- SELECT s.* from tblagents a,tblSales s where a.agentno=s.agentno and a.agentname = "shiv";



-- SELECT sum(sales_amount) FROM tblSales where agentno=1005;

-- SELECT sum(s.sales_amount),a.agentcity from tblagents a,tblSales s where a.agentno=s.agentno GROUP by a.agentcity;

-- UPDATE tblagents set agentname="yesha" where agentname ="yash" and agentcity="pune"; 

SELECT a.agentname from tblagents a,tblSales s where a.agentno=s.agentno and commission is null;
