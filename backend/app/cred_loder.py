import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Credentials:
    def __init__(self):
        self.api_key = None
        self.mqtt = None


    def load_credentials(self):

        with open(f"{BASE_DIR}/credentials.json", 'r') as file:
            credentials = json.load(file)
        
        self.api_key = credentials["api_keys"]
        self.mqtt = credentials["mqtt_creds"]
        return None
    
creds = Credentials()
creds.load_credentials()