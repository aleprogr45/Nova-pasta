import streamlit as st
def celsius_fahrenheit(t):
    return (t*1.8)+32
def celsius_kelvin(t):
    return temp+275.15
def fahrenheit_celsius(t):
    return (t-32)*1.8
def fahrenheit_kelvin(t):
    return fahrenheit_celsius(t)+275.15
def kelvin_celsius(t):
    return t-273.15
def kelvin_fahrenheit(t):
    return celsius_fahrenheit(t)*kelvin_celsius(t)
#Problema temperatura
st.sidebar.title("Conversor de temperatura")
st.title("Conversos de temperatura")
st.sidebar.markdown("Converte a temperatura em Celsius, fahrenheit e Kelvin")
#celsius_selecionado=st.sidebar.checkbox("Celsius",key="temp_celsius")
#fahrenheit_selecionado=st.sidebar.checkbox("Fahrenheit",key="temp_fahrenheit")
#kelvin_selecionado=st.sidebar.checkbox("Kelvin",key="temp_kelvin")
#Entrada de dados
temp=st.number_input("Valor da temperatura",format="%.2f",step=1.0)


#Processamento de dados
if st.button("Converter",icon="✨"):
    if celsius_selecionado:
        st.write(f"{temp}°C em Fahrenheit: {celsius_fahrenheit(temp):.2f}°F")
        st.write(f"{temp}°C em Kelvin:{celsius_kelvin(temp):.2f}K")
    elif fahrenheit_selecionado:
        st.write(f"{temp}°F em Celsius: {fahrenheit_celsius(temp):.2f}°C")
        st.write(f"{temp}°F em Kelvin: {fahrenheit_kelvin(temp):.2f}K")
    elif kelvin_selecionado:
        st.write(f"{temp}K em Celsius: {kelvin_celsius(temp):.2f}°C")
        st.write(f"{temp}K em Fahrenheit: {kelvin_fahrenheit(temp):.2f}°F")