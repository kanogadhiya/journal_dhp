import sqlite3 as s
db= s.connect('persondb.db')
# createquery = ''' create table person ( personid integer primary key,pname text not null,mono integer ,age integer not null);'''
# selectquery = "select * from person;"
# deletequery = "delete from person where pname=?;
#Query="insert into person (personid,pname,mono,age) valuse (1,'yash',82,18);"
# data=[(1,"yash",823829400,18),(2,"akash",8954263485,20),(3,"smit",7810654832,19)]
try :
    cur=db.cursor()
    # cur.execute('create table person ( personid integer primary key,pname text not null,mono integer,age integer not null);')
    cur.execute("insert into person (personid,pname,mono,age) valuse(1,'yash',82,18);")
    print('succuss.!!')
    db.commit()
except:
    print("error!")
    db.rollback()
db.close()
