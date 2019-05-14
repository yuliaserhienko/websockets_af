import json

from asgiref.sync import async_to_sync


from channels.generic.websocket import WebsocketConsumer


NOTIFICATION_GROUP_NAME = 'notifocations'


class NotificationConsumer(WebsocketConsumer):
    def connect(self):

        async_to_sync(self.channel_layer.group_add)(
            NOTIFICATION_GROUP_NAME,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            NOTIFICATION_GROUP_NAME,
            self.channel_name
        )

    def receive(self, text_data):
        async_to_sync(self.channel_layer.group_send)(
            NOTIFICATION_GROUP_NAME,
            {
                'type': 'notification',
                'message': text_data
            }
        )

    # Receive message from room group
    def notification(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
