from logger_base import log
from users import User
import sqlite3 as sl

class Connection:
    
    # QUERIES
    _CREATE_MAIN_TABLE = '''CREATE TABLE IF NOT EXISTS accounts(
        id_account INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        app_name TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        url TEXT NOT NULL)'''
    _SELECT = 'SELECT * FROM accounts ORDER BY id_account'
    _SELECT_BY_ID = 'SELECT * FROM accounts WHERE id_account=?'
    _SELECT_BY_APP_NAME = 'SELECT * FROM accounts WHERE app_name=?'
    _INSERT = 'INSERT INTO accounts(app_name, username, password, url) VALUES(?, ?, ?, ?)'
    _UPDATE = 'UPDATE accounts SET app_name=?, username=?, password=?, url=? WHERE id_account=?'
    _DELETE = 'DELETE FROM accounts WHERE id_account=?'
    _GET_PASSWORD_BY_ID = 'SELECT password FROM accounts WHERE id_account=?'
    _GET_PASSWORD_BY_APP_NAME = 'SELECT password FROM accounts WHERE app_name=?'
    _DB_NAME = 'password_manager.db'
    _connection = None
    _cursor = None
    
    # CLASS METHODS
    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = sl.connect(cls._DB_NAME)
            log.debug(f'Connection successfully established: {cls._connection}')
            return cls._connection
        else:
            return cls._connection
    
    @classmethod
    def get_cursor(cls):
        if cls._cursor is None:
            with Connection.get_connection():
                cls._cursor = Connection.get_connection().cursor()
                log.debug(f'The cursor has been created successfully: {cls._cursor}')
                return cls._cursor
        else:
            return cls._cursor
    
    @classmethod
    def create_table(cls):
        cursor = Connection.get_cursor()
        cursor.execute(cls._CREATE_MAIN_TABLE)
    
    @classmethod
    def select(cls):
        cursor = Connection.get_cursor()
        cursor.execute(cls._SELECT)
        registers = cursor.fetchall()
        accounts = []
        for i in registers:
            account = User(i[0], i[1], i[2], i[3], i[4])
            accounts.append(account)
        return accounts
    
    @classmethod
    def select_by_id(cls, user):
        cursor = Connection.get_cursor()
        values = (user.id_account,)
        cursor.execute(cls._SELECT_BY_ID, values)
        registers = cursor.fetchall()
        accounts = []
        for i in registers:
            account = User(i[0], i[1], i[2], i[3], i[4])
            accounts.append(account)
        return accounts
    
    @classmethod
    def select_by_app_name(cls, user):
        cursor = Connection.get_cursor()
        values = (user.app_name,)
        cursor.execute(cls._SELECT_BY_APP_NAME, values)
        registers = cursor.fetchall()
        accounts = []
        for i in registers:
            account = User(i[0], i[1], i[2], i[3], i[4])
            accounts.append(account)
        return accounts
    
    @classmethod
    def insert(cls, user):
        connection = Connection.get_connection()
        cursor = Connection.get_cursor()
        values = (user.app_name, user.username, user.password, user.url)
        cursor.execute(cls._INSERT, values)
        connection.commit()
        log.debug(f'Inserted account: {user}')
        return cursor.rowcount
    
    @classmethod
    def update(cls, user):
        connection = Connection.get_connection()
        cursor = Connection.get_cursor()
        values = (user.app_name, user.username, user.password, user.url, user.id_account) 
        cursor.execute(cls._UPDATE, values)
        connection.commit()
        log.debug(f'Updated account: {user}')
        return cursor.rowcount
    
    @classmethod
    def delete(cls, user):
        connection = Connection.get_connection()
        cursor = Connection.get_cursor()
        values = (user.id_account,)
        cursor.execute(cls._DELETE, values)
        connection.commit()
        log.debug(f'Deleted account: {user}')
        return cursor.rowcount
    
    @classmethod
    def get_password_by_id(cls,user):
        cursor = Connection.get_cursor()
        values = (user.id_account,)
        cursor.execute(cls._GET_PASSWORD_BY_ID, values)
        registers = cursor.fetchall()
        for i in registers:
            password = i
        return password
    
    @classmethod
    def get_password_by_app_name(cls, user):
        cursor = Connection.get_cursor()
        values = (user.app_name,)
        cursor.execute(cls._GET_PASSWORD_BY_APP_NAME, values)
        registers = cursor.fetchall()
        for i in registers:
            password = i
        return password

if __name__ == "__main__":
    # CONNECTION TEST
    # Connection.get_connection()
    # Connection.get_cursor()
    
    # CREATE TABLE TEST
    Connection.create_table()
    
    # INSERT TEST
    # account = User(app_name='test', username='testaccount', password='test123', url='testurl')
    # inserted_accounts = Connection.insert(account)
    # log.debug(f'Inserted accounts: {inserted_accounts}')
    
    # SELECT TEST
    accounts = Connection.select()
    for i in accounts:
        log.debug(i)