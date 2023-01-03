from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, get_user_model
from register.forms import SignUpForm
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json


# Create your views here.

@csrf_exempt
def signup(request):
    print(request.body)
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        hashed_password = make_password(password)
        User = get_user_model()
        user = User.objects.create(
            username=username, email=email, password=hashed_password, last_login=timezone.now())
        user.save()
        if user:
            login(request, user)
            return JsonResponse({'token': request.session.session_key})
        else:
            return JsonResponse({'error': 'Signup failed'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
