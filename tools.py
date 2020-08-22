import os
import dialogflow_v2 as dialogflow
from dialogflow_v2.types import TextInput, QueryInput

dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = os.environ['PROJECT_ID']
CREDENTIALS = os.environ['GOOGLE_APP_CREDENTIALS']



def detect_intent_from_text(text, session_id, language_code='en'):
    """
    Create a session, ex
    """
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = TextInput(text=text, language_code=language_code)
    query_input = QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result

def construct_reply(query, session_id):
    response = detect_intent_from_text(query, session_id).fulfillment_text
    return response


