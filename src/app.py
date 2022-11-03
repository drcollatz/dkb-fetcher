from flask import Flask, Response, request
from dkb import fetch_dkb
from errors import errors

app = Flask(__name__)
app.register_blueprint(errors)

@app.get('/')
def fetch_data_default():
    return fetch_data(30)

@app.get('/<int:days>')
def fetch_data(days):

    if request.authorization is None:
        return "Basic auth please!"
    if days == 0:
        return "More days please"

    dkb_data = fetch_dkb(request.authorization.username, request.authorization.password, days)
    return dkb_data

@app.get("/health")
def health():
    return Response("OK", status=200)