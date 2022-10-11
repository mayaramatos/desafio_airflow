
# Desafio Módulo V - Fundamentos de Engenharia de Dados

#

Trata-se de repositório cujo objetivo é obter a soma das quantidades vendidas, através da coluna quantity com destino para o Rio de Janeiro. 
Assim, necessitando o join das tabelas orders e order_detail.

A tabela output_orders.csv gerada pela task1 foi utilizada como a variável orders e order_datail direto do banco de dados.

Utilizou-se o banco de dados Northwind no formato Sqlite3.

Para entrega final há o arquivo final_output.txt, o qual foi gerado através da concatenação das strings do arquivo count.txt e a variável my_email criada no airflow tendo como value o meu email corporativo.

A orquestração do Airflow deu-se em três etapas:



![](Image\orquestracao_airflow.jpg)


## Resumo do Projeto 🎯

#

1. Clone do repositório
2. Criação do ambiente virtual
3. instalação do airflow através do install.sh
4. Configuração do AIRFLOW_HOME 
5. Criação da pasta dags e dos scripts necessários
6. Configuração da dags_folder = /home/mayara/airflow_tooltorial/airflow-data/dags
7. Criação da variável my_email
8. Execução do processo 

#

### Resultado dos processos executados com sucesso:


![](Image\airflow_tasks.jpg)