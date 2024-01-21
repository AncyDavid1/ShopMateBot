# from fastapi import FastAPI
# from pydantic import BaseModel
# from rasa.core.agent import Agent
# from rasa.nlu.model import Interpreter
# from rasa.utils.endpoints import EndpointConfig
#
# app = FastAPI()
#
# class Message(BaseModel):
#     message: str
#
# nlu_model_path = "./models/nlu"  # Replace with the actual path to your NLU model directory
# core_model_path = "./models/20240118-141625-simple-pound.tar.gz"
# action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
#
# nlu_interpreter = Interpreter.load(nlu_model_path)
# agent = Agent.load(core_model_path, interpreter=nlu_interpreter, action_endpoint=action_endpoint)
#
# @app.post("/predict")
# async def predict(message: Message):
#     response = await agent.handle_text(message.message)
#     return {"response": response[0]['text']}
#
# if __name__ == "__main__":
#     import uvicorn
#
#     uvicorn.run(app, host="127.0.0.1", port=8000)
