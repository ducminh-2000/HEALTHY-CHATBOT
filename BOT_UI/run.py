import warnings
warnings.filterwarnings('ignore')


from flask import Flask, render_template, request
from flask import jsonify
from flask_wtf.csrf import CSRFProtect

import sys
import os
sys.path.append("/home/haind/Documents/VFAST/healthy_chatbot")

from test_load_model import evaluateInput


app = Flask(__name__,static_url_path="/static")
csrf = CSRFProtect(app)
csrf.init_app(app)

@csrf.exempt
@app.route('/test', methods=['POST'])
def reply():
	json1 = request.json
	text = json1['msg']
	print(text)
	output = evaluateInput(text)
	return jsonify(text=output)


@app.route("/")
def index():
    return render_template("index.html")

if (__name__ == "__main__"):
    app.run(port = 5000,debug=True)
