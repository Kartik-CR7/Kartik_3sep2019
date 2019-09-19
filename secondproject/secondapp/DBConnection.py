import cx_Oracle
con = cx_Oracle.connect('testuser1/pass@123@10.1.6.66/orcl')
cur = con.cursor()
cur.execute("create table pragati(id number primary key,age number(10))")

