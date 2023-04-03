import pymysql
from db_connector import DBConnector


class Channel:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def get_channels(self):
        connection = self.db_connector.connect()
        if not connection:
            return []

        try:
            with connection.cursor() as cursor:
                sql = "SELECT id, nom FROM channels"
                cursor.execute(sql)
                result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"Erreur lors de la récupération des channels: {e}")
            return []
        finally:
            self.db_connector.close(connection)

    def add_channel(self, nom):
        connection = self.db_connector.connect()
        if not connection:
            return False

        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO channels (nom) VALUES (%s)"
                cursor.execute(sql, (nom,))
            connection.commit()
            return True
        except Exception as e:
            print(f"Erreur lors de l'ajout d'un channel: {e}")
            return False
        finally:
            self.db_connector.close(connection)