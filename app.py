from sklearn.linear_model import LinearRegression
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Dados de treino
modelo = LinearRegression()
data = pd.DataFrame({
    'area': [2600, 3000, 3200, 3600, 4000],
    'price': [550000, 565000, 610000, 680000, 725000]
})
modelo.fit(data[['area']], data.price)


class AreaInput(BaseModel):
    area: float


class AreaListInput(BaseModel):
    areas: List[float]  # Lista de áreas para predição em lote


@app.get("/")
def root():
    """
    Bem-vindo à API de Predição de Preços!

    Rotas disponíveis:
    - `/Value_Ml` : Mostra os dados utilizados para o treinamento da regressão linear.
    - `/prediction/` : Recebe um valor de área (float) e retorna a previsão de preço.
    - `/prediction_batch/` : Recebe uma lista de áreas e retorna as previsões para todas.
    """
    return {'mensagem': 'Bem-vindo à minha API para predição de preços com Machine Learning!'}


@app.get("/Value_Ml")
def value():
    return {"dados utilizados para treino": data.to_dict(orient='records')}


@app.post("/prediction/")
def predict(area: AreaInput):
    try:
        predicted = modelo.predict([[area.area]])[0]
    except Exception as erro:
        return {"erro": str(erro)}
    else:
        return {'area': area.area, 'preço_predito': round(predicted, 2)}


@app.post("/prediction_batch/")
def predict_batch(areas: AreaListInput):
    """
    Permite que o usuário envie uma lista de áreas para previsão em lote.
    Exemplo de JSON esperado:
    {
        "areas": [2500, 2700, 3100, 4000]
    }
    """
    try:
        predictions = modelo.predict([[a] for a in areas.areas])
        result = [{"area": areas.areas[i], "preço_predito": round(predictions[i], 2)} for i in range(len(areas.areas))]
    except Exception as erro:
        return {"erro": str(erro)}
    else:
        return {"previsões": result}
