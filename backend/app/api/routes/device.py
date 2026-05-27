
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services.gemini_service import node_gemini
from app.services.mqtt_service import publish_mqtt
from app.cred_loder import creds
import asyncio

router = APIRouter(
    prefix="/device",
    tags=["Device"]
)

publish_topic = creds.mqtt["COMMAND_TOPIC"]

@router.post("/prompt")
async def prompt(prompt : str):
    try:
        
        llm_response = await asyncio.to_thread(node_gemini.get_response, prompt)

        if llm_response['success']:
            
            msg = {
                "cmd_type" : "rgb",
                "cmd" : llm_response["data"]
            }

            publish_mqtt(publish_topic, msg)

        response = {"success":True, "data":llm_response["message"]}
        return JSONResponse(content=response, status_code=200)
    
    except Exception as err:
        response = {"success":False, "message":str(err)}
        return JSONResponse(content=response, status_code=400)