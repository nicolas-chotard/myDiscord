import tkinter as tk
from tkinter import ttk, messagebox
from db_connector import DBConnector
from user import User
from channel import Channel
from message import Message

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()


        host = 'localhost'
        user = 'root'
        password = '1234'
        database = 'myDiscord'
        self.db_connector = DBConnector(host, user, password, database)

        self.user_manager = User(self.db_connector)
        self.channel_manager = Channel(self.db_connector)
        self.message_manager = Message(self.db_connector)


        self.title("MyDiscord")
        self.geometry("800x600")

        self.connected_user_label = tk.Label(self, text="Utilisateur connecté: Aucun")
        self.connected_user_label.pack(side=tk.TOP, anchor=tk.W, padx=5, pady=5)

        self.left_frame = tk.Frame(self)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.channel_list = ttk.Treeview(self.left_frame)
        self.channel_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.chat_area = tk.Text(self, wrap=tk.WORD)
        self.chat_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.entry = tk.Entry(self)
        self.entry.pack(side=tk.BOTTOM, fill=tk.X, expand=True)

        self.login_button = tk.Button(self, text="Se connecter", command=self.open_login_window)
        self.login_button.pack(side=tk.BOTTOM, padx=5, pady=5)

        self.logout_button = tk.Button(self, text="Se déconnecter", command=self.logout)
        self.logout_button.pack(side=tk.BOTTOM, padx=5, pady=5)

    def open_login_window(self):
        self.login_window = LoginWindow(self)

    def logout(self):
        pass

    def update_channels(self):
        pass

class LoginWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.user_manager = self.parent.user_manager

        self.title("Connexion")

        self.email_label = tk.Label(self, text="Email :")
        self.email_label.pack()

        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        self.password_label = tk.Label(self, text="Mot de passe :")
        self.password_label.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Se connecter", command=self.login)
        self.login_button.pack()

        self.signup_button = tk.Button(self, text="S'inscrire", command=self.open_signup_window)
        self.signup_button.pack()

    def login(self):
        pass

    def open_signup_window(self):
        self.signup_window = SignupWindow(self)

class SignupWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Inscription")
        self.parent = parent

        self.nom_label = tk.Label(self, text="Nom :")
        self.nom_label.pack()

        self.nom_entry = tk.Entry(self)
        self.nom_entry.pack()

        self.prenom_label = tk.Label(self, text="Prénom :")
        self.prenom_label.pack()

        self.prenom_entry = tk.Entry(self)
        self.prenom_entry.pack()

        self.email_label = tk.Label(self, text="Email :")
        self.email_label.pack()

        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        self.password_label = tk.Label(self, text="Mot de passe :")
        self.password_label.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.signup_button = tk.Button(self, text="S'inscrire", command=self.signup)
        self.signup_button.pack()

    def signup(self):
        nom = self.nom_entry.get()
        prenom = self.prenom_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not nom or not prenom or not email or not password:
            messagebox.showerror("Erreur", "Tous les champs sont obligatoires.")
            return

        try:
            self.parent.user_manager.register(nom, prenom, email, password)
            messagebox.showinfo("Succès", "Inscription réussie. Vous pouvez vous connecter.")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'inscription de l'utilisateur: {e}")


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()