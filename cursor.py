from logger_base import log
from connection import Connection

class Cursor:
    
    def __init__(self):
        self._connection = None
        self._cursor = None
    
    def __enter__(self):
        log.debug('Entering with method')
        self._connection = Connection.getConnection()
        self._cursor = self._connection.cursor()
        return self._cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('Exiting with method')
        if exc_val:
            self._connection.rollback()
            log.error(f'An error has occurred, a rollback has been done: {exc_val} {exc_type} {exc_tb}')
        else:
            self._connection.commit()
            log.debug(f'Transaction commited.')
        
        self._cursor.close()
        Connection.freeConnection(self._connection)