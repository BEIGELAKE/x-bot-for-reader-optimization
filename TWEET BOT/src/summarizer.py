import cohere
from config.config import config
from utils.logger import log_error

co = cohere.Client(config.cohere_api_key)

def summarize_text(text):
    try:
        response = co.summarize(text=text, length="short")
        return response.summary
    except cohere.CohereError as e:
        log_error(f"Cohere API error: {e}")
        return "Error summarizing the content."
