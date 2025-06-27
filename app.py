import streamlit as st
from pymongo import MongoClient
import pandas as pd

# Conexão com o MongoDB
client = MongoClient("mongodb+srv://ryant3525:talpo100@meucluster.yyky9es.mongodb.net/?retryWrites=true&w=majority&appName=meucluster")
db = client["eshop_brasil"]
clientes = db["clientes"]
outros = db["outros_dados"]  # Para a parte de concatenação

st.title("E-Shop Brasil - Gestão de Clientes")

# Barra lateral com opções
opcao = st.sidebar.radio("Selecione uma funcionalidade:", [
    "Inserir Dados",
    "Visualizar Dados",
    "Editar/Excluir Dados",
    "Concatenar Dados",
    "Buscar por Filtro"
])

# Inserção
if opcao == "Inserir Dados":
    st.subheader("Inserir novo cliente")
    with st.form("form_inserir"):
        nome = st.text_input("Nome")
        email = st.text_input("Email")
        cidade = st.text_input("Cidade")
        produto = st.selectbox("Produto", ["Notebook", "Celular", "Tênis", "Livro", "Fone"])
        valor = st.number_input("Valor (R$)", min_value=0.0)
        submit = st.form_submit_button("Salvar")
        if submit:
            clientes.insert_one({
                "nome": nome,
                "email": email,
                "cidade": cidade,
                "produto": produto,
                "valor": valor
            })
            st.success("Cliente inserido com sucesso!")

# Visualização
elif opcao == "Visualizar Dados":
    st.subheader("Lista de clientes")
    dados = list(clientes.find({}, {'_id': 0}))
    st.dataframe(pd.DataFrame(dados))

# Edição ou exclusão
elif opcao == "Editar/Excluir Dados":
    st.subheader("Editar ou excluir cliente")
    lista = list(clientes.find())
    nomes = [f"{doc['nome']} - {doc['_id']}" for doc in lista]
    selecionado = st.selectbox("Selecione um cliente", nomes)
    doc_id = lista[nomes.index(selecionado)]['_id']
    doc = clientes.find_one({'_id': doc_id})

    novo_nome = st.text_input("Nome", value=doc['nome'])
    novo_email = st.text_input("Email", value=doc['email'])
    novo_cidade = st.text_input("Cidade", value=doc['cidade'])
    novo_produto = st.text_input("Produto", value=doc['produto'])
    novo_valor = st.number_input("Valor (R$)", value=doc['valor'])

    col1, col2 = st.columns(2)
    if col1.button("Atualizar"):
        clientes.update_one(
            {"_id": doc_id},
            {"$set": {
                "nome": novo_nome,
                "email": novo_email,
                "cidade": novo_cidade,
                "produto": novo_produto,
                "valor": novo_valor
            }}
        )
        st.success("Cliente atualizado!")
    if col2.button("Excluir"):
        clientes.delete_one({"_id": doc_id})
        st.warning("Cliente removido.")

# Concatenação de coleções
elif opcao == "Concatenar Dados":
    st.subheader("Concatenar com 'outros_dados'")
    dados1 = list(clientes.find({}, {'_id': 0}))
    dados2 = list(outros.find({}, {'_id': 0}))
    df = pd.DataFrame(dados1 + dados2)
    st.dataframe(df)

# Filtros de busca
elif opcao == "Buscar por Filtro":
    st.subheader("Buscar por cidade ou produto")
    cidade_filtro = st.text_input("Filtrar por cidade")
    produto_filtro = st.selectbox("Produto", ["", "Notebook", "Celular", "Tênis", "Livro", "Fone"])
    query = {}
    if cidade_filtro:
        query["cidade"] = cidade_filtro
    if produto_filtro:
        query["produto"] = produto_filtro

    resultados = list(clientes.find(query, {'_id': 0}))
    st.dataframe(pd.DataFrame(resultados))