import streamlit as st
#from streamlit import header,write,text_input,button,warning,success,error
#from math import sqrt,pow
#Função python
def calculo(delta):
    valor = (mt.sqrt(delta))/(2*a)
    return valor
import math as mt
st.header("Calculadora de Bhaskara")
st.write("Calculadora de raízes \n de uma equação de segundo grau")
st.write("ax²+bx+c=0")
#Entrada de dados
a=st.text_input("Digite o valor de a:")
b=st.text_input("Digite o valor de b:")
c=st.text_input("Digite o valor de c:")
#Processamento de dados
if st.button("Calcular raízes"):
   try:
    a=float(a)#Convertendo string para float
    b=float(b)
    c=float(c)
    delta=mt.pow(b,2)-4*a*c
    if delta<0:
      st.warning("A equação não possui raízes reais.")
    elif delta == 0:
       raiz=(-b+mt.sqrt(delta))/(2*a)
       st.success(f"A equação possui uma raiz real: {raiz}")
    else:
      raiz1=(-b+calculo(delta))
      raiz2=(-b+mt.sqrt(delta))/(2*a)
      st.success(f"As raízes da equação são: \n Raiz 1: {raiz1} \n Raiz 2: {raiz2}" )
   except ValueError:
    st.error("Por favor insira valores válidos")
    st.write("O valor de delta é: ", delta)
   except ZeroDivisionError:
     st.error("O valor de 'a' não pode ser zero em uma equação de segundo grau.")
