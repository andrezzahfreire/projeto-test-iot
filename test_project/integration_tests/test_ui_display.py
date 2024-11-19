# integration_tests/test_ui_display.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest

# URL da aplicação web para teste
UI_URL = "http://localhost:3000"  # substitua pela URL correta da sua aplicação

@pytest.fixture(scope="module")
def browser():
    # Inicializa o navegador Chrome para testes
    driver = webdriver.Chrome()
    driver.get(UI_URL)
    yield driver
    driver.quit()

def test_ui_display_data(browser):
    """
    Testa se a interface exibe os dados recebidos do dispositivo IoT corretamente.
    """

    # Aguarda o carregamento da página
    time.sleep(2)  # Ajuste conforme necessário para aguardar o carregamento dos dados

    # Verifica se os elementos de dados estão presentes na interface
    try:
        # Localiza o elemento que exibe o ID do sensor e verifica se ele está correto
        sensor_id_element = browser.find_element(By.ID, "sensor_id_display")
        assert sensor_id_element.text == "sensor_01", "Erro: ID do sensor exibido incorretamente na UI."

        # Localiza o elemento de temperatura e verifica se o valor está correto
        temperature_element = browser.find_element(By.ID, "temperature_display")
        assert temperature_element.text == "25.3°C", "Erro: Temperatura exibida incorretamente na UI."

        # Localiza o elemento de umidade e verifica o valor exibido
        humidity_element = browser.find_element(By.ID, "humidity_display")
        assert humidity_element.text == "55%", "Erro: Umidade exibida incorretamente na UI."

    except Exception as e:
        pytest.fail(f"Erro ao verificar a interface do usuário: {e}")

    print("Teste de exibição de dados na UI passou com sucesso.")

def test_ui_display_updates(browser):
    """
    Testa se a interface é atualizada em tempo real com os dados mais recentes.
    """

    # Simula o envio de novos dados para o backend
    # Aqui você poderia ter um script para enviar novos dados de teste para a API do backend
    time.sleep(2)  # Ajuste para garantir que os dados tenham tempo de atualizar

    # Verifica se os dados na UI são atualizados
    try:
        # Verifica novamente a temperatura e umidade após atualização
        updated_temperature_element = browser.find_element(By.ID, "temperature_display")
        assert updated_temperature_element.text == "26.0°C", "Erro: A UI não exibiu a temperatura atualizada."

        updated_humidity_element = browser.find_element(By.ID, "humidity_display")
        assert updated_humidity_element.text == "60%", "Erro: A UI não exibiu a umidade atualizada."

    except Exception as e:
        pytest.fail(f"Erro ao verificar atualização da interface do usuário: {e}")

    print("Teste de atualização em tempo real da UI passou com sucesso.")
