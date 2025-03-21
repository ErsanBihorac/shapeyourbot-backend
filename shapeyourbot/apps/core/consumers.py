import json
from channels.generic.websocket import WebsocketConsumer

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

        # ai answer
        answer = "AI: This will be the response to your message, answered by an AI."

        self.send(text_data=json.dumps({
            "type": "chat",
            "message": answer
        }))