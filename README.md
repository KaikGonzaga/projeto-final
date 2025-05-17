# 📋 Sistema de Cadastro de Clientes - XYZ Comércio

Este projeto é uma aplicação web desenvolvida em **Python com Streamlit**, com o objetivo de ajudar o comércio **XYZ** a organizar o cadastro de seus clientes. O sistema permite **cadastrar, consultar, editar e excluir clientes**, garantindo facilidade de uso e acesso rápido às informações.

---

## 🚀 Funcionalidades

- ✅ Cadastro de novos clientes
- 🔍 Consulta rápida por nome
- ✏️ Edição dos dados dos clientes
- ❌ Exclusão de registros
- 🧪 Testes unitários com `pytest`

---

## 🛠 Tecnologias Utilizadas

- [Python 3.9+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pytest](https://docs.pytest.org/)
- Armazenamento local em **JSON**

---

## 📁 Estrutura do Projeto

```plaintext
cliente_app/
│
├── data/
│   └── clientes.json             # Base de dados dos clientes
│
├── app.py                        # Interface web (Streamlit)
├── cliente_manager.py            # Lógica de manipulação dos dados
├── test_cliente_manager.py       # Testes automatizados
└── requirements.txt              # Bibliotecas necessárias
