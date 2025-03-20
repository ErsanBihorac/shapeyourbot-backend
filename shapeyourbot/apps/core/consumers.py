import json
from channels.generic.websocket import WebsocketConsumer
from .rag import receive_llm_answer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            "type": "connection_established",
            "message": "You are now connected!"
        }))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        
        print("message", message)
        
        self.send(text_data=json.dumps({
            "type": "chat",
            "message": message
        }))

        # add streaming?
        answer = receive_llm_answer(message)

        self.send(text_data=json.dumps({
            "type": "chat",
            "message": answer
        }))