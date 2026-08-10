from app import create_app
from app.extensions import db


app = create_app()


with app.app_context():

    try:
        db.engine.connect()

        print("✅ Connexion MySQL réussie")

    except Exception as e:

        print("❌ Erreur de connexion MySQL")
        print(e)
        