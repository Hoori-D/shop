from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib.auth import get_user_model

from user_profile.forms import UserProfileForm
from user_profile.models import Profile


class IndexView(DetailView):
    model = get_user_model()
    template_name = 'user_profile/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль'
        return context


@login_required
def change_profile(request, pk):
    user = request.user
    all_users = get_user_model().objects.values_list('username', flat=True)
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    if request.method == 'POST':
        if request.FILES.get('image'):
            image_file = request.FILES.get('image')
            profile.image = image_file
            messages.success(request,
                             "Изображение обновлено")
        if request.POST.get('username') and request.POST.get('username') != user.username:
            if request.POST.get('username') in all_users:
                messages.warning(request,"Данное имя уже используется")
            else:
                profile.user.username = request.POST.get('username')
                messages.success(request,"Имя обновлено")
        if request.POST.get('gender') and profile.gender != request.POST.get('gender'):
            profile.gender = request.POST.get('gender')
            messages.success(request,
                             "Пол обновлен")
        profile.user.save()
        profile.save()
        return redirect(reverse_lazy('user_profile:index',kwargs={'pk': pk}))
    else:
        form = UserProfileForm(instance=profile)

    return render(request,'user_profile/index.html',{'form': form, 'title': f'Профиль - {user.username}', 'profile': profile})