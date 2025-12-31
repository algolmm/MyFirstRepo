import os
import urllib
from sqlalchemy import create_engine
from dotenv import load_dotenv

class AdventureWorksDBManager:
    def __init__(self):
        load_dotenv()
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASS')
        self.server = os.getenv('DB_SERVER')
        self.database = os.getenv('DB_NAME')
        self.driver = "ODBC Driver 17 for SQL Server" # O quello che hai verificato

        self.engine = self.create_db_engine()

    def create_db_engine(self):
        password = os.getenv('DB_PASS')
        encoded_password = urllib.parse.quote_plus(password)

        conn_str = (
            f"mssql+pyodbc://{os.getenv('DB_USER')}:{encoded_password}@"
            f"{os.getenv('DB_SERVER')}/{os.getenv('DB_NAME')}?"
            "driver=ODBC+Driver+17+for+SQL+Server")

        try:
            engine = create_engine(conn_str, echo=False)
            print("Connessione al database: {self.database} stabilita con successo.")
            return engine
        except Exception as e:
            print(f"Errore di connessione al database: {e}")
            return None
        
db = AdventureWorksDBManager()