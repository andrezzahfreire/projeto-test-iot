# integration_tests/mockdata.py

# Dados simulados para os testes de comunicação com o backend
def get_mock_sensor_data():
    """
    Retorna dados simulados de um sensor IoT.
    :return: Dicionário com dados simulados do sensor.
    """
    return {
        "sensor_id": "sensor_01",
        "temperature": 25.3,
        "humidity": 55,
        "timestamp": "2024-11-14T12:30:00Z"
    }

def get_mock_sensor_data_list():
    """
    Retorna uma lista de dados simulados de múltiplos sensores IoT.
    :return: Lista com dicionários de dados simulados dos sensores.
    """
    return [
        {"sensor_id": "sensor_01", "temperature": 25.3, "humidity": 55, "timestamp": "2024-11-14T12:30:00Z"},
        {"sensor_id": "sensor_02", "temperature": 22.1, "humidity": 60, "timestamp": "2024-11-14T12:45:00Z"},
        {"sensor_id": "sensor_03", "temperature": 24.5, "humidity": 58, "timestamp": "2024-11-14T13:00:00Z"}
    ]

# Dados simulados para os testes de banco de dados
def get_mock_db_data():
    """
    Retorna dados simulados que poderiam ser extraídos de um banco de dados.
    :return: Lista de dicionários com dados simulados de sensor.
    """
    return [
        {"sensor_id": "sensor_01", "temperature": 25.3, "humidity": 55, "timestamp": "2024-11-14T12:30:00Z"},
        {"sensor_id": "sensor_02", "temperature": 22.1, "humidity": 60, "timestamp": "2024-11-14T12:45:00Z"}
    ]

# Dados simulados para os testes de interface do usuário
def get_mock_ui_data():
    """
    Retorna dados simulados que podem ser exibidos na interface do usuário.
    :return: Dicionário com dados simulados para a interface do usuário.
    """
    return {
        "sensor_id": "sensor_01",
        "temperature": 25.3,
        "humidity": 55,
        "status": "Active"
    }

# Função para gerar dados simulados de dispositivos IoT
def generate_mock_iot_data(sensor_id, temperature, humidity):
    """
    Gera dados simulados para um sensor específico.
    :param sensor_id: O ID do sensor.
    :param temperature: Temperatura simulada.
    :param humidity: Umidade simulada.
    :return: Dicionário com os dados simulados do sensor.
    """
    return {
        "sensor_id": sensor_id,
        "temperature": temperature,
        "humidity": humidity,
        "timestamp": "2024-11-14T12:30:00Z"
    }
