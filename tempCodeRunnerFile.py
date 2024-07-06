''' 1 - Entrar na planilha e extrair o CPF do cliente
2 - Entrar no site https://consultcpf-devaprender.netlify.app/
o CPF da planilha para pesquisar o status do pagamento daquele cliente

3 - Verificar se está 'em dia' ou 'atrasado'
4- Se estiver 'em dia', pegar a data do pagamento e o metodo de pagamento
5 - Caso contrario (se estiver atrasado), colocar o status como pendente
6 - Inserir essas novas informaçoes(nome, valor, cpf, vencimento, status e caso enteja 'em dia', data do pagamento, metodo de pagamento(cartao, boleto) em uma nova planilha
7 - Repetir até chegar no ultimo cliente'''

import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Abrir a planilha e extrair o CPF
planilha_clientes = openpyxl.load_workbook('dados_clientes.xlsx')

# Selecionar a aba com os dados dos clientes
pagina_clientes = ['Sheet1']

# Iterar sobre os clientes
for linha in pagina_clientes.iter_rows(min_row=2, values_only=True):
    nome, valor, cpf, vencimento = linha
    
    # Entrar na página do site para pesquisar o status do pagamento
    driver = webdriver.Chrome()
    driver.get('https://consultcpf-devaprender.netlify.app/')
    sleep(5)


    