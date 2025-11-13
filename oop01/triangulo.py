#Problema triangulo sem oop
#Entrada de dados
#TRIANGULO X
print("Inserir as medidas do triângulo X")
ax=int(input("Digite a medida a:"))
bx=int(input("Digite a medida b:"))
cx=int(input("Digite a medida c:"))
#TRIANGULO Y
print("Inserir as medidas do triângulo Y")
ay=int(input("Digite a medida a:"))
by=int(input("Digite a medida b:"))
cy=int(input("Digite a medida c:"))
#Processamento de dados
p = (ax+bx+cx)/2
areax = (p*(p-ax)*(p-bx)*(p-cx))**0.5
p = (ay + by + cy)/2
areay = (p*(p-ay)*(p-by)*(p-cy))**0.5
#Condicional para verificar qual triângulo é maior
if areax > areay:
    saida = "A área do triângulo X é maior que a área do triângulo Y"
elif areay > areax:
    saida = "A área do triângulo Y é maior do que o triângulo X"
else:
    saida = "As áreas dos triângulo são iguais"
#Saída de dados
print(f"A área do triângulo X = {areax:.1f}")
print(f"A área do triângulo Y = {areay:.1f}")
print(saida)