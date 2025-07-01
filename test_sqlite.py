import sqlite3

# Tenta criar um banco de dados de teste
db_path = 'test_db.sqlite3'

try:
    # Conecta ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Cria uma tabela de teste
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teste (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL
        )
    ''')
    
    # Insere um registro de teste
    cursor.execute('INSERT INTO teste (nome) VALUES (?)', ('Teste',))
    conn.commit()
    
    # Verifica se a tabela foi criada
    cursor.execute('SELECT * FROM teste')
    print('Tabela criada e registro inserido com sucesso!')
    
    # Fecha a conexão
    conn.close()
    print('Conexão com SQLite3 funcionando corretamente!')
    
except sqlite3.Error as e:
    print(f'Erro ao trabalhar com SQLite3: {e}')
