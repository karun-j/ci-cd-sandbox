# app.py
import requests
from pdb import set_trace

def api_request():
    # This function makes an API request and triggers debugging on failure
    try:
        response = requests.get("https://example.com/api")  # Replace with your API endpoint
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        print(f"Error occurred: {e}")  # Print the error message
        set_trace()  # Trigger the debugger when an error occurs

if __name__ == "__main__":
    api_request()  # Call the function to execute the API request
