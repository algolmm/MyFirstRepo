import urllib
import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Carichiamo le variabili dal file .env
load_dotenv()

password = os.getenv('DB_PASS')
# Trasforma i caratteri speciali in formato "URL safe"
encoded_password = urllib.parse.quote_plus(password)

# Costruiamo la stringa di connessione (per Azure SQL)
# Se usi il Driver 18, ricorda che spesso richiede TrustServerCertificate=yes
conn_str = (
    f"mssql+pyodbc://{os.getenv('DB_USER')}:{encoded_password}@"
    f"{os.getenv('DB_SERVER')}/{os.getenv('DB_NAME')}?"
    "driver=ODBC+Driver+17+for+SQL+Server")


try:
    engine = create_engine(conn_str)
    
    # La tua query SQL (sfrutta la tua competenza senior)
    query = "SELECT TOP 10 * FROM SalesLT.Customer"
    
    # Portiamo tutto in un DataFrame Pandas
    df = pd.read_sql(query, engine)
    
    print("Connessione ad Azure riuscita!")
    print(df.head())

except Exception as e:
    print(f"Errore di connessione: {e}")