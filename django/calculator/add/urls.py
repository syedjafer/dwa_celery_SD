from django.urls import path
from add.views import add , result

urlpatterns = [
    path('add/<int:param1>/<int:param2>', add, name='add_func' ),
    path('res/<str:async_key>', result)
]
