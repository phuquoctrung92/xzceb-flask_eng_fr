"""Machine Translation"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """Translate the text input from English to French"""
    if english_text == "":
        return ""
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = json_to_string(translation)
    return french_text

def french_to_english(french_text):
    """Translate the text input from French to English"""
    if french_text == "":
        return ""
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = json_to_string(translation)
    return english_text

def json_to_string(translated):
    """Convert JSON and return first element in translations value"""
    load_json = json.loads(json.dumps(translated, indent=2, ensure_ascii=False))
    result = load_json["translations"][0]["translation"]
    return result
