from django.shortcuts import redirect, render
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Notification
from .forms import NotificationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages


@user_passes_test(lambda u: u.is_superuser)
def set_notification(request):
    form = NotificationForm(request.POST)
    response = {'form': form}

    if (request.method == 'POST'):
        if (form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} has been made a notification for user!')
            return redirect('home')
    return render(request, 'set_notification.html', response)

@user_passes_test(lambda u: u.is_superuser)
def get_notification(request):
    form = NotificationForm(request.POST)
    if (request.method == 'POST'):
        if (form.is_valid()):
            form.save()
            notif_data = {}
            notif_data['title'] = request.POST.get('title')
            notif_data['messages'] = request.POST.get('messages')
            return JsonResponse(notif_data, safe=False)
    return render(request, '')

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
