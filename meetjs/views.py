from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def login(request):
    if request.user.is_authenticated():
        return redirect(reverse('question'))
    return render(request, 'login.html')
