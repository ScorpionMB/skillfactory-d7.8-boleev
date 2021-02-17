from django.shortcuts import render
from .models import Author, Book, Publisher, Friend
from .forms import ProfileCreationForm
from django.views.generic import ListView, FormView  
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import login, authenticate

def lib(request):
    context = {}
    return render(request, 'p_library/lib.html', context)

def test(request):
    books = Book.objects.all()
    context = {'books': books, "title": "мою библиотеку",}
    return render(request, 'p_library/test.html', context)

def index(request):
    context = {}
    if request.user.username == 'admin':
        return render(request, 'p_library/index.html', context)
    if request.user.is_authenticated:  
        context['username'] = request.user.username
        context['github_url'] = SocialAccount.objects.get(provider='github', user=request.user).extra_data['html_url']
    return render(request, 'p_library/index.html', context)

def publisher(request):
    publishers = Publisher.objects.all()
    context = {'publishers': publishers}
    return render(request, 'p_library/publishers.html', context)

def friends(request):
    friends = Friend.objects.all()
    context = {'friends': friends}
    return render(request, 'p_library/friends_book.html', context)

class AuthorList(ListView):  
    model = Author  
    template_name = 'p_library/authors_list.html'

class BookList(ListView):  
    model = Book  
    template_name = 'p_library/book_list.html'

class RegisterView(FormView):  
    form_class = UserCreationForm  
  
    def form_valid(self, form):  
        form.save()  
        username = form.cleaned_data.get('username')  
        raw_password = form.cleaned_data.get('password1')  
        login(self.request, authenticate(username=username, password=raw_password))  
        return super(RegisterView, self).form_valid(form)  
   
class CreateUserProfile(FormView):  
    form_class = ProfileCreationForm  
    template_name = 'p_library/profile-create.html'  
    success_url = reverse_lazy('p_library:index')  
  
    def dispatch(self, request, *args, **kwargs):  
        if self.request.user.is_anonymous:  
            return HttpResponseRedirect(reverse_lazy('p_library:login'))  
        return super(CreateUserProfile, self).dispatch(request, *args, **kwargs)  
  
    def form_valid(self, form):  
        instance = form.save(commit=False)  
        instance.user = self.request.user  
        instance.save()  
        return super(CreateUserProfile, self).form_valid(form)