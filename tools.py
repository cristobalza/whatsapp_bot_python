import os
import dialogflow_v2 as dialogflow
from dialogflow_v2.types import TextInput, QueryInput

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "secure-site-280108-a72354178baf.json"
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID="secure-site-280108"


def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = TextInput(text=text, language_code=language_code)
    query_input = QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result


def fetch_reply(query, session_id):
    """
    Takes a query and returns in a text form
    """
    response = detect_intent_from_text(query,session_id)
    return response.fulfillment_text
