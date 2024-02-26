from django.urls import path
from . import views
urlpatterns = [
    path('books/', views.BookPost.as_view(), name='bookPost'),
    path('book_detail/<int:id>', views.bookDetailsPost.as_view(), name='book_details'),
    path('return/<int:id>/', views.returnBook, name='return'),
    path('borrow/<int:id>/', views.borrowBook, name='borrow'),

]