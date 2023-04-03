from db_connector import DBConnector

class Message:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def send_message(self, user_id, channel_id, content):
        connection = self.db_connector.connect()
        if not connection:
            return None

        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO messages (user_id, channel_id, content) VALUES (%s, %s, %s)"
                cursor.execute(sql, (user_id, channel_id, content))
            connection.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Erreur lors de l'envoi du message: {e}")
            return None
        finally:
            self.db_connector.close(connection)

    def get_messages(self, channel_id):
        connection = self.db_connector.connect()
        if not connection:
            return []

        try:
            with connection.cursor() as cursor:
                sql = """SELECT messages.id, users.nom, users.prenom, messages.content, messages.timestamp
                         FROM messages
                         JOIN users ON users.id = messages.user_id
                         WHERE messages.channel_id = %s
                         ORDER BY messages.timestamp"""
                cursor.execute(sql, (channel_id,))
                result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"Erreur lors de la récupération des messages: {e}")
            return []
        finally:
            self.db_connector.close(connection)

    def delete_message(self, message_id):
        connection = self.db_connector.connect()
        if not connection:
            return False

        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM messages WHERE id = %s"
                cursor.execute(sql, (message_id,))
            connection.commit()
            return True
        except Exception as e:
            print(f"Erreur lors de la suppression du message: {e}")
            return False
        finally:
            self.db_connector.close(connection)