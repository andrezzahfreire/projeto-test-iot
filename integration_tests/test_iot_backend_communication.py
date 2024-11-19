# integration_tests/test_iot_backend_communication.py

import requests
import time

# URL do endpoint do backend que o dispositivo IoT deve enviar dados
BACKEND_URL = "http://localhost:5000/api/iot_data"  

def test_iot_backend_communication():
    """
    Testa se o backend recebe os dados enviados pelo dispositivo IoT.
    """
    
    # Dados de exemplo que o dispositivo IoT enviaria
    test_data = {
        "sensor_id": "sensor_01",
        "temperature": 22.5,
        "humidity": 60,
        "timestamp": "2024-01-01T12:00:00"
    }

    # Envia os dados simulados para o backend
    response = requests.post(BACKEND_URL, json=test_data)

    # Verifica se o backend respondeu com sucesso (HTTP status 200)
    assert response.status_code == 200, f"Erro: resposta do backend foi {response.status_code}"
    
    # Verifica o conteúdo da resposta para garantir que o backend recebeu e processou os dados corretamente
    response_json = response.json()
    assert response_json.get("status") == "success", "Erro: Backend não confirmou o recebimento com sucesso"
    assert response_json.get("received_data") == test_data, "Erro: Os dados recebidos não coincidem com os enviados"

    # Aguarda um breve intervalo para verificar a consistência da conexão e evitar falsos positivos em casos de delay
    time.sleep(1)

    print("Teste de comunicação IoT-Backend passou com sucesso.")

