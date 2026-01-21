from codigo.bytebank import Funcionario
from pytest import mark, raises


class TestBytebank:
    # Teste criado com funcionalidade existente usando técnica Given-When-Then
    # @mark.skip
    def test_idade_com_data_nascimento_07_11_1999_precisa_retornar_26(self):
        entrada = "07/11/1999"
        esperado = 26
        # A lógica do método idade, não checa o dia do aniversário para saber se
        # já passou ou não, ela apenas checa o ano, por isso o método está dando
        # errado ("ainda tenho 26 anos")

        funcionario_teste = Funcionario("Teste", entrada, 1111)  # Given-Contexto

        resultado = funcionario_teste.idade()  # When-Ação

        assert resultado == esperado  # Then-Desfecho

    # Teste criado com funcionalidade existente usando técnica Given-When-Then
    def test_sobrenome_com_nome_lucas_cordeiro_precisa_retornar_cordeiro(self):
        entrada = "Lucas Cordeiro"
        esperado = "Cordeiro"

        lucas = Funcionario(entrada, "07/11/1999", 1111)  # Given-Contexto

        resultado = lucas.sobrenome()  # When-Ação

        assert resultado == esperado  # Then-Desfecho

    # Este teste foi criado sem existir a funcionalidade, assim ele falhou de
    # início A partir dele, implantamos a funcionalidade
    def test_decrescimo_salario_100000_deve_retornar_90000(self):
        salario_entrada = 100000
        nome_entrada = "Helena Vitória"
        esperado = 90000

        helena = Funcionario(nome_entrada, "12/10/1998", salario_entrada)

        resultado = helena.decrescimo_salario()

        assert resultado == esperado

    # Essa marcação com @mark.calcular_bonus serve para identificar os testes
    # mais facilmente entre todos os testes disponíveis dentro do Pytest
    # (principalmente na hora de rodar, as vezes não queremos rodar todos os
    # testes, mas sim apenas alguns)
    # Se quiser deixar mais explícito, podemos passar @pytest.mark.calcular_bonus
    @mark.calcular_bonus
    def test_calcular_bonus_recebe_10000_deve_retornar_1000(self):
        salario_entrada = 10000
        bonus_esperado = 1000

        ayanne = Funcionario("Ayanne Cordeiro", "21/06/1994", salario_entrada)

        bonus_calculado = ayanne.calcular_bonus()

        assert bonus_calculado == bonus_esperado

    @mark.calcular_bonus
    def test_calcular_bonus_recebe_15000_deve_retornar_exception(self):
        # with pytest.raises(Exception) -> já espera que a saída do teste
        # (assert) seja um Exception (não precisa igualar o assert no final com
        # um "bonus_esperado")
        with raises(Exception):
            salario_entrada = 15000

            ayanne = Funcionario("Ayanne Cordeiro", "21/06/1994", salario_entrada)

            bonus_calculado = ayanne.calcular_bonus()

            assert bonus_calculado
