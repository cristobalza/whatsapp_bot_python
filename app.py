from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
from tools import construct_reply

app = Flask(__name__)

@app.route("/")
def hola():
    return "Hello, Mundo!"

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    """
    Returns the input message that you send back to you.
    """
    # Fetch the message
    msg = request.form.get('Body')
    phone_no = request.form.get('From')
    reply = construct_reply(msg, phone_no)

    # Create reply
    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
