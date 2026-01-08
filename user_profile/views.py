from django.contrib.auth.decorators import login_required
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
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        profile.image = image_file
        profile.save()
        return redirect(reverse_lazy('user_profile:index',kwargs={'pk': pk}))
    else:
        form = UserProfileForm(instance=profile)

    return render(request,'user_profile/index.html',{'form': form})