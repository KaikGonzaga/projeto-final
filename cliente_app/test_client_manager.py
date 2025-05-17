import pytest
import sqlite3
import os
from client_manager import *

TEST_DB = "database.db"

# Substitui o nome do banco de dados temporariamente
def setup_module(module):
    global DB_NAME
    DB_NAME = TEST_DB
    criar_tabela()

def teardown_module(module):
    os.remove(TEST_DB)

def test_adicionar_e_listar_cliente():
    cliente = {
        "nome": "Teste Usuário",
        "email": "teste@example.com",
        "telefone": "123456789",
        "endereco": "Rua A, 123"
    }
    adicionar_cliente(cliente)
    clientes = listar_clientes()
    assert len(clientes) > 0
    assert clientes[-1][1] == "Teste Usuário"

def test_editar_cliente():
    clientes = listar_clientes()
    cliente_id = clientes[-1][0]
    cliente_atualizado = {
        "nome": "Usuário Editado",
        "email": "editado@example.com",
        "telefone": "000000000",
        "endereco": "Rua B, 456"
    }
    editar_cliente(cliente_id, cliente_atualizado)
    clientes = listar_clientes()
    assert clientes[-1][1] == "Usuário Editado"

def test_excluir_cliente():
    clientes = listar_clientes()
    cliente_id = clientes[-1][0]
    excluir_cliente(cliente_id)
    novos_clientes = listar_clientes()
    assert all(c[0] != cliente_id for c in novos_clientes)
