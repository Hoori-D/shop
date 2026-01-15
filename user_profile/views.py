from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib.auth import get_user_model

from user_profile.forms import ProfileForm, UserForm
from user_profile.models import Profile


class IndexView(DetailView):
    model = get_user_model()
    template_name = 'user_profile/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль'
        return context


# @login_required
# def change_profile(request, pk):
#     user = request.user
#     all_users = get_user_model().objects.values_list('username', flat=True)
#     try:
#         profile = Profile.objects.get(user=request.user)
#     except Profile.DoesNotExist:
#         profile = Profile.objects.create(user=request.user)
#     if request.method == 'POST':
#         if request.FILES.get('image'):
#             image_file = request.FILES.get('image')
#             profile.image = image_file
#             messages.success(request,
#                              "Изображение обновлено")
#         if request.POST.get('username') and request.POST.get('username') != user.username:
#             if request.POST.get('username') in all_users:
#                 messages.warning(request,"Данное имя уже используется")
#             else:
#                 profile.user.username = request.POST.get('username')
#                 messages.success(request,"Имя обновлено")
#         if request.POST.get('gender') and profile.gender != request.POST.get('gender'):
#             profile.gender = request.POST.get('gender')
#             messages.success(request,
#                              "Пол обновлен")
#         profile.user.save()
#         profile.save()
#         return redirect(reverse_lazy('user_profile:index',kwargs={'pk': pk}))
#     else:
#         form = UserProfileForm(instance=profile)
#
#     return render(request,'user_profile/index.html',{'form': form, 'title': f'Профиль - {user.username}', 'profile': profile})


@login_required
def profile_update(request, pk):
    user = request.user
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        user_form = UserForm(request.POST, instance=user)
        if profile_form.is_valid():
            if profile_form.has_changed():
                messages.success(request,
                             "Профиль обновлен")
            profile_form.save()
        if user_form.is_valid():
            if user_form.has_changed():
                changed_fields = user_form.changed_data
                if 'email' in changed_fields:
                    send_mail("Subject here",
                              "Here is the message.",
                              "from@example.com",
                              ["to@example.com"],
                              fail_silently=False,
                    )
                    messages.success(request,
                                     "Почта обновлена")
                messages.success(request,
                             "Пользователь обновлен")
            user_form.save()
    else:
        profile_form = ProfileForm(instance=profile)
        user_form = UserForm(instance=user)
    return render(request,
                  'user_profile/index.html',
                  {
                      'profile_form': profile_form, 'user_form': user_form, 'title': f'Профиль - {user.username}'
                  })