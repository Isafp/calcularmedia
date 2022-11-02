import streamlit as st

st.title("Simple Calculator")
#coletando dados

n1 = int(input("Número 1:" ))
n2 = int(input("Número 2:" ))
n3 = int(input("Número 3:" ))
n4 = int(input("Número 4:" ))
n5 = int(input("Número 5:" ))

#calculando a média
media = (n1 + n2 + n3 + n4 + n5)/(5)

#exibindo o resultado
print("Média= " + str(media))
