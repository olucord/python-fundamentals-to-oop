from codigo.bytebank import Funcionario


def main():
    lucas = Funcionario("Lucas Cordeiro", "07/11/1999", 10000)
    print(f"Sobrenome = {lucas.sobrenome()}")
    if lucas.calcular_bonus() > 0:
        print(f"Você tem um bônus de {lucas.calcular_bonus()}")
        print(f"Seu salário é de {lucas.salario}")
        print(f"No total você receberá {lucas.salario + lucas.calcular_bonus()}")
    else:
        print(f"Seu salário é de {lucas.salario}")
        print("Você não tem um bônus, pois seu salário ultrapassa R$ 10.000")


main()
