import os
from flask import Flask, render_template, request

app = Flask(__name__)

https://www.eais.go.kr/moct/awp/aia01/AWPAIA01L01

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)