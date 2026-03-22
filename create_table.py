from connectdb import con

sql = '''
    create table fruit_juice(
    id integer primary key autoincrement, 
    name text not null, 
    price integer not null)
'''

con.execute(sql)