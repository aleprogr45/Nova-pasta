import streamlit as st
def calculo_perimetro(c):
    return(medidaA+medidaB+medidaC)

def area_trapezio(d):
    return ((medidaA+medidaB)*medidaC)/2

def forma_triangulo(e):
    return (medidaA<medidaB+medidaC) and (medidaB<medidaA+medidaC) and (medidaC<medidaA+medidaB)

    
#Problema triângulo
st.title("Cálculo perímetro triângulo")
st.set_page_config("Cálculo perímetro triângulo")
#Entrada de dados
medidaA=st.number_input("Inserir a medida A:", min_value=0)
medidaB=st.number_input("Inserir a medida B:", min_value=0)
medidaC=st.number_input("Inserir a medida C:", min_value=0)
calculo_perimetro=(medidaA+medidaB+medidaC)

#Processamento de dados
# if st.button("Execute",icon="✨"):
#     if (medidaA+medidaB)> medidaC:
#         st.write(f"A soma do perímetro é: ", {calculo_perimetro})
#     elif (medidaA+medidaC) > medidaB:
#         st.write(f"A soma do perímetro é: ", {calculo_perimetro})
#     else:
#         st.write(f"Não é um triângulo")

if st.button("Execute"):
    if forma_triangulo:
        st.write(f"O valor da soma do perímetro: {calculo_perimetro}")
    #elif calculo_perimetro:
        #st.write(f"A soma do perímetro é: {calculo_perimetro}")
    elif area_trapezio:
        st.write(f"Área trapézio: {area_trapezio}")
