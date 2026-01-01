import pandas as pd
from db_manager import db

def esercizio_sintassi_prodotto():
    try: 
        # 1. Recupero dati
        engine = db.engine
        query = "SELECT Name, ListPrice FROM SalesLT.Product"
        df = pd.read_sql(query, engine)

        # Trasformiamo la colonna 'Name' in una lista Python per l'esercizio
        nomi_prodotti = df['Name'].tolist()
        prezzi_prodotti = df['ListPrice'].tolist()

        # Uniamo i due dati in una lista di tuple (Name, Price)
        # Zip è una funzione fantastica che "accoppia" le liste come una cerniera lampo
        catalogo = list(zip(nomi_prodotti, prezzi_prodotti))

        # --- IL CUORE DELL'ESERCIZIO: LIST COMPREHENSION ---
        # Obiettivo: Tag "PREMIUM" per chi costa > 500, altrimenti lasciamo il nome.
        # Sintassi: [valore_se_true if condizione else valore_se_false for elemento in lista]
        prodotti_taggati = [
            f"PREMIUM: {nome}" if prezzo > 500 else nome
            for nome, prezzo in catalogo
        ]
        # Stampiamo i primi 15 per vedere il risultato
        print("\n--- Risultato Trasformazione ---")
        for p in prodotti_taggati[:15]:
            print(p)

    except Exception as e:
        print(f"Errore durante l'esercizio: {e}")

if __name__ == "__main__":  
    esercizio_sintassi_prodotto()


