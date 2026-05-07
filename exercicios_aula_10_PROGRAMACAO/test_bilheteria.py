from bilheteria import definir_preco_ingresso, PRECO_INTEIRA, PRECO_MEIA, PRECO_ISENTO

def test_ingresso_infantil():
    for i in range(0,4):
        assert definir_preco_ingresso(i) == PRECO_ISENTO

def test_ingresso_jovem():
    for i in range(4,19):
        assert definir_preco_ingresso(i) == PRECO_MEIA

def test_ingresso_idoso():
    for i in range(60,120):
        assert definir_preco_ingresso(i) == PRECO_MEIA

def test_ingresso_adulto():
    for i in range(19,60):
        assert definir_preco_ingresso (i) == PRECO_INTEIRA
        