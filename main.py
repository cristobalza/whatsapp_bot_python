from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route("/")
def hola():
    return "Hola, Mundo!"

if __name__ == "__main__":
    app.run(debug=True)
