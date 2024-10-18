# debug.py
import requests
from pdb import set_trace

def api_request():
    try:
        response = requests.get("https://example.com/api")
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error occurred: {e}")
        set_trace()  # Trigger pdb debugger

if __name__ == "__main__":
    api_request()
