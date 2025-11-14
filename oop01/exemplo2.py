import produtoOOP as p #Importar o módulo

p1 = p.Produto() #Intanciar o objeto

#Entrada de dados
print("Digite os dados do produto")
p1.nome = input("\tNome: ")
p1.preco = float(input("\tPreco: "))
p1.saldo = int(input("\tQuantidade: "))
#Saida de dados 1
print("Dados do produto")
print(f"\tNome do produto: {p1.nome}")
print(f"\tValor de compra: {p1.preco}")
print(f"\tQuantidade em estoque: {p1.saldo}")
print(f"\tValor total em estoque: {p1.valorTotalEmEstoque():.2f}")
