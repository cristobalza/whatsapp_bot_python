from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import os
import dialogflow_v2 as dialogflow 
# from dialogflow_v2.types import TextInput, QueryInput
from utils import *

from google.api_core.exceptions import InvalidArgument
import requests

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'private-key.json'

DIALOGFLOW_PROJECT_ID = 'whatsapp-project-1'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'

# from utils import fetch_reply

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def root():
    return "Hola, Mundo!"

@app.route("/whatsapp", methods=['POST'])
def create():
    """Respond to incoming calls with a simple text message."""
    msg = request.form.get('Body')
    phone_num = request.form.get('From')
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, phone_num)
    text_input = dialogflow.types.TextInput(text=msg, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    # print('Query Text:', response.query_result.query_text)
    # print('Detected intent', response.query_result.intent.display_name)
    # print('Detected intent confidence:', response.query_result.intent_detection_confidence)
    # print('Fulfillmnet text:', response.query_result.fulfillment_text)

    reply_diagfl = response.query_result.fulfillment_text
    resp_twi = MessagingResponse()
    resp_twi.message(reply_diagfl)

    return str(resp_twi)

if __name__ == "__main__":
    app.run()
