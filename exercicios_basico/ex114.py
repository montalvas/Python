import requests

try:
    response = requests.get('http://pudim.com.br/')
except:
    print('\033[31mO site pudim está inacessível\033[m')
else:
    print('\033[34mConsegui acessar o site pudim com sucesso!\033[m')