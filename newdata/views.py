from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import TrainingDataForm

def newdata_view(request):
    if request.method == 'POST':
        form = TrainingDataForm(request.POST)
        print(form)
        if form.is_valid():
            training_data = form.save(commit=False)
            training_data.user = request.user
            training_data.save()
            print(training_data)
            return redirect('home')  # Redirect to home or any other page
    else:
        form = TrainingDataForm()
        print("unvalid")
    return render(request, 'newdata.html', {'form': form, 'User': request.user.profile})
