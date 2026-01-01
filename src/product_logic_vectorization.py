import pandas as pd
from db_manager import db

def esercizio_sintassi_prodotto():
    try: 
        # 1. Recupero dati
        engine = db.engine
        query = "SELECT Name, ListPrice FROM SalesLT.Product"
        df = pd.read_sql(query, engine)

         # Il modo "Data Scientist" (Vectorization)
        df['Name'] = df.apply(lambda x: f"PREMIUM: {x['Name']}" if x['ListPrice'] > 500 else x['Name'], axis=1)

        # Stampiamo i primi 15 per vedere il risultato
        print("\n--- Risultato Trasformazione ---")
        for p in df['Name'].head(15):
            print(p)    

    except Exception as e:
        print(f"Errore durante l'esercizio: {e}")       

if __name__ == "__main__":  
    esercizio_sintassi_prodotto()   