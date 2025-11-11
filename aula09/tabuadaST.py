import streamlit as st
#Tabuada
#Título
TITULO="Tabuada"
st.title(TITULO)
st.set_page_config(TITULO)
#Entrada de dados
n = None
try:
    n=int(st.text_input("Deseja a tabuada de qual número?"))
    for i in range(1,11):
        saida=f"{n} x {i} = {n*i}"
        st.markdown(f"""{saida}""")
except ValueError:
    if n is None: 
        st.warning("Digite somente número")
    else:
        st.error("Digite somente número inteiros")
    