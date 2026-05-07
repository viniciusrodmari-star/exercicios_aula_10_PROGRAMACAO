PRECO_INTEIRA = 140
PRECO_MEIA = PRECO_INTEIRA // 2
PRECO_ISENTO = 0

def definir_preco_ingresso(idade):
    if idade < 4:
        return PRECO_ISENTO
    
    elif idade <= 18 or idade >= 60: 
        return PRECO_MEIA
    
    elif idade < 60:
        return PRECO_INTEIRA
    
    