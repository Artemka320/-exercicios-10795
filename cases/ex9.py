def processamento_requisicao():
    req = {"metodo": "POST", "conteudo": ""}
    
    match req:
        case {"metodo": "GET"}:
            print("Requisição GET recebida")
        case {"metodo": "POST", "conteudo": conteudo} if conteudo:
            print("Requisição POST com dados válidos")
        case {"metodo": "POST", "conteudo": ""} | {"metodo": "POST", "conteudo": None}:
            print("Requisição POST sem dados")
        case _:
            print("Método não suportado")