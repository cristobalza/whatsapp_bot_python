from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route("/")
def hola():
    return "Hello, Mundo!"

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    """
    Returns the input message that you send back to you.
    """

    msg = request.form.get('Body')

    resp = MessagingResponse()
    resp.message("You said: {}".format(msg))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
