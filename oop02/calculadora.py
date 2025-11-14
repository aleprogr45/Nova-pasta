class calculadora1:
    #Atributo da classe
    PI = 3.14

    #Métodos estáticos da classe
    @staticmethod
    def circunferencia(raio) -> float:
        return 2 * calculadora1.PI * raio
    @staticmethod    
    def area(raio) -> float:
        return calculadora1.PI * raio **2