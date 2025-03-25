# Cotacao-de-moedas
Cotacao de moedas US e BR


# Flask Currency Exchange Rates

Este é um projeto simples em Flask que obtém e exibe as cotações do dólar e euro em relação ao real.

## Tecnologias Utilizadas
- Python 3
- Flask
- Requests
- HTML/CSS (para renderização da página)

## Instalação
1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```sh
   pip install flask requests
   ```

## Como Executar
1. Execute o arquivo principal:
   ```sh
   python app.py
   ```
2. Acesse no navegador:
   ```
   http://127.0.0.1:5000/
   ```

## Estrutura do Projeto
```
seu-projeto/
│-- templates/
│   ├── index.html
│-- app.py
│-- README.md
│-- requirements.txt (opcional)
```

## Exemplo de Resposta
O projeto obtém dados da API [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas) e retorna algo como:
```json
{
  "dolar": 5.12,
  "euro": 5.50
}
```

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir um PR ou relatar problemas.




