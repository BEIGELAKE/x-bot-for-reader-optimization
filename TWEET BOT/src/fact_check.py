import requests
from utils.logger import log_error


def fact_check(text):
    try:
        # Simulating a fact-checking API request (replace with a real one if available)
        # For example, PolitiFact API or similar services.
        fact_check_url = "https://somefactcheckingapi.com/check"
        response = requests.post(fact_check_url, json={"query": text})

        if response.status_code == 200:
            return response.json()['result']
        else:
            return "Could not verify the claim."

    except Exception as e:
        log_error(f"Fact-checking error: {e}")
        return "Error occurred during fact-checking."
