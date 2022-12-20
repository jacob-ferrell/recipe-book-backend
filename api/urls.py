from django.urls import path, include

urlpatterns = [
    path('post-recipe', include('api.urls'))

]
