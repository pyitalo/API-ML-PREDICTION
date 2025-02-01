# 📊 API de Predição de Preços com FastAPI e Machine Learning

Esta API permite prever o preço de imóveis com base na área em metros quadrados, utilizando um modelo de **Regressão Linear** treinado com dados fictícios. Desenvolvido com  **FastAPI** , a API suporta predições individuais e em lote.

## 🚀 Tecnologias Utilizadas

* **Python 3.12**
* **FastAPI** (Framework para APIs)
* **Scikit-learn** (Modelo de Machine Learning)
* **Pandas** (Manipulação de dados)

## 📥 Instalação e Execução

1. **Clone este repositório** :

```bash
   git clone https://github.com/seu-usuario/api-ml.git
   cd api-ml
```

1. **Crie um ambiente virtual (opcional, mas recomendado)** :

```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
```

1. **Instale as dependências** :

```bash
   pip install -r requirements.txt
```

1. **Execute a API** :

```bash
   uvicorn main:app --reload
```

1. **Acesse a documentação interativa** no navegador:
   * [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  *(Swagger UI)*
   * [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) *(Redoc)*

---

## 🌍 Endpoints Disponíveis

### 1️⃣ **Rota Principal**

**`GET /`**

* Exibe uma mensagem de boas-vindas e informações sobre a API.

### 2️⃣ **Obter Dados de Treinamento**

**`GET /Value_Ml`**

* Retorna os dados utilizados para treinar o modelo de Machine Learning.

### 3️⃣ **Predição de Preço (Individual)**

**`POST /prediction/`**

* Recebe um valor de **área** e retorna a predição de preço correspondente.

📌 **Exemplo de Entrada:**

```json
{
  "area": 3000
}
```

📌 **Exemplo de Resposta:**

```json
{
  "area": 3000,
  "preço_predito": 565000.0
}
```

### 4️⃣ **Predição de Preço (Em Lote)**

**`POST /prediction_batch/`**

* Recebe uma **lista** de valores de área e retorna as previsões correspondentes.

📌 **Exemplo de Entrada:**

```json
{
  "areas": [2500, 2700, 3100, 4000]
}
```

📌 **Exemplo de Resposta:**

```json
{
  "previsões": [
    {"area": 2500, "preço_predito": 540000.0},
    {"area": 2700, "preço_predito": 560000.0},
    {"area": 3100, "preço_predito": 600000.0},
    {"area": 4000, "preço_predito": 725000.0}
  ]
}
```

---

## 📌 Melhorias Futuras

* 📈 Permitir upload de arquivos CSV com dados para predição em lote.
* 🏠 Adicionar mais variáveis ao modelo para aumentar a precisão.
* ☁️ Deploy da API na AWS Lambda ou no Google Cloud.

---

## 📜 Licença

Este projeto é de **uso livre** para aprendizado e portfólio! Sinta-se à vontade para contribuir. 🚀
