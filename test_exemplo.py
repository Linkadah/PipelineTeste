from exemplo import funcao_carregar_aquivo, funcao_ler_aquivo

def test_carregar_aquivo():
    assert funcao_carregar_aquivo() == "Arquivo carregado!!!"
    
def test_ler_aquivo():
    assert funcao_ler_aquivo() == "Leitura realizada!!!"