from flask import Flask, request, jsonify
from src.classes.service import Service

app = Flask(__name__)
srv = Service()

@app.route("/", methods=['GET'])
def main():
    return srv.template()

@app.route("/", methods=['POST'])
def message():
	return srv.message()

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)