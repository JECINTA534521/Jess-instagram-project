from django.conf.urls import url
from . import views
from .views import (
InboxView, ThreadView, CreateDirectMessage, DeleteDirectMessage, ViewDirectMessage
)


urlpatterns = [
    url('inbox/', InboxView.as_view(), name='direct_messages-inbox'),
    url('thread/<str:username>/', ThreadView.as_view(), name='direct_messages-thread'),
    url('new/', CreateDirectMessage.as_view(), name='direct_messages-new'),
    url('<int:pk>/', ViewDirectMessage.as_view(), name='direct_messages-detail'),
    url('<int:pk>/delete/', DeleteDirectMessage.as_view(), name='direct_messages-delete'),
    ]
