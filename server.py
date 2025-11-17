from flask import Flask
from flask import render_template, request
from model_training import train
from rent_predicting import predict_rent

app = Flask(__name__)
# model = train()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("Recebido um pedido POST")
        data = request.get_json()
        features = data.values()
        print("Features: ", features)
        # print("------------------")
        # predicted_rent = predict_rent(features, model)
        # return {f"<h1> predicted_rent: {predicted_rent}</h1>"}
    else:
        return render_template('index.html')



app.run(host = '0.0.0.0', port = 5000)