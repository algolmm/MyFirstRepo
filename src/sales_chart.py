import urllib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

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

engine = create_engine(conn_str)

# Query: Uniamo gli ordini alle categorie
query = """
SELECT 
    pc.Name AS CategoryName, 
    SUM(sod.LineTotal) AS TotalSales
FROM SalesLT.SalesOrderDetail sod
JOIN SalesLT.Product p ON sod.ProductID = p.ProductID
JOIN SalesLT.ProductCategory pc ON p.ProductCategoryID = pc.ProductCategoryID
GROUP BY pc.Name
ORDER BY TotalSales DESC
"""
try:
    df = pd.read_sql(query, engine)

    # --- PARTE VISUAL ---
    plt.figure(figsize=(10, 6)) # Impostiamo la dimensione della "tela"
    
    # Usiamo Seaborn per un look professionale
    sns.barplot(x='TotalSales', y='CategoryName', data=df, palette='viridis')

    plt.title('Fatturato Totale per Categoria di Prodotto - AdventureWorks', fontsize=15)
    plt.xlabel('Fatturato ($)', fontsize=12)
    plt.ylabel('Categoria', fontsize=12)
    
    # Un tocco di classe: aggiungiamo una griglia leggera
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    # Salviamo il grafico per una futura presentazione
    plt.savefig('data/fatturato_categorie.png', bbox_inches='tight')
    
    plt.show() # Mostra il grafico a video

except Exception as e:
        print(f"Errore durante l'esecuzione della query o la visualizzazione: {e}")
