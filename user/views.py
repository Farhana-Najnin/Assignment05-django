from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import SignupForm
from django.contrib import messages
from Books.models import Book,Borrow 
from Category.models import Categori
# Create your views here.

class SignUpFormView(CreateView):
    template_name = 'signup.html'
    form_class = SignupForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name,{'form':form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Sign up successfully')
            return redirect('login')
        else:
            return render(request,self.template_name,{'form':form})
    

class LoginFormView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def get(self, request):
        LoginForm = self.form_class()
        return render(request,self.template_name,{'form':LoginForm})
    
    def post(self,request):
        LoginForm = self.form_class(request, data=request.POST)
        if LoginForm.is_valid():
            self.form_valid(LoginForm)
            messages.success(request,'Logged in successfully')
            return redirect('home_page')
        else:
            messages.warning(request,'Invalid Information')
            return render(request,self.template_name,{'form':LoginForm})   


class LogoutFormView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home_page')
    

def ProfileView(request,category_slug = None):
    data = Book.objects.all()
    categoryBook = Categori.objects.all()
    borrow = Borrow.objects.all()

    if category_slug is not None:
        user_id = request.user.id
        category = Categori.objects.get(slug = category_slug)
        data = Book.objects.filter(Category = category)
        borrow = Borrow.objects.filter(id = user_id)

    return render(request, 'profile.html', {'data': data,'borrow': borrow, 'categoryBook': categoryBook})