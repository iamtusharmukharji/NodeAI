from app.cred_loder import creds
from .mqtt_service import node_mqtt
from openai import OpenAI
from openai import RateLimitError

import json

API_KEY = creds.api_key["GEMINI_API_KEY"]
API_URL = creds.api_key["GEMINI_API_URL"]
MODEL = creds.api_key["GEMINI_MODEL"]

sys_instructions = '''

you are a chatbot that turns an RGB led to the color specified by the user query and can tell user's device informaion like temperture, humidiy,
device's rssi(signl strength) and firmware version based on data that will be given to you. You will only respond
with the RGB values in the format {"success":true, "data": [R, G, B], "message":<some user friendly message>}. Do not include any other text in your response.
If user query is not a color related, or data related to device then respond with {"success": false, "data": null, "message":<some user friendly message>}
If user asks about any data like temperature, humidity of his room, etc or signal strength or firmware version you need to lookup to this data 
where s0-s4 is swtich's current state 0-> Off, 1 -> On, temp is in degree celcius, humid is in % humidity, rssi in value, and version is firmware version
'''
sys2 = '''
In case of user asking only for data the response structure should be like {"success":true, data: null, message:<some user friendly message with data>}
otherwise the sructure should be {"success":true, "data": null, "message":<some user friendly message with data>}
'''

class NodeGemini:

    def __init__(self):
        
        self.client = OpenAI(
            api_key=  API_KEY, 
            base_url= API_URL
        )

    def get_response(self, user_prompt):
        try:
            response = self.client.chat.completions.create(
                
                model= MODEL,
                messages=[
                    {"role": "system", "content": f"{sys_instructions}\n{node_mqtt.device_data}\n{sys2}"},
                    {"role": "user", "content": user_prompt}
                ]
            )
            print(response.choices[0].message.content)
            return json.loads(response.choices[0].message.content)
        except RateLimitError:
            return {
                "success": False,
                "data" : None,
                "message": "AI request limit reached. Please try again later or switch to another Gemini API key/model."
            }

    


node_gemini = NodeGemini()
