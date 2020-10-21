from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from .tasks import create_random_schedule, create_random_user_accounts
from .forms import GenerateRandomUserForm


def schedule_veiw(request):
    create_random_schedule('day')
    template_name = 'entry/index.html'
    return render(request, template_name)


class UsersListView(ListView):
    template_name = 'entry/users_list.html'
    model = User


class GenerateRandomUserView(FormView):
    template_name = 'entry/generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')
