from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm
from accounts.models import Team, User, Profile
from django.contrib import messages
from django.db import transaction

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

#@transaction.atomic dekoratörü ile
# İşlem, tüm kod bloğunun çalışması bittikten sonra ya tamamlanır ya da geri alınır.
# Bu sayede, kullanıcının ve profili ile ilişkili takımın birlikte kaydedilmesi sağlanır.

@transaction.atomic
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            team_name = form.cleaned_data.get('team')
            password = form.cleaned_data.get('password1')
            user = form.save()  # Kullanıcıyı kaydet
            # Eğer kullanıcının profil bilgisi zaten varsa, onu al, yoksa yeni bir profil oluştur
            profile, created = Profile.objects.get_or_create(user=user)
            # Takımı oluştur ve profil ile ilişkilendir
            team, created = Team.objects.get_or_create(name=team_name)
            profile.team = team
            profile.save()
            login(request, user)  # Kullanıcıya otomatik olarak giriş yap
            return redirect('home')  # veya yönlendirmek istediğiniz sayfaya yönlendirin
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})