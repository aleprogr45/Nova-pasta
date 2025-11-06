import streamlit as st
st.title("Simulação de lançamento \\n de dardos🤷‍♂️")
'''Simulação de lançamento de três dardos. O objetivo do aplicativo e mostrar o dardo com a maior distância'''
#Entrada de dados
st.header("Inserir as três distâncias dos dardos lançados pelo jogador.")
coluna1,coluna2,coluna3=st.columns(3)
with coluna1:
    dardo1=st.number_input("Distância do 1° Dardo",min_value=0)
with coluna2:
    dardo2=st.number_input("Distância do 2° Dardo",min_value=0)
with coluna3:
    dardo3=st.number_input("Distância do 3° Dardo",min_value=0)
#Estrutura de controle de decisão
if (dardo1>dardo2) and (dardo1>dardo3):
    dardo_vencedor="Dardo 1"
elif (dardo2>dardo1) and (dardo2>dardo3):
    dardo_vencedor="Dardo 2"
else:
    dardo_vencedor="Dardo 3"
#Saída de dados
if st.button("Apresentar resultados de lançamento"):
    st.write(f"O dardo com a maior distância é o: {dardo_vencedor}")
