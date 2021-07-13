from logger_base import log
from psycopg2 import pool
from werkzeug.security import generate_password_hash, check_password_hash
import sys

class Connection:
    
    # Change this with you database information
    _USER = 'postgres'
    _PASSWORD = 'yasuraoka060698'
    _HOST = 'localhost'
    _PORT = '5432'
    _DB = 'password_manager'
    
    _MIN_CONN = 1
    _MAX_CONN = 1
    _pool = None
    
    @classmethod
    def getPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CONN, cls._MAX_CONN, user=cls._USER, password=cls._PASSWORD, host=cls._HOST, port=cls._PORT, database=cls._DB)
                log.debug(f'Pool creation succesful: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'An error has occurred when getting the pool: {e}')
                sys.exit()
        else:
            return cls._pool
    
    @classmethod
    def getConnection(cls):
        connection = cls.getPool().getconn()
        log.debug(f'Connection gotten from pool: {connection}')
        return connection
    
    @classmethod
    def freeConnection(cls, connection):
        cls.getPool().putconn(connection)
        log.debug(f'Connection returned to the pool: {connection}')
    
    @classmethod
    def closeConnections(cls):
        log.debug(f'All connections closed')
        cls.getPool().closeall()