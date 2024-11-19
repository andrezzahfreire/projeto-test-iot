# Projeto de Testes - IoT e Aplicação Web

Este projeto contém testes para verificar a comunicação entre dispositivos IoT (Arduino) e uma aplicação web, além de testar a funcionalidade do sensor, o armazenamento de dados e a interface do usuário (UI). Os testes são realizados utilizando o framework `pytest`.

## Objetivo

Verificar os seguintes aspectos da integração entre o dispositivo IoT e a aplicação web:

1. Comunicação entre o dispositivo IoT (Arduino) e o backend da aplicação.
2. Funcionamento correto do sensor e a resposta da lâmpada.
3. Armazenamento e integridade dos dados coletados pelo dispositivo IoT no banco de dados.
4. Visualização dos dados na interface web (frontend).

## Estrutura do Projeto

```plaintext
iot-web-testing/
│
├── tests/
│   ├── test_iot_backend_communication.py    # Testes para a comunicação entre IoT e o backend
│   ├── test_sensor_functionality.py         # Testes para verificar o funcionamento do sensor
│   ├── test_datastorage.py                  # Testes de coleta e armazenamento de dados
│   ├── test_ui_display.py                   # Testes para a interface do usuário (UI)
│   └── helpers.py                           # Funções auxiliares para os testes
│
├── mockdata.py                              # Dados mockados para os testes
├── requirements.txt                         # Dependências do projeto
└── README.md                                # Este arquivo
```

## Pré-requisitos

Antes de começar, você precisará ter o Python 3 instalado e configurar o ambiente com as dependências necessárias. 

### Instalação

1. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd iot-web-testing
   ```

2. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Para Linux/macOS
   venv\Scripts\activate      # Para Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Como Rodar os Testes

Após instalar as dependências, você pode executar os testes com o seguinte comando:

```bash
pytest
```

Isso irá rodar todos os testes localizados no diretório `tests/`. Para rodar um teste específico, use o comando:

```bash
pytest tests/test_iot_backend_communication.py
```

## Descrição dos Testes

### 1. Teste de Integração IoT - Backend

- **Objetivo**: Verificar se o dispositivo IoT (Arduino) se comunica corretamente com o backend da aplicação.
- **Procedimento**: Configura o dispositivo IoT para enviar dados de teste e verifica se o backend os recebe corretamente.

### 2. Teste de Funcionamento do Sensor

- **Objetivo**: Assegurar que o sensor detecta corretamente o ambiente e aciona a lâmpada como esperado.
- **Procedimento**: Simula condições de ativação do sensor e verifica se a lâmpada responde corretamente.

### 3. Teste de Coleta e Armazenamento de Dados

- **Objetivo**: Garantir que os dados coletados pelo dispositivo IoT são armazenados corretamente no banco de dados.
- **Procedimento**: Verifica se os dados são salvos corretamente no banco de dados e se podem ser consultados sem inconsistências.

### 4. Teste de Interface do Usuário (UI)

- **Objetivo**: Verificar a visualização correta dos dados coletados na interface web.
- **Procedimento**: Testa a exibição dos dados, incluindo a atualização em tempo real e responsividade da interface em diferentes dispositivos.

## Contribuições

Se você deseja contribuir para o projeto, fique à vontade para enviar um Pull Request. Antes de contribuir, verifique se os testes estão passando e siga o estilo de codificação do projeto.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais informações.
