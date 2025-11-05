import streamlit as st
#Atividade01
#Cálculo de troco
TITULO="Cálculo de troco"
st.set_page_config(page_title=TITULO)
st.markdown(f"<h2 style='text-align: center;'>{TITULO}</h2>", unsafe_allow_html=True)
#st.title("Cálculo de troco")
#Entrada de dados
precounitario=st.number_input("Digite o preço unitário em R$:",min_value=0.0, help="Insira o preço em reais unitário para ser calculado o troco.")
quantidadecomprada=st.number_input("Digite a quantidade comprada:",min_value=0, help="Insira a quantidade comprada.")
valorrecebido=st.number_input("Digite o valor recebido em R$:",min_value=0.0, help="Insira o valor pago em reais para ser calculado o troco.")
#Processamento de dados
calculotroco=valorrecebido-(precounitario*quantidadecomprada)
#Saída de dados
st.write(f"Seu troco será: {calculotroco:.2f} reais.")