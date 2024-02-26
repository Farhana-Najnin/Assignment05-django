from django.db import models
from Category.models import Categori
from django.contrib.auth.models import User 
# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Categori,on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to = 'media/uploads/',blank=True,null=True)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    
class comment(models.Model):
    post = models.ForeignKey(Book, on_delete = models.CASCADE, related_name = "comment")
    name =  models.CharField(max_length = 60)
    email  = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return f"comment by{self.name}"

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username} - {self.book.name}"