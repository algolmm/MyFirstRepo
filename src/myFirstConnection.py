import pandas as pd
from sqlalchemy import create_engine
from db_manager import db



try:
    engine = db.engine
    
    # La tua query SQL (sfrutta la tua competenza senior)
    query = "SELECT TOP 10 * FROM SalesLT.Customer"
    
    # Portiamo tutto in un DataFrame Pandas
    df = pd.read_sql(query, engine)
    
    print("Connessione ad Azure riuscita!")
    print(df.head())

except Exception as e:
    print(f"Errore di connessione: {e}")