from flask import Flask
from flask import render_template
# from model_training import train
# from rent_predicting import predict_rent

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

app.run(host = '0.0.0.0', port = 5000)