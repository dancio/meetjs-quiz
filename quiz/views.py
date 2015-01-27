from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


from .forms import AnswerForm


@login_required()
def question(request):
    form = AnswerForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        answer = form.save(commit=False)
        answer.user = request.user
        answer.save()
        form.save_m2m()
        return redirect(reverse('thanks'))

    return render(request, 'question.html', {'form': form})


@login_required()
def thanks(request):
    return render(request, 'thanks.html')
