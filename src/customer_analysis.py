import pandas as pd
from db_manager import db

def analyze_top_customers():
    try:
        engine = db.engine
       
        # 1. Estrazione (Query mirate, non carichiamo tutto il DB!)
        # Prendiamo i clienti
        cust_query = "SELECT CustomerID, FirstName, LastName, CompanyName FROM SalesLT.Customer"
        df_customers = pd.read_sql(cust_query, engine)

        # Prendiamo gli ordini
        orders_query = "SELECT CustomerID, TotalDue FROM SalesLT.SalesOrderHeader"
        df_orders = pd.read_sql(orders_query, engine)

        # --- FASE 1: DATA CLEANING ---
        # Verifichiamo se ci sono nulli fastidiosi (importante per il valore del dato)
        # Se CompanyName è nullo, mettiamo 'Private Citizen'
        df_customers['CompanyName'] = df_customers['CompanyName'].fillna('Private Citizen')

        # --- FASE 2: DATA MERGING (Il JOIN di Python) ---
        # Uniamo i due DataFrame sulla chiave CustomerID
        df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how='inner')

        # --- FASE 3: ANALISI E AGGREGAZIONE ---
        # Calcoliamo la spesa totale per ogni azienda/cliente
        top_spenders = df_merged.groupby(['CompanyName', 'FirstName', 'LastName'])['TotalDue'].sum().reset_index()

        # Ordiniamo per spesa decrescente
        top_spenders = top_spenders.sort_values(by='TotalDue', ascending=False)

        print("\n--- TOP 10 SPENDERS (AdventureWorks) ---")
        print(top_spenders.head(10))

        # Esportiamo in Excel (un classico nelle offerte Spindox per i clienti)
        top_spenders.to_excel("data/top_spenders_report.xlsx", index=False)

    except Exception as e:
        print(f"Errore nell'analisi: {e}")

if __name__ == "__main__":
    analyze_top_customers()