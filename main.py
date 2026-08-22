ci = """
ENTREGA DE ASSISTENCIA TECNICA - CLIENTE
CLIENTE: ADRIEL CARVALHO 
DATA: 13/08
ENDEREÇO: AVENIDA EXEMPLO, 520 - Guarujá - SÃO PAULO
"""
ci2 = """
RETIRADA DE SOBRAS E LIXO - CLIENTE BEATRIZ ALEXANDRE
CLIENTE: BEATRIZ ALEXANDRE
DATA: 22/08
ENDEREÇO: AVENIDA SANTO AMARO, 600 - Morumbi - SÃO PAULO
"""

ci3 = """
ENTREGA DE ASSISTENCIA TECNICA - CIENTE DAVI CARVALHO
cliente: DAVI CARVALHO
DATA: 25/08
ENDEREÇO: RUA CONCÓRDIA, 285 - ITAPECERICA DA SERRA - SÃO PAULO
"""

ci_quebrada = """
ENTREGA DE ASSISTENCIA TECNICA
CLIENTE: FULANO DE TAL
DATA: 20/08
"""

cis = [ ci , ci2, ci3 ]

def extrair_cliente(ci):
    linhas = ci.splitlines()
    for linha in linhas:
        if linha.upper().startswith("CLIENTE:"):
            partes = linha.split(":")
            cliente = partes[1].strip()
            return cliente
    return "Cliente não informado - verificar a C.I"

def extrair_data(ci):
    linhas = ci.splitlines()
    for linha in linhas:
        if linha.upper().startswith("DATA:"):
            partes = linha.split(":")
            data = partes[1].strip()
            return data
    return "Data não informada - verificar a C.I"

def extrair_endereco(ci):
    linhas = ci.splitlines()
    for linha in linhas:
        if linha.upper().startswith("ENDEREÇO: "):
            partes = linha.split(":")
            endereco = partes[1].strip()
            return endereco
    return "Endereço não informado"    

def extrair_tipo(ci):
    if "ENTREGA" in ci.upper():
        return "ENTREGA"
    elif "RETIRADA" in ci.upper():
        return "RETIRADA"
    else:
        return "Tipo de Serviço não informado - verificar a C.I"

def extrair_bairro(ci):
    endereco = extrair_endereco(ci)
    partes = endereco.split("-")
    if len(partes) >= 2:
        bairro = partes[1].strip()
        return bairro
    return "Endereço não informado - verificar a C.I"

def is_viagem(ci):
    locais_viagem = ["CAMPINAS", "PORTO FELIZ", "CARAGUATATUBA", "RIVIERA", "GUARUJÁ"]
    bairro = extrair_bairro(ci)
    for local in locais_viagem:
        if local in bairro.upper():
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

resultado = []
for ci_atual in cis:
    dados = processar_ci(ci_atual)
    resultado.append(dados)

for item in resultado:
    print("Cliente:", item["cliente"])
    print("Tipo:", item["tipo"])
    print("Data:", item["data"])
    print("Bairro:", item["bairro"])
    print("Viagem:", item["viagem"])
    print("------------------")

print(extrair_bairro(ci_quebrada))