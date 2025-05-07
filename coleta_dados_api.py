import requests


def enviar_arquivo():
    # Caminho do arquivo para uploud
    caminho = 'C:/Users/kaiqu/Downloads/produtos_informatica.xlsx'

    # Enviar arquivo
    requisicao = requests.post('https://www.file.io/', files={'file': open(caminho, 'rb')})
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['link']
    print("Arquivo enviado. Link para acesso:", url)

    # def enviar_arquivo_chave():
    #     # Caminho do arquivo e chave de upload
    #     caminho = 'C:/Users/kaiqu/Downloads/produtos_informatica.xlsx'
    #     chave_acesso = 'BSGIUGU-FJHFDJ-FD'    # API KEY

    # Enviar arquivo
    requisicao = requests.post(
        'https://www.file.io/',
        files={'file': open(caminho, 'rb')},
        headers={'Authorization': chave_acesso}
    )
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['link']
    print("Arquivo enviado com chave. Link para acesso:", url)

    enviar_arquivo()
