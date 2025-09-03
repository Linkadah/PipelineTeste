from calculadora import soma, subtrair, multiplicar, dividir

#TESTES Soma
def test_um_soma():
    assert soma(3,4) == 7

def test_dois_soma():
    assert soma(4,4) == 8

def test_teis_soma():
    assert soma(5,4) == 9

# TESTES Subtração
def test_um_subtrair():
    assert subtrair(4,3) == 1

def test_dois_subtrair():
    assert subtrair(4,3) == 1

def test_treis_subtrair():
    assert subtrair(4,3) == 1

# TESTES Multiplicação
def test_um_mult():
    assert multiplicar(1,2) == 2

def test_dois_mult():
    assert multiplicar(1,3) == 3

def test_treis_mult():
    assert multiplicar(1,4) == 4

# TESTES Divisão
def test_um_div():
    assert dividir(10,2) == 5

def test_dois_div():
    assert dividir(4,2) == 2

def test_treis_div():
    assert dividir(40,4) == 10