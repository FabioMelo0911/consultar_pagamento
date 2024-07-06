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
from time import sleep


# Abrir a planilha e extrair os dados
planilha_clientes = openpyxl.load_workbook('dados_clientes.xlsx')
pagina_clientes = planilha_clientes['Sheet1']

# Criar uma nova planilha para salvar os resultados
nova_planilha = openpyxl.Workbook()
pagina_resultados = nova_planilha.active
pagina_resultados.title = 'Resultados'
pagina_resultados.append(['Nome', 'Valor', 'CPF', 'Vencimento', 'Status', 'Data de Pagamento', 'Método de Pagamento'])
# Entrar na página do site para pesquisar o status do pagamento
driver = webdriver.Chrome()
driver.get('https://consultcpf-devaprender.netlify.app/')
# Iterar sobre os clientes
for linha in pagina_clientes.iter_rows(min_row=2, values_only=True):
    nome, valor, cpf, vencimento = linha
    sleep(5)  # Esperar a página carregar completamente
    
    # Pesquisar o CPF
    campo_pesquisa = driver.find_element(By.XPATH, '//input[@id="cpfInput"]')
    sleep(1)
    campo_pesquisa.send_keys(cpf)
    sleep(1)
    
    # Clicar no botão de pesquisar
    botao_pesquisar = driver.find_element(By.XPATH,'//button[@class="btn btn-custom btn-lg btn-block mt-3"]')
    sleep(1)
    botao_pesquisar.click()
    sleep(5)  # Esperar a página carregar completamente
    
    # Verificar se está 'em dia' ou 'atrasado'
    status = driver.find_element(By.XPATH,'//span[@id="statusLabel"]')
    if status.text == 'Em dia':
        data_pagamento = driver.find_element(By.XPATH,'//p[@id="paymentDate"]')
        metodo_pagamento = driver.find_element(By.XPATH,'//p[@id="paymentMethod"]')
        pagina_fechamento.append([nome, valor, cpf, vencimento, 'em dia', 'xxx','xxx' ])    
    else:
        # Inserir essas novas informaçoes na nova planilha
        planilha_fechamento = openpyxl.load_workbook('planilha fechamento.xlsx')
        pagina_fechamento = planilha_fechamento['Sheet1']

        pagina_fechamento.append([nome, valor, cpf, vencimento, 'pendente'])
