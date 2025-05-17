import streamlit as st
from client_manager import *

st.set_page_config(page_title="Cadastro de Clientes - XYZ", layout="centered")
st.title("📋 Sistema de Cadastro de Clientes")

criar_tabela()

menu = st.sidebar.selectbox("Menu", ["Cadastrar", "Consultar / Editar / Excluir"])

if menu == "Cadastrar":
    st.subheader("Cadastrar Novo Cliente")
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    telefone = st.text_input("Telefone")
    endereco = st.text_input("Endereço")

    if st.button("Salvar"):
        if nome and email:
            novo_cliente = {"nome": nome, "email": email, "telefone": telefone, "endereco": endereco}
            adicionar_cliente(novo_cliente)
            st.success("Cliente cadastrado com sucesso!")
        else:
            st.warning("Nome e e-mail são obrigatórios!")

elif menu == "Consultar / Editar / Excluir":
    st.subheader("Lista de Clientes")
    clientes = listar_clientes()

    if not clientes:
        st.info("Nenhum cliente cadastrado.")
    else:
        for cliente in clientes:
            cliente_id, nome, email, telefone, endereco = cliente
            with st.expander(f"{nome} ({email})"):
                editar = st.checkbox("Editar", key=f"edit_{cliente_id}")

                if editar:
                    novo_nome = st.text_input("Nome", value=nome, key=f"nome_{cliente_id}")
                    novo_email = st.text_input("Email", value=email, key=f"email_{cliente_id}")
                    novo_telefone = st.text_input("Telefone", value=telefone, key=f"tel_{cliente_id}")
                    novo_endereco = st.text_input("Endereço", value=endereco, key=f"end_{cliente_id}")

                    if st.button("Salvar Alterações", key=f"save_{cliente_id}"):
                        cliente_atualizado = {
                            "nome": novo_nome,
                            "email": novo_email,
                            "telefone": novo_telefone,
                            "endereco": novo_endereco
                        }
                        editar_cliente(cliente_id, cliente_atualizado)
                        st.success("Cliente atualizado com sucesso!")

                if st.button("Excluir", key=f"del_{cliente_id}"):
                    excluir_cliente(cliente_id)
                    st.warning("Cliente excluído com sucesso!")
