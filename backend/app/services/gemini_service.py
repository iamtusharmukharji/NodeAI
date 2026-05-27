from app.cred_loder import creds
from openai import OpenAI
import json

API_KEY = creds.api_key["GEMINI_API_KEY"]
API_URL = creds.api_key["GEMINI_API_URL"]
MODEL = creds.api_key["GEMINI_MODEL"]

sys_instructions = '''

you are a chatbot that turns an RGB led to the color specified by the user query. You will only respond
with the RGB values in the format {"sucess":true, data: [R, G, B], message:<some user friendly message>}. Do not include any other text in your response.
If user query is not a color related, respond with {"success": false, "data": null, message:<some user friendly message>}

'''

class NodeGemini:

    def __init__(self):
        
        self.client = OpenAI(
            api_key=  API_KEY, 
            base_url= API_URL
        )

    def get_response(self, user_prompt):
        
        response = self.client.chat.completions.create(
            
            model= MODEL,
            messages=[
                {"role": "system", "content": sys_instructions},
                {"role": "user", "content": user_prompt}
            ]
        )
        print(response.choices[0].message.content)
        return json.loads(response.choices[0].message.content)
    


node_gemini = NodeGemini()
