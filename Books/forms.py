from django import forms 
from .models import Book,comment

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['name','email','body']