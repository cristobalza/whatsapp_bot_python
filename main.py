from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route("/")
def hola():
    return "Hola, Mundo!"

@app.route("/whatsapp", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""

    msg = request.form.get('Body')

    resp = MessagingResponse()
    resp.message("You said: {}".format(msg))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)
