from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from order import consumers

application = ProtocolTypeRouter(
    {
        "websocket": URLRouter(
            [
                path("ws/some_path/", consumers.NotificationConsumer),
            ]
        ),
    }
)
