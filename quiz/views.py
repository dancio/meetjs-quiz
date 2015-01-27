from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required()
def question(request):
    return render(request, 'question.html')


@login_required()
def thanks(request):
    return render(request, 'thanks.html')
