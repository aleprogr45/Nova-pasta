import streamlit as st

#Problema de números consecutivos
st.title("Calculadora de pares consecutivos")

#Entrada de Dados
numero = st.number_input("Digite um número inteiro", step=1)
botao = st.button("Calcular")

contagem = 0
soma = 0

if botao:
    if (numero%2) != 0:
        numero += 1
    soma = numero
    while contagem < 5:
            numero += 2
            contagem += 1
            soma += numero
    st.write(soma)

