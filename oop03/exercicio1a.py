class Pessoa:
    #Atributos
    nome:str
    idade:int

#Contrutor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
#Metodos
    def maior_idade(self, idade):
        if self.idade > idade:
            return self.idade
        elif self.idade < idade:
            return idade
        else:
            return "A idade das duas pessoas são iguais"
        
    def p_maior_idade(self, idade, nome):
        if self.idade > idade:
            return self.nome
        elif self.idade < idade:
            return nome
        else:
            return "...."
    
    def saida(self):
        return f'''
Dados das pessoas:
\tNome da 1° Pessoa: {self. nome}
\tNome da 2° Pessoa: {self. nome}
\tIdade da 1° Pessoa: {self. idade} anos.
\tIdade da 1° Pessoa: {self. idade} anos.
\tPessoa com maior idade: {self. p_maior_idade()} anos com {self.maior_idade()}.
'''