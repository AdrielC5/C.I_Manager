ci = """
ENTREGA DE ASSISTENCIA TECNICA - CLIENTE
CLIENTE: ADRIEL CARVALHO 
DATA: 13/08
ENDEREÇO: AVENIDA EXEMPLO, 520 - GUARUJÁ - SÃO PAULO
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

def extrair_bairro(ci):
    endereco = extrair_endereco(ci)
    partes = endereco.split("-")
    bairro = partes[1].strip()
    return bairro

def is_viagem(ci):
    locais_viagem = ["CAMPINAS", "PORTO FELIZ", "CARAGUATATUBA", "RIVIERA", "GUARUJÁ"]
    bairro = extrair_bairro(ci)
    for local in locais_viagem:
        if local in bairro:
            return True
    return False

def processar_ci(ci):
    dados = {
        "cliente": extrair_cliente(ci),
        "tipo": extrair_tipo(ci),
        "data": extrair_data(ci),
        "endereco": extrair_endereco(ci),
        "bairro": extrair_bairro(ci),
        "viagem": is_viagem(ci)
    }
    return dados

resultado = processar_ci(ci)
print(resultado)