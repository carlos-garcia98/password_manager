from logger_base import log
from connection import Connection
from cursor import Cursor
from users import User

class UserDAO:
    
    _SELECT = 'SELECT * FROM accounts ORDER BY app_name'
    _INSERT = 'INSERT INTO accounts(app_name, username, password, url) VALUES(%s, %s, %s, %s)'
    _UPDATE = 'UPDATE accounts SET app_name = %s, username = %s, password = %s, url = %s WHERE id_account = %s'
    _DELETE = 'DELETE FROM accounts WHERE id_account = %s'
    
    @classmethod
    def select(cls):
        with Cursor() as cur:
            cur.execute(cls._SELECT)
            registers = cur.fetchall()
            users = []
            for i in registers:
                user = User(i[0], i[1], i[2], i[3], i[4])
                users.append(user)
            return users
    
    @classmethod
    def insert(cls, user):
        with Cursor() as cur:
            values = (user.app_name, user.username, user.password, user.url)
            cur.execute(cls._INSERT, values)
            log.info(f'Inserted user: {user}')
            return cur.rowcount
    
    @classmethod
    def update(cls, user):
        with Cursor() as cur:
            values = (user.app_name, user.username, user.password, user.url, user.id_account)
            cur.execute(cls._UPDATE, values)
            log.info(f'Updated user: {user}')
            return cur.rowcount
    
    @classmethod
    def delete(cls, user):
        with Cursor() as cur:
            values = (user.id_account,)
            cur.execute(cls._DELETE, values)
            log.info(f'Deleted user: {user}')
            return cur.rowcount