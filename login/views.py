from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponse()
            response.cookies['sessionid'] = request.session.session_key
            print(request.session.session_key)
            print(response)
            return response
        else:
            return JsonResponse({'error': 'Login failed'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
    
def logout_view(request):
    logout(request)
    request.session.delete()
    return JsonResponse({'success': True})