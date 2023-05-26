#Importações / Imports
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from time import sleep
import save

#Definir configurações da janela do Google Chrome / Define Google Chrome tab configurations
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ['enable-automation'])
navegador = webdriver.Chrome(ChromeDriverManager().install(), options=options)

#Acessar os resultados da Fase / Access Phase 2 results
navegador.get("https://olimpiadasbiologiasistema.butantan.gov.br/ResultadoFase2")

#Informação de Menção Honrosa / Honorable Mention information 
navegador.find_element(By.XPATH, '//*[@id="accordion2"]/div[5]/div[1]/h4/a').click()

#Listas auxiliares / Auxiliary Lists
linha = []
linha_aux = []

#Mover a página até que o elemento seja visível / Scroll page untill the element can be found
element = navegador.find_element(By.XPATH, '//*[@id="tabelaMencaoHonrosa_paginate"]/ul/li[7]/a')
navegador.execute_script("arguments[0].scrollIntoView(true);", element)
sleep(5)

while(True):

    #Em cada página, são mostrados dez alunos premiados / On each page, ten awarded students are shown
    for x in range(1, 11):

        #Para a última página, podem existir informações de menos de dez estudantes / On the last page, there may be information for less than ten students
        try: 

            #Para cada estudante, sete informações são disponibilizadas / For each student, seven pieces of information are available
            for i in range(1, 7):
                linha_aux.append(navegador.find_element(By.XPATH, '//*[@id="tabelaMencaoHonrosa"]/tbody/tr[' + str(x) + ']/td[' + str(i) + ']').text)

            linha.append(linha_aux)
            linha_aux = []

        except:
            break

    #Obter a classe do elemento que possibilita acessar a próxima página / Get the class of the element that enables access to the next page      
    condicao = (navegador.find_element(By.XPATH, '//*[@id="tabelaMencaoHonrosa_paginate"]/ul/li[7]').get_attribute('class'))

    #Se a classe do elemento mudar para 'next disabled', esta é uma última página / If the element class is changed to 'next disabled', this is the last page
    if (condicao == 'next disabled'):
        break

    else:
        element.click()

#Salvar o documento / Save the file
save.salvar(linha)