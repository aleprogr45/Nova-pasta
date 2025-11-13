import streamlit as st
#import markdown as st
st.title("Classificação de níveis de glicose no sangue")
st.markdown(
    """
    | Nível de glicose | Classificação |
    | ---------------- | ------------- |
    | 0 - 70           | Hipoglicemia  |
    | 71 - 100         | Normal        |
    | 101 - 140        | Pré-diabetes  |
    | 141 ou mais      | Diabetes      |
        """)
#Entradas de dados
glicose=st.number_input("Insira o nível de glicose no sangue (mg/dl):", min_value=0)
#st.button("Classificar")# Botão para classificar o nível de glicose
#Condição de estrutura
if st.button("Classificar"):
    if glicose <= 70:
        st.write("Nível de glicose: Hipoglicemia")
        #st.balloons()
        st.error("Vai no médico")
    elif 71 >= glicose <= 100:
        st.write("Nível de glicose: Normal")
    elif 101 >= glicose <= 140:
        st.write("Nível de glicose: Pré-diabetes")
    else:
        st.write("Nível de glicose: Diabetes")