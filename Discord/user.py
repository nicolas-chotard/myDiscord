import hashlib

class User:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def authenticate(self, email, password):
        connection = self.db_connector.connect()
        if not connection:
            return None

        password_hash = hashlib.sha256(password.encode()).hexdigest()

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM users WHERE email = %s AND mot_de_passe = %s"
                cursor.execute(sql, (email, password_hash))
                result = cursor.fetchone()
            return result
        except Exception as e:
            print(f"Erreur lors de l'authentification de l'utilisateur: {e}")
            return None
        finally:
            self.db_connector.close(connection)

    def register(self, nom, prenom, email, password):
        connection = self.db_connector.connect()
        if not connection:
            return None

        password_hash = hashlib.sha256(password.encode()).hexdigest()

        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO users (nom, prenom, email, mot_de_passe) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (nom, prenom, email, password_hash))
            connection.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Erreur lors de l'inscription de l'utilisateur: {e}")
            return None
        finally:
            self.db_connector.close(connection)