# integration_tests/helpers.py

import requests
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Função para enviar dados simulados para o backend via API (POST)
def send_test_data_to_backend(endpoint, data):
    """
    Envia dados de teste para o backend usando uma requisição POST.
    :param endpoint: O endpoint da API para o qual os dados serão enviados.
    :param data: O dicionário de dados a ser enviado no corpo da requisição.
    :return: A resposta da requisição.
    """
    try:
        response = requests.post(endpoint, json=data)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar dados para o backend: {e}")
        return None

# Função para verificar se um dado está sendo armazenado corretamente no banco de dados
def verify_data_in_database(query, expected_value, db_config):
    """
    Verifica se os dados foram armazenados corretamente no banco de dados.
    :param query: A consulta SQL para buscar os dados no banco.
    :param expected_value: O valor esperado a ser encontrado.
    :param db_config: Dicionário contendo as configurações do banco de dados.
    :return: True se os dados forem encontrados, caso contrário, False.
    """
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if result and expected_value in result:
            return True
        else:
            return False
    except mysql.connector.Error as err:
        print(f"Erro ao consultar o banco de dados: {err}")
        return False

# Função para obter dados exibidos na UI usando o Selenium
def get_data_from_ui_element(browser, element_id):
    """
    Obtém o texto exibido em um elemento da interface do usuário.
    :param browser: O objeto do Selenium WebDriver.
    :param element_id: O ID do elemento HTML a ser localizado.
    :return: O texto do elemento ou None se não encontrado.
    """
    try:
        element = browser.find_element(By.ID, element_id)
        return element.text
    except Exception as e:
        print(f"Erro ao obter dado do elemento {element_id}: {e}")
        return None

# Função para inicializar o navegador WebDriver
def init_browser(url):
    """
    Inicializa o WebDriver do Selenium e acessa a URL fornecida.
    :param url: A URL a ser acessada pela interface de testes.
    :return: O objeto WebDriver.
    """
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(2)  # Aguarda o carregamento da página
    return browser

# Função para verificar se a interface foi atualizada corretamente
def check_ui_update(browser, element_id, expected_value):
    """
    Verifica se um elemento da interface foi atualizado corretamente.
    :param browser: O objeto do Selenium WebDriver.
    :param element_id: O ID do elemento HTML a ser verificado.
    :param expected_value: O valor esperado do elemento.
    :return: True se o valor do elemento for o esperado, caso contrário, False.
    """
    actual_value = get_data_from_ui_element(browser, element_id)
    if actual_value == expected_value:
        return True
    else:
        print(f"Valor inesperado no elemento {element_id}: {actual_value}")
        return False
