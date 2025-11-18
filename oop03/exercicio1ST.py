import exercicio1a as p
import streamlit as st


st.header("Programação Orientada a Objetos em Streamlit")
st.title("Função 1: Pessoa mais velha")

#Entrada de dados
nome = (st.text_input("Nome da pessoa 1"))
idade = (st.number_input("Idade da pessoa 1", min_value=0, step=1))
nome = (st.text_input("Nome da pessoa 2"))
idade = (st.number_input("Idade da pessoa 2", min_value=0, step=1))


#Instanciar o meu objeto
resultado = p.Pessoa(nome, idade)

#Processamento de dados
st.button("Calcular pessoa mais velha")

#Saída de dados
st.write(f"O mais velho é o = {p.Pessoa}")


