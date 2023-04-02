import sqlite3
import random
import string

# Fonction pour générer un mot de passe aléatoire
def generate_password():
    # Choisissez une longueur aléatoire pour le mot de passe
    length = random.randint(50, 51)

    # Choisissez des caractères aléatoires pour le mot de passe
    letters = string.ascii_letters + string.digits + '!@#%&-'
    #string.punctuation
    password = ''.join(random.choice(letters) for i in range(length))
    #letters = string.ascii_letters
    
    # Retourner le mot de passe généré
    return password

# Fonction pour effacer la table existante et créer une nouvelle table
def create_table():
    # Établir une connexion à la base de données
    conn = sqlite3.connect('results.db')

    # Supprimer la table existante
    conn.execute('DROP TABLE IF EXISTS results')

    # Créer la table
    conn.execute('''
        CREATE TABLE results (
            id INTEGER PRIMARY KEY,
            password TEXT
        )
    ''')

    # Fermer la connexion à la base de données
    conn.close()

# Fonction pour insérer des données dans la table
def insert_data(num_passwords):
    # Établir une connexion à la base de données
    conn = sqlite3.connect('results.db')

    # Insérer les données
    for i in range(num_passwords):
        password = generate_password()
        conn.execute('INSERT INTO results (password) VALUES (?)', (password,))

    # Valider les changements
    conn.commit()

    # Fermer la connexion à la base de données
    conn.close()

# Effacer la table existante et créer une nouvelle table
create_table()

# Générer et insérer 10 mots de passe aléatoires dans la table
insert_data(10)
