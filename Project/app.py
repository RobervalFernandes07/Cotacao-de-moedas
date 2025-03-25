from flask import Flask, render_template
import requests

app = Flask(__name__)

def obter_cotacoes():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    try:
        response = requests.get(url)
        data = response.json()
        return {
            "dolar": round(float(data['USDBRL']['bid']), 2),
            "euro": round(float(data['EURBRL']['bid']), 2)
        }
    except Exception as e:
        print("Erro ao buscar cotações:", e)
        return {"dolar": "Erro", "euro": "Erro"}

@app.route("/")
def index():
    cotacoes = obter_cotacoes()
    return render_template("index.html", cotacoes=cotacoes)

if __name__ == "__main__":
    app.run(debug=True)



