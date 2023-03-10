from django.shortcuts import render
from myapp.forms import UserCommentsForm
from .models import UserComments
from django.http import JsonResponse

# Create your views here.


def form_view(request):
    form = UserCommentsForm()

    if request.method == 'POST':
        form = UserCommentsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            uc = UserComments(
                first_name = cd['first_name'],
                last_name = cd['last_name'],
                comment = cd ['comment'],
            )
            
            uc.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'blog.html', {'form': form})