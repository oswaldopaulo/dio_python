import requests

def retorna_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    if response.status_code==200:
        return response.json()
    else:
        return

if __name__ == '__main__':
    cep = retorna_cep(18209245)
    print(cep)