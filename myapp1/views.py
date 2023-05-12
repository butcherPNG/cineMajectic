from django.shortcuts import render
from django.views.generic import CreateView

from myapp1.forms import SearchForm


from myapp1.models import User
from django.urls import reverse_lazy
from myapp1.forms import RegisterUserForm
from django.shortcuts import render
from django.views.generic import CreateView




# Create your views here.
def index_page(request):
    return render(request, 'index.html')

def film_page(request):
    return render(request, 'film.html')

def order_page(request):
    return render(request, 'order.html')

def login_page(request):
    return render(request, 'login_index.html')

def about_page(request):
    return render(request, 'about.html')



def index_page(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'search_results.html', {'query': form.cleaned_data['query']})
    else:
        form = SearchForm()
    return render(request, 'index.html', {'form': form})



class RegisterUser(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login_index')


def registration(request):
    if request.method == 'POST':
        username = method.POST['username']
        phone_number = method.POST['phone_number']
        email = method.POST['email']
        password = method.POST['password']

        user = User.objects.create_user(username = username, phone_number = phone_number, email = email,
                                        password = password)

        user.save()
        return user



def text(request):
    return render(request, 'text.html')

def login(request):
    return render(request, 'registration/login.html')


