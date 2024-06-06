import json

import requests

URL = "https://restcountries.com/v2/all"

def requisicao(url):
    try:
        resposta_da_requisicao = requests.get(url)
        if resposta_da_requisicao.status_code == 200:
            return resposta_da_requisicao.text
    except:
        print("Erro ao fazer a requisição!")

def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta)
    except:
        print("Erro ao fazer o parsing!")

def exibir_paises_carregados(lista_de_paises):
    print(f"Quantidade de países carregados: {len(lista_de_paises)}\n")
    for indice, pais in enumerate(lista_de_paises, 1):
        print(f"País {indice}: {pais['name']}")

def pesquisar_pais(lista_de_paises):
    pais_pesquisado = input("\nDigite o nome do país desejado: ")
    verificador = False
    for pais in lista_de_paises:
        if pais_pesquisado == pais["name"]:
            print(f"Região: {pais['region']}")
            print(f"Capital: {pais['capital']}")
            print(f"Moeda: {pais['currencies'][0]['name']}")
            print(f"População {pais['population']}")
            verificador = True
    if verificador == False:
        print("País inexistente!")

if __name__ == "__main__":
    conteudo_da_resposta_da_requisicao = requisicao(URL)
    if conteudo_da_resposta_da_requisicao:
        lista_de_paises = parsing(conteudo_da_resposta_da_requisicao)
        if lista_de_paises:
            print("Carregamento concluído!\n")
            exibir_paises_carregados(lista_de_paises)
            pesquisar_pais(lista_de_paises)
