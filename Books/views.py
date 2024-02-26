from django.shortcuts import redirect,get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView,DetailView
from user.models import UserBankAccount
from . import forms 
from . models import Borrow,Book
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class BookPost(CreateView):
    model = Book
    form_class = forms.BookForm
    template_name = 'home.html'
    success_url = reverse_lazy('home.html')
    def form_valid(self, form):
        return super().form_valid(form)

class bookDetailsPost(DetailView):
    model = Book
    template_name = 'details.html'
    pk_url_kwarg = 'id'

    def post(self, *args, **kwargs):
            commentform = forms.CommentForm(data=self.request.POST)
            post = self.get_object()
            if commentform.is_valid():
                new_comment = commentform.save(commit=False)
                new_comment.post = post 
                new_comment.save()
            return self.get(self, *args, **kwargs)
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object 
        comments = post.comment.all()
        commentform = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = commentform
        return context 
    
def borrowBook(request,id):
    book = get_object_or_404(Book, pk=id)
    user_profile, created = UserBankAccount.objects.get_or_create(user=request.user)

    if book.quantity > 0:
            if user_profile.balance > 100:
                borrow = Borrow.objects.create(user=request.user, book=book)
                borrow.save()
                book.quantity -= 1
                book.save()
                useraccount = user_profile[0] if created else user_profile
                useraccount.balance -= book.price
                useraccount.save()
                messages.success(request, 'You borrowed book Successfully!!!!!')
                return redirect('profile')
            else:
                messages.error(request, 'You donot have sufficient balance to borrow this book')
                return redirect('deposit')
    else:
        messages.success(request, 'This book out of stock')
        return redirect('home_page')
    return redirect('profile')

def returnBook(request, id):
    borrow = get_object_or_404(Borrow, pk=id)
    book = borrow.book
    user_profile = UserBankAccount.objects.get_or_create(user=request.user)[0]
    if borrow.user == request.user:
        borrow.delete() 
        book.quantity += 1
        book.save()
        user_profile.balance += book.price 
        user_profile.save()
        messages.success(request, 'You have returned the book successfully!!!')
    else:
        messages.error(request, 'You arenot authorize for return book')
    return redirect('profile')