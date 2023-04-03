import pymysql

class DBConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        try:
            connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return connection
        except Exception as e:
            print(f"Erreur lors de la connexion à la base de données: {e}")
            return None

    def close(self, connection):
        if connection:
            connection.close()


host = 'localhost'
user = 'root'
password = '1234'
database = 'myDiscord'

db_connector = DBConnector(host, user, password, database)
connection = db_connector.connect()



db_connector.close(connection)