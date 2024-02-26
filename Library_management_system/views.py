from django.shortcuts import render
from Books.models import Book
from Category.models import Categori

def home(request, category_slug = None):
    data = Book.objects.all()
    bookCategory = Categori.objects.all()

    if category_slug is not None:
        category = Categori.objects.get(slug = category_slug)
        data = Book.objects.filter(category = category)

    return render(request, 'home.html', {'data': data, 'book_category': bookCategory})