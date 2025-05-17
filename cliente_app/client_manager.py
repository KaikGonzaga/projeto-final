import sqlite3

DB_NAME = "database.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT,
            endereco TEXT
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_cliente(cliente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO clientes (nome, email, telefone, endereco)
        VALUES (?, ?, ?, ?)
    ''', (cliente["nome"], cliente["email"], cliente["telefone"], cliente["endereco"]))
    conn.commit()
    conn.close()

def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    dados = cursor.fetchall()
    conn.close()
    return dados

def editar_cliente(cliente_id, cliente_atualizado):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE clientes
        SET nome = ?, email = ?, telefone = ?, endereco = ?
        WHERE id = ?
    ''', (cliente_atualizado["nome"], cliente_atualizado["email"],
          cliente_atualizado["telefone"], cliente_atualizado["endereco"], cliente_id))
    conn.commit()
    conn.close()

def excluir_cliente(cliente_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
    conn.commit()
    conn.close()
