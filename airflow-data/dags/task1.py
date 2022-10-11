import pandas as pd
import sqlite3

def ler_csv():
    # Conectando com o banco sqlite:
    con = sqlite3.connect('/home/mayara/airflow_tooltorial/data/Northwind_small.sqlite')
    df = pd.read_sql_query('select * from "order"', con)
    
    # Escrevendo o arquivo output_orders.csv 
    df.to_csv('output_orders.csv', index = False)

    con.close()