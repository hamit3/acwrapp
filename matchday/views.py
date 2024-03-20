from django.shortcuts import render

# Create your views here.
def matchday_view(request):
    return render(request, 'matchday.html', {'User': request.user.profile})