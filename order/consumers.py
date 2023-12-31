from channels.generic.websocket import AsyncWebsocketConsumer
import json


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Добавим пользователя в группу для персонализированных уведомлений
        if self.scope["user"].is_authenticated:
            self.group_name = f"user_{self.scope['user'].id}"
            await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Удаление пользователя из группы при отключении
        if hasattr(self, "group_name"):
            await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get(
            "message"
        )  # Используем .get для безопасного извлечения
        if message:
            # Производим обработку полученного сообщения
            await self.send(text_data=json.dumps({"message": message}))

    async def order_status_change(self, event):
        # Отправка уведомления о смене статуса заказа
        await self.send(
            text_data=json.dumps(
                {"order_id": event["order_id"], "status": event["status"]}
            )
        )
