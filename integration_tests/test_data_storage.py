# integration_tests/test_data_storage.py

import requests
import pymysql  # ou psycopg2 para PostgreSQL, dependendo do banco de dados utilizado
import pytest
import time

# URL do endpoint do backend que recebe os dados do dispositivo IoT
BACKEND_URL = "http://localhost:5000/api/iot_data"

# Configuração para conectar ao banco de dados
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "iot_database",
}

def test_data_storage():
    """
    Testa se o backend armazena corretamente os dados recebidos no banco de dados.
    """

    # Dados de exemplo que o dispositivo IoT enviaria
    test_data = {
        "sensor_id": "sensor_01",
        "temperature": 25.3,
        "humidity": 55,
        "timestamp": "2024-01-01T12:30:00"
    }

    # Envia os dados simulados para o backend
    response = requests.post(BACKEND_URL, json=test_data)

    # Verifica se o backend respondeu com sucesso (HTTP status 200)
    assert response.status_code == 200, f"Erro: resposta do backend foi {response.status_code}"

    # Aguarda um breve intervalo para garantir que os dados tenham sido processados e armazenados
    time.sleep(1)

    # Conecta ao banco de dados para verificar os dados armazenados
    connection = pymysql.connect(**DB_CONFIG)
    try:
        with connection.cursor() as cursor:
            # Query para verificar o último dado inserido pelo sensor
            query = """
            SELECT sensor_id, temperature, humidity, timestamp
            FROM sensor_data
            ORDER BY timestamp DESC
            LIMIT 1;
            """
            cursor.execute(query)
            result = cursor.fetchone()

            # Verifica se os dados armazenados correspondem aos dados enviados
            assert result is not None, "Erro: Nenhum dado encontrado no banco de dados."
            assert result[0] == test_data["sensor_id"], "Erro: sensor_id incorreto no banco de dados."
            assert result[1] == test_data["temperature"], "Erro: temperatura incorreta no banco de dados."
            assert result[2] == test_data["humidity"], "Erro: umidade incorreta no banco de dados."
            assert result[3] == test_data["timestamp"], "Erro: timestamp incorreto no banco de dados."

    finally:
        connection.close()

    print("Teste de armazenamento de dados passou com sucesso.")
