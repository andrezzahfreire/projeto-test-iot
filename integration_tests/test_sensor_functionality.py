# integration_tests/test_sensor_functionality.py

import pytest
import serial
import time

# Configurações da porta serial para conectar ao dispositivo IoT (Arduino)
SERIAL_PORT = "COM3"  # substitua pelo nome da porta usada no dispositivo
BAUD_RATE = 9600      # a taxa de comunicação deve coincidir com a do código Arduino

def test_sensor_functionality():
    """
    Testa se o sensor detecta o ambiente e aciona a lâmpada conforme esperado.
    """

    # Conecta ao monitor serial do dispositivo
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
    time.sleep(2)  # Tempo para garantir a conexão com o Arduino

    try:
        # Simula uma condição de ativação do sensor
        ser.write(b"SIMULATE_MOTION\n")  # Envia um comando ao Arduino para simular a detecção de movimento
        
        # Lê a resposta do dispositivo
        output = ser.readline().decode().strip()

        # Verifica se a lâmpada acende em resposta ao sensor
        assert output == "LAMP_ON", "Erro: A lâmpada não acendeu após a detecção do sensor."

        # Simula a condição de desativação
        ser.write(b"SIMULATE_NO_MOTION\n")
        output = ser.readline().decode().strip()

        # Verifica se a lâmpada apaga quando não há mais movimento
        assert output == "LAMP_OFF", "Erro: A lâmpada não apagou após a ausência de detecção do sensor."

    finally:
        ser.close()

    print("Teste de funcionalidade do sensor passou com sucesso.")
