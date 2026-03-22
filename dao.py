from connectdb import con, cur
from name import Juice

def insert(juice: Juice):
    sql = 'insert into fruit_juice(name, price) values(?,?)'
    rs = con.execute(sql, (juice.name, juice.price))
    row = rs.rowcount
    if row>0:
        con.commit()
        return row
    else:
        return 0
    
def update(juice: Juice):
    sql = 'update fruit_juice set price = ? where id = ? '
    rs = con.execute(sql, (juice.price, juice.id))
    row = rs.rowcount
    if row>0:
        con.commit()
        return row
    else:
        return 0
    
def delete(id: int):
    sql = 'delete from fruit_juice where id = ?'
    rs = con.execute(sql, (id, ))
    row = rs.rowcount
    if row>0:
        con.commit()
        return row
    else:
        return 0
    
def select():
    sql = 'select * from fruit_juice'
    rs = con.execute(sql)
    Juices = rs.fetchall()
    if Juices:
        data = []
        for juice in Juices:
            id, name, price = juice
            data.append(Juice(id=id, name=name, price=price))
        return data
    else:
        return[]
    
def select_by_name(name: str):
    sql = 'select * from fruit_juice where name like ?'
    rs = con.execute(sql, ('%' + name + '%', ))
    Juices = rs.fetchall()
    if Juices:
        data = []
        for juice in Juices:
            id, name, price = juice
            data.append(Juice(id=id, name=name, price=price))
        return data
    else:
        return[]