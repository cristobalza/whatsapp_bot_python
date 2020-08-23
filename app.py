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
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=msg, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    print('Query Text:', response.query_result.query_text)
    print('Detected intent', response.query_result.intent.display_name)
    print('Detected intent confidence:', response.query_result.intent_detection_confidence)
    print('Fulfillmnet text:', response.query_result.fulfillment_text)
    # sendMessage()
    return response.query_result.fulfillment_text
    
def whatsapp_reply(phone_num, message):
    
    url = "https://api.twilio.com/2010-04-01/Accounts/ACb4f3673da88894b59e7943e7051cfe39/Messages.json"

    payload = {'From': 'whatsapp:'+ my_phone_number,
    'Body':message,
    'To':phone_num
    }
    
    headers = {'Authorization': 'Basic QUNiNGYzNjczZGE4ODg5NGI1OWU3OTQzZTcwNTFjZmUzOTpkOWI4N2VjOTY5OTk1ZDc3MDliNDg3OWEzY2U5ZWNkNQ=='}
    response = requests.request("GET", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))
    return ""
if __name__ == "__main__":
    app.run()
