import streamlit as st
st.set_page_config("Simulação Lançamento Dardos")
def grafico(dardo1,dardo2,dardo3):
    #Apresentação de gráfico exibindo lançamento
    st.area_chart([0,dardo1],use_container_width=True,height=200,color="#c3f709")
    st.area_chart([0,dardo2],use_container_width=True,height=200,color="#ec2607")
    st.area_chart([0,dardo3],use_container_width=True,height=200,color="#094bfe")
st.title("Simulação de lançamento de dardos🤷‍♂️")
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
maior_distancia= max(dardo1,dardo2,dardo3)
#Estrutura de controle de decisão
if (dardo1>dardo2) and (dardo1>dardo3):
    dardo_vencedor="Dardo 1"
elif (dardo2>dardo1) and (dardo2>dardo3):
    dardo_vencedor="Dardo 2"
elif dardo1==dardo2 or dardo1==dardo3 or dardo2==dardo3:
    dardo_vencedor="Empate"
#else:
    #dardo_vencedor="Dardo 3"
#Saída de dados
if st.button("Apresentar resultados de lançamento"):
    if dardo_vencedor=="Empate":
        st.write("Houve empate sem vencedores")
    st.write(f"O dardo com a maior distância é o: {dardo_vencedor} com a maior distância sendo: {maior_distancia}")
    grafico(dardo1,dardo2,dardo3)
