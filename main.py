ci = """
ENTREGA DE ASSISTENCIA TECNICA - CLIENTE
CLIENTE: ADRIEL CARVALHO 
DATA: 13/08
ENDEREÇO: AVENIDA EXEMPLO, 520 - CAMPINAS - SÃO PAULO
"""

def extrair_cliente(ci):
    linhas = ci.splitlines()
    for linha in linhas:
        if linha.startswith("CLIENTE:"):
            partes = linha.split(":")
            cliente = partes[1].strip()
            return cliente

def extrair_data(ci):
    linhas = ci.splitlines()
    for linha in linhas:
        if linha.startswith("DATA:"):
            partes = linha.split(":")
            data = partes[1].strip()
            return data

def extrair_endereco(ci):
    linhas = ci.splitlines()
    for linha in linhas:
        if linha.startswith("ENDEREÇO: "):
            partes = linha.split(":")
            endereco = partes[1].strip()
            return endereco

def extrair_tipo(ci):
    if "ENTREGA" in ci:
        return "ENTREGA"
    elif "RETIRADA" in ci:
        return "RETIRADA"