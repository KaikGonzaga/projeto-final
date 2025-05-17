# 📋 Sistema de Cadastro de Clientes - XYZ Comércio

Este projeto é uma aplicação web desenvolvida em **Python com Streamlit**, que permite à empresa **XYZ Comércio** cadastrar, consultar, editar e excluir clientes, utilizando um banco de dados **SQLite3** para armazenamento dos dados.

---

## 🚀 Funcionalidades

- ✅ Cadastro de novos clientes
- 🔍 Consulta de clientes cadastrados
- ✏️ Edição dos dados dos clientes
- ❌ Exclusão de clientes
- 🧪 Testes unitários com `pytest`

---

## 🛠 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [SQLite3](https://www.sqlite.org/index.html)
- [Pytest](https://docs.pytest.org/)

---

## 📁 Estrutura do Projeto

```plaintext
cliente_app/
│
├── app.py                      # Interface web com Streamlit
├── cliente_manager.py          # Operações com banco de dados SQLite3
├── test_cliente_manager.py     # Testes com pytest
├── database.db                 # Banco de dados SQLite3 (gerado automaticamente)
└── requirements.txt            # Dependências do projeto
