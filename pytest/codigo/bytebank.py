from datetime import date


class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nasciemnto_quebrada = self._data_nascimento.split("/")
        ano_nascimento = data_nasciemnto_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        sobrenome = self.nome.strip().split(" ")
        return sobrenome[-1]

    # Criado junto com o método abaixo na metodologia TDD
    def checar_se_e_socio(self):
        sobrenomes = ["Vitória", "Silva", "Almeida", "Santos", "Rocha"]
        return self.salario >= 100000 and self.sobrenome() in sobrenomes

    # Criado depois de criar o teste do Bytebank através da metodologia TDD (Test-Driven Development)
    def decrescimo_salario(self):
        if self.checar_se_e_socio():
            decrescimo = self._salario * 0.1
            self._salario -= decrescimo
            return self._salario

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise ("O salário é alto demais para receber um bônus.")
        return valor

    def __str__(self):
        return f"Funcionario({self._nome}, {self._data_nascimento}, {self._salario})"
