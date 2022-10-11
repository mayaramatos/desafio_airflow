import pandas as pd
import sqlite3

def join_tables():
    # Conexão sqlite 
    con = sqlite3.connect('/home/mayara/airflow_tooltorial/data/Northwind_small.sqlite')

    cursor = con.cursor()
    order_datail = pd.read_sql ('select * from "OrderDetail"', con)
    orders = pd.read_csv('output_orders.csv', sep = ',')
  
   # Alterarando o nome da coluna ID
    orders = orders.rename(columns={'Id': 'OrderId'}) 

    # Realizando o Join
    join = pd.merge(order_datail, orders, how='left', on = 'OrderId')

    # Filtrando pela cidade do Rio de Janeiro
    join = join[join['ShipCity'] == 'Rio de Janeiro']

    # Transformando o resultado em string
    soma_quantidade = str(join['Quantity'].sum())
    print (soma_quantidade)

    # Gerando o arquivo count.txt
    with open("count.txt" , "w") as folder:
        folder.write(soma_quantidade)
    
    return soma_quantidade
