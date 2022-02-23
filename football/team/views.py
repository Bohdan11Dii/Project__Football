from email import message
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .models import Model
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login





from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

def index(request):
	return render(request, 'team/index.html')

def loginform(request):
    return render(request, 'team/index.html')





@login_required
def basic(request):
    current_user = request.user
    user_id = current_user.id
    print(user_id)
    context = {'user_id': user_id}
    return render(request, 'team/basic.html', context)


def first(request):
	return render(request, 'team/first.html')


def registerform(request):
	return render(request, 'team/register.html')


class RegisterView(SuccessMessageMixin, CreateView):
	model = User
	fields = ['username', 'password', 'email']
	template_name = 'team/register.html'
	success_url = reverse_lazy('registerform')
	success_message = "Аккаунт створено, будь ласка увійдіть"

	def form_valid(self, form):
		form.instance.password = make_password(form.instance.password)
		return super().form_valid(form)


from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve, reverse
from django.http import HttpResponseRedirect
from football import settings

class LoginRequiredMiddleware(MiddlewareMixin):
    """
    Middleware that requires a user to be authenticated to view any page other
    than LOGIN_URL. Exemptions to this requirement can optionally be specified
    in settings by setting a tuple of routes to ignore
    """
    def process_request(self, request):
        assert hasattr(request, 'user'), """
        The Login Required middleware needs to be after AuthenticationMiddleware.
        Also make sure to include the template context_processor:
        'django.contrib.auth.context_processors.auth'."""

        if not request.user.is_authenticated:
            current_route_name = resolve(request.path_info).url_name

            if not current_route_name in settings.AUTH_EXEMPT_ROUTES:
                return HttpResponseRedirect(reverse(settings.AUTH_LOGIN_ROUTE))

def players(request):
    models = Model.objects.all()
    return render(request, 'team/players.html', {'name' : 'Нападаючий', "models": models})

def gallery(request):
    return render(request, 'team/gallery.html')

def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()


        messages.info(request, "Дякую за ваше повідомлення")
    return render(request, 'team/contact.html' )


def bloh(request):
    return render(request, 'team/bloh.html')










