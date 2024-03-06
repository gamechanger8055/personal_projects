import queue

class ConnectionPool:
    def __init__(self, max_connection):
        self.max_connection=max_connection
        self.connection=queue.Queue(max_connection)

    def getConnection(self):
        if not self.connection.full():
            connection=Connection()
            self.connection.put(connection)
            return connection
        else:
            return self.connection.get()

    def releaseConnection(self, connection):
        self.connection.put(connection)


class Connection:
    def __init__(self):
        self.is_on=False

    def open(self):
        self.is_on=True

    def close(self):
        self.is_on=False

pool=ConnectionPool(5)
print(pool.connection)
con1=pool.getConnection()
con1.open()
con1.close()
pool.releaseConnection(con1)
print(pool.connection)