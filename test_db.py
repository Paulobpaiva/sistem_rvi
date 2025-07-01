import psycopg2

try:
    conn = psycopg2.connect(
        dbname='sistema_estacionamento',
        user='postgres',
        password='your_password',
        host='localhost',
        port='5432'
    )
    print("Conexão com o PostgreSQL bem-sucedida!")
    conn.close()
except Exception as e:
    print(f"Erro ao conectar ao PostgreSQL: {str(e)}")
